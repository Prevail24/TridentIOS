from dataclasses import dataclass


@dataclass(frozen=True)
class HttpArtifactObservation:
    """
    A file retrieved from an HTTP endpoint and stored as mission evidence.
    """

    source_url: str
    evidence_path: str
    filename: str
    sha256: str
    size: int

    content_type: str | None = None
    status_code: int | None = None
    final_url: str | None = None
    host_header: str | None = None
