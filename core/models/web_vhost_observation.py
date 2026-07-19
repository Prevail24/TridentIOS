from dataclasses import dataclass


@dataclass(frozen=True)
class WebVhostObservation:
    """
    A virtual host discovered through HTTP Host-header enumeration.

    This model is tool-neutral. Gobuster vhost, ffuf, and future
    DNS/HTTP discovery sensors can all produce it.
    """

    base_url: str
    hostname: str
    url: str

    status_code: int | None = None
    content_length: int | None = None
    redirect_location: str | None = None
