from core.models.httpx_observation import HttpxObservation
from core.models.observation import Observation
from core.services.observation_emitter import ObservationEmitter


class HttpxObservationTranslator:
    """
    Converts HTTPX domain observations into canonical Trident observations.

    One HTTPX response becomes one contextual `http_endpoint`
    observation so the relationship between the host, URL, status,
    title, server, and technologies remains intact.
    """

    def __init__(self):
        self.emitter = ObservationEmitter()

    def translate(
        self,
        observations: list[HttpxObservation],
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
                category="http_endpoint",
                data={
                    "url": observation.url,
                    "host": observation.host,
                    "host_ip": observation.host_ip,
                    "host_header": observation.host_header,
                    "probe_url": observation.probe_url,
                    "port": observation.port,
                    "scheme": observation.scheme,
                    "status_code": observation.status_code,
                    "redirect_location": observation.redirect_location,
                    "title": observation.title,
                    "webserver": observation.webserver,
                    "content_type": observation.content_type,
                    "path": observation.path,
                    "response_time": observation.response_time,
                    "content_length": observation.content_length,
                    "technologies": observation.technologies,
                    "ipv4_addresses": observation.ipv4_addresses,
                    "ipv6_addresses": observation.ipv6_addresses,
                },
                confidence=1.0,
            )

            emitted.append(canonical)

        return emitted
