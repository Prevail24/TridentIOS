from core.models.nmap_observation import NmapObservation
from core.graph.graph_builder import GraphBuilder


class NmapObservationTranslator:
    """
    Translates native Nmap observations into canonical Trident observation text
    and can build a knowledge graph from Nmap observations.
    """

    def translate(self, obs: NmapObservation) -> str:
        return (
            f"{obs.host} has {obs.state} "
            f"{obs.protocol} port {obs.port} "
            f"running {obs.service or 'unknown service'}"
        )

    def translate_many(self, observations: list[NmapObservation]) -> list[str]:
        return [self.translate(obs) for obs in observations]

    def build_graph(self, observations: list[NmapObservation]):
        builder = GraphBuilder()

        for obs in observations:
            builder.add_host_port_service(
                host_value=obs.host,
                port_value=obs.port,
                service_value=obs.service,
                product_value=obs.product,
                version_value=obs.version,
            )

        return builder.graph