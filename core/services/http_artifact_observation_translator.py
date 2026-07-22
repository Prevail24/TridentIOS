from core.models.http_artifact_observation import HttpArtifactObservation
from core.models.observation import Observation
from core.services.observation_emitter import ObservationEmitter


class HttpArtifactObservationTranslator:
    """
    Converts retrieved HTTP artifacts into canonical Trident observations.
    """

    def __init__(self):
        self.emitter = ObservationEmitter()

    def translate(
        self,
        observations: list[HttpArtifactObservation],
        *,
        mission_id: str | None,
        tool_run_id: str | None,
        evidence_id: str | None,
    ) -> list[Observation]:
        emitted = []

        for observation in observations:
            canonical = self.emitter.emit(
                mission_id=mission_id,
                tool_run_id=tool_run_id,
                evidence_id=evidence_id,
                category="http_artifact",
                data={
                    "source_url": observation.source_url,
                    "final_url": observation.final_url,
                    "host_header": observation.host_header,
                    "evidence_path": observation.evidence_path,
                    "filename": observation.filename,
                    "content_type": observation.content_type,
                    "size": observation.size,
                    "sha256": observation.sha256,
                    "status_code": observation.status_code,
                },
                confidence=1.0,
            )

            emitted.append(canonical)

        return emitted
