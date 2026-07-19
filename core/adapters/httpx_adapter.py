import json
import subprocess
from urllib.parse import urlparse, urlunparse

from core.adapters.base import ToolAdapter
from core.engine import TridentEngine
from core.parsers.httpx.json_parser import HttpxJsonParser
from core.services.httpx_observation_translator import (
    HttpxObservationTranslator,
)
from core.services.observation_engine import ObservationEngine


class HttpxAdapter(ToolAdapter):
    """
    Execute HTTPX and record its output as mission intelligence.
    """

    def __init__(
        self,
        target: str,
        *,
        host_header: str | None = None,
    ):
        self.target = target
        self.host_header = host_header
        self.engine = TridentEngine()
        self.parser = HttpxJsonParser()
        self.translator = HttpxObservationTranslator()
        self.observation_engine = ObservationEngine()

    def execute(self) -> dict:
        mission_id = self.engine.state.get_active_mission()

        tool_run = self.engine.tool_runs.create(
            tool="httpx",
            target=self.target,
            mission_id=mission_id,
        )

        command = [
            "httpx",
            "-u",
            self.target,
            "-json",
            "-silent",
            "-title",
            "-status-code",
            "-location",
            "-tech-detect",
            "-server",
        ]

        if self.host_header:
            command.extend(["-H", f"Host: {self.host_header}"])

        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )

        records = [
            json.loads(line)
            for raw_line in result.stdout.splitlines()
            if (line := raw_line.strip())
        ]

        for record in records:
            self._annotate_record(record)

        native_observations = self.parser.parse(records)
        observations = self.translator.translate(
            native_observations,
            mission_id=mission_id,
            tool_run_id=tool_run.id,
            evidence_id=None,
        )

        processed = []

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

    def _annotate_record(self, record: dict) -> None:
        record.setdefault("probe_url", record.get("url") or self.target)

        if not self.host_header:
            return

        record["host_header"] = self.host_header
        record["host"] = self.host_header

        parsed = urlparse(record.get("url") or self.target)
        if not parsed.scheme:
            return

        port = record.get("port")
        netloc = self.host_header

        if port:
            try:
                port_number = int(port)
            except (TypeError, ValueError):
                port_number = None

            if (
                port_number
                and (parsed.scheme, port_number)
                not in {("http", 80), ("https", 443)}
            ):
                netloc = f"{self.host_header}:{port_number}"

        record["url"] = urlunparse(parsed._replace(netloc=netloc))
