from dataclasses import dataclass, field


@dataclass
class HttpxObservation:
    url: str
    host: str
    host_ip: str | None
    port: int | None
    scheme: str | None
    status_code: int | None
    title: str | None
    webserver: str | None
    content_type: str | None
    path: str | None
    response_time: str | None
    content_length: int | None
    technologies: list[str] = field(default_factory=list)
    ipv4_addresses: list[str] = field(default_factory=list)
    ipv6_addresses: list[str] = field(default_factory=list)