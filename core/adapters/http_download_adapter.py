from hashlib import sha256
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

from core.adapters.base import ToolAdapter
from core.config import Config
from core.engine import TridentEngine
from core.models.http_artifact_observation import HttpArtifactObservation
from core.services.http_artifact_observation_translator import (
    HttpArtifactObservationTranslator,
)
from core.services.observation_engine import ObservationEngine


class HttpDownloadAdapter(ToolAdapter):
    """
    Download an HTTP artifact and record file metadata as mission intelligence.
    """

    def __init__(
        self,
        url: str,
        *,
        host_header: str | None = None,
    ):
        self.url = url
        self.host_header = host_header
        self.engine = TridentEngine()
        self.translator = HttpArtifactObservationTranslator()
        self.observation_engine = ObservationEngine()

    def execute(self) -> dict:
        mission_id = self.engine.state.get_active_mission()

        tool_run = self.engine.tool_runs.create(
            tool="http_download",
            target=self.url,
            mission_id=mission_id,
        )

        request = Request(self.url)

        if self.host_header:
            request.add_header("Host", self.host_header)

        with urlopen(request, timeout=20) as response:
            content = response.read()
            final_url = response.geturl()
            status_code = response.status
            headers = response.headers

        filename = self._filename(final_url, headers)
        evidence_path = self._evidence_path(tool_run.id, filename)
        evidence_path.write_bytes(content)

        digest = sha256(content).hexdigest()

        native_observation = HttpArtifactObservation(
            source_url=self.url,
            final_url=final_url,
            host_header=self.host_header,
            evidence_path=str(evidence_path),
            filename=filename,
            content_type=headers.get_content_type(),
            size=len(content),
            sha256=digest,
            status_code=status_code,
        )

        observations = self.translator.translate(
            [native_observation],
            mission_id=mission_id,
            tool_run_id=tool_run.id,
            evidence_id=str(evidence_path),
        )

        processed = []

        tool_run.evidence.append(str(evidence_path))

        for observation in observations:
            tool_run.observations.append(observation.id)
            processed.append(
                self.observation_engine.process(observation)
            )

        self.engine.tool_runs.repository.save(tool_run)

        return {
            "tool_run": tool_run,
            "observations": observations,
            "processed": processed,
        }

    def _evidence_path(self, run_id: str, filename: str) -> Path:
        evidence_root = Config.KNOWLEDGE_DIR / "evidence" / "http"
        evidence_root.mkdir(parents=True, exist_ok=True)

        return evidence_root / f"{run_id}-{filename}"

    def _filename(self, final_url: str, headers) -> str:
        disposition = headers.get("Content-Disposition")

        if disposition:
            for part in disposition.split(";"):
                key, _, value = part.strip().partition("=")

                if key.lower() == "filename" and value:
                    return self._safe_filename(value.strip('"'))

        parsed = urlparse(final_url)
        name = unquote(Path(parsed.path).name)

        if not name:
            name = "artifact.bin"

        return self._safe_filename(name)

    def _safe_filename(self, filename: str) -> str:
        safe = "".join(
            character
            if character.isalnum() or character in {".", "-", "_"}
            else "_"
            for character in filename
        ).strip("._")

        return safe or "artifact.bin"
