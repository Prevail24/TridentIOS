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
        mode: str = "dir",
        host_header: str | None = None,
        extensions: str | None = None,
        domain: str | None = None,
        append_domain: bool = True,
        status_codes_blacklist: str = "302,404",
        exclude_status: str | None = None,
        threads: int = 10,
    ):
        return GobusterSensor(
            target=target,
            wordlist=wordlist,
            mode=mode,
            host_header=host_header,
            extensions=extensions,
            domain=domain,
            append_domain=append_domain,
            status_codes_blacklist=status_codes_blacklist,
            exclude_status=exclude_status,
            threads=threads,
        ).collect()
