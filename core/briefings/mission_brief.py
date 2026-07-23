from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(frozen=True)
class MissionBrief:
    """
    Canonical operational briefing presented to the Observer.

    A MissionBrief summarizes a completed CouncilSession.
    It is an intelligence product, not evidence.
    """

    mission_id: str | None
    target: str | None

    executive_summary: str
    confidence: float

    key_findings: list[str] = field(default_factory=list)
    priority_actions: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    council_members: list[str] = field(default_factory=list)

    generated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )