from core.models.observation import Observation
from core.models.web_path_observation import WebPathObservation
from core.services.observation_emitter import ObservationEmitter


class GobusterObservationTranslator:
    """
    Converts tool-neutral WebPathObservation objects into
    canonical Trident observations.

    The translator records only what was observed.
    It does not infer exposure, vulnerability, or significance.
    """

    def __init__(self):
        self.emitter = ObservationEmitter()

    def translate(
        self,
        observations: list[WebPathObservation],
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
                category="web_path",
                data={
                    "base_url": observation.base_url,
                    "path": observation.path,
                    "url": observation.url,
                    "status_code": observation.status_code,
                    "content_length": observation.content_length,
                    "redirect_location": observation.redirect_location,
                },
                confidence=1.0,
            )

            emitted.append(canonical)

        return emitted
