from dataclasses import dataclass


@dataclass(frozen=True)
class WebPathObservation:
    """
    A web resource discovered through content enumeration.

    This model is tool-neutral. Gobuster, ffuf, Feroxbuster,
    and future discovery sensors can all produce it.
    """

    base_url: str
    path: str
    url: str

    status_code: int | None = None
    content_length: int | None = None
    redirect_location: str | None = None