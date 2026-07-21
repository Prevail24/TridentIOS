from dataclasses import dataclass
from enum import Enum


class RecommendationStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    DEFERRED = "deferred"
    DISMISSED = "dismissed"


class RecommendationPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class Recommendation:
    """
    A deterministic recommendation produced by the Planner.
    """

    capability_id: str
    reason: str

    confidence: str = "Medium"
    priority: RecommendationPriority = RecommendationPriority.MEDIUM
    status: RecommendationStatus = RecommendationStatus.PENDING

    scope: str | None = None
    evidence: tuple[str, ...] = ()
    requires: tuple[str, ...] = ()
    produces: tuple[str, ...] = ()

    available: bool = True
    rule: str | None = None
    required_inputs: tuple[str, ...] = ()

    @property
    def executable(self) -> bool:
        """
        Return True when the recommendation is available,
        requires no additional operator input, and remains pending.
        """
        return (
            self.available
            and not self.required_inputs
            and self.status is RecommendationStatus.PENDING
        )