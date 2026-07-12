from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Relationship:
    """
    Canonical relationship between two entities.
    """

    id: str

    source_id: str
    target_id: str

    relationship_type: str

    confidence: float = 1.0
    created_at: datetime = field(default_factory=datetime.utcnow)