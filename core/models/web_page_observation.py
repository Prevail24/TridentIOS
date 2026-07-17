from dataclasses import dataclass, field


@dataclass(frozen=True)
class WebFormObservation:
    """
    A form discovered inside an observed web document.
    """

    method: str
    action: str | None
    inputs: tuple[dict, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class WebPageObservation:
    """
    Tool-neutral intelligence extracted from a web document.

    HTTP clients, crawlers, and future browser-backed sensors may all
    produce this same observation.
    """

    requested_url: str
    final_url: str

    status_code: int
    content_type: str | None
    content_length: int | None

    title: str | None

    headers: dict[str, str] = field(default_factory=dict)
    cookies: tuple[dict, ...] = field(default_factory=tuple)

    links: tuple[str, ...] = field(default_factory=tuple)
    scripts: tuple[str, ...] = field(default_factory=tuple)
    stylesheets: tuple[str, ...] = field(default_factory=tuple)
    images: tuple[str, ...] = field(default_factory=tuple)

    forms: tuple[WebFormObservation, ...] = field(default_factory=tuple)
    comments: tuple[str, ...] = field(default_factory=tuple)
    metadata: dict[str, str] = field(default_factory=dict)

    redirect_history: tuple[str, ...] = field(default_factory=tuple)
