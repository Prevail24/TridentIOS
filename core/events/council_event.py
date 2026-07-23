from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(frozen=True)
class CouncilEvent:
    """
    Immutable event emitted by a Council member.
    """

    actor: str
    message: str

    event_type: str = "info"
    source: str | None = None
    mission_id: str | None = None
    tool_run_id: str |None = None

    data: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))