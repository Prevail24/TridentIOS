from core.models.nmap_observation import NmapObservation


class NmapObservationTranslator:
    """
    Translates native Nmap observations into canonical Trident observation text.
    """

    def translate(self, obs: NmapObservation) -> str:
        return (
            f"{obs.host} has {obs.state} "
            f"{obs.protocol} port {obs.port} "
            f"running {obs.service or 'unknown service'}"
        )

    def translate_many(self, observations: list[NmapObservation]) -> list[str]:
        return [self.translate(obs) for obs in observations]