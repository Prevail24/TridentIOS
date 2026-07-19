from core.models.observation import Observation
from core.models.web_vhost_observation import WebVhostObservation
from core.services.observation_emitter import ObservationEmitter


class GobusterVhostObservationTranslator:
    """
    Converts virtual-host observations into canonical Trident observations.
    """

    def __init__(self):
        self.emitter = ObservationEmitter()

    def translate(
        self,
        observations: list[WebVhostObservation],
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
                category="web_vhost",
                data={
                    "base_url": observation.base_url,
                    "hostname": observation.hostname,
                    "url": observation.url,
                    "status_code": observation.status_code,
                    "content_length": observation.content_length,
                    "redirect_location": observation.redirect_location,
                },
                confidence=1.0,
            )

            emitted.append(canonical)

        return emitted
