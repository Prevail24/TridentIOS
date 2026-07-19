from core.armory.gobuster.sensor import GobusterSensor


class GobusterService:
    """
    Compatibility facade for the Gobuster sensor pipeline.
    """

    def run(
        self,
        target: str,
        wordlist: str,
        *,
        host_header: str | None = None,
        status_codes_blacklist: str = "302,404",
        threads: int = 10,
    ):
        return GobusterSensor(
            target=target,
            wordlist=wordlist,
            host_header=host_header,
            status_codes_blacklist=status_codes_blacklist,
            threads=threads,
        ).collect()
