from dataclasses import dataclass


@dataclass
class NmapObservation:
    """
    Native observation extracted directly from Nmap XML.
    """

    host: str
    port: int
    protocol: str
    state: str
    service: str | None = None
    product: str | None = None
    version: str | None = None
    extrainfo: str | None = None