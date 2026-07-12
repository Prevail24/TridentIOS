from dataclasses import dataclass, field
from datetime import date


@dataclass
class Evidence:
    """
    Evidence represents a source, artifact, clue, or supporting item
    attached to an Observation.
    """

    id: str
    title: str
    evidence_type: str
    source: str
    observation_id: str
    author: str
    created: date
    updated: date
    status: str = "active"

    notes: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
