from dataclasses import dataclass


@dataclass(frozen=True)
class WebPathObservation:
    """
    Native representation of discovered web content.

    Tool-neutral.

    Gobuster, ffuf, feroxbuster and future
    web discovery engines all produce this.
    """

    host: str

    url: str

    path: str

    status_code: int

    content_length: int | None = None

    redirect_location: str | None = None
    