from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Observation:
    """
    Canonical Trident observation.

    Observations are immutable records of something seen.
    They are perception, not interpretation.
    """

    id: str

    mission_id: str | None
    tool_run_id: str | None
    evidence_id: str | None

    category: str
    data: dict

    confidence: float = 1.0
    observed_at: datetime = field(default_factory=datetime.utcnow)