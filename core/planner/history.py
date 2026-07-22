from dataclasses import dataclass

from core.planner.recommendation import RecommendationStatus


@dataclass(frozen=True)
class RecommendationRecord:
    capability_id: str
    scope: str | None


class PlannerHistory:
    """
    Tracks recommendation lifecycle state for the lifetime of a
    planning session.
    """

    def __init__(self):
        self._statuses: dict[
            RecommendationRecord,
            RecommendationStatus,
        ] = {}

    def mark_status(
        self,
        capability_id: str,
        scope: str | None,
        status: RecommendationStatus,
    ) -> None:
        record = RecommendationRecord(
            capability_id=capability_id,
            scope=scope,
        )

        self._statuses[record] = status

    def status_for(
        self,
        capability_id: str,
        scope: str | None,
    ) -> RecommendationStatus | None:
        record = RecommendationRecord(
            capability_id=capability_id,
            scope=scope,
        )

        return self._statuses.get(record)

    def mark_accepted(
        self,
        capability_id: str,
        scope: str | None,
    ) -> None:
        self.mark_status(
            capability_id,
            scope,
            RecommendationStatus.ACCEPTED,
        )

    def mark_running(
        self,
        capability_id: str,
        scope: str | None,
    ) -> None:
        self.mark_status(
            capability_id,
            scope,
            RecommendationStatus.RUNNING,
        )

    def mark_completed(
        self,
        capability_id: str,
        scope: str | None,
    ) -> None:
        self.mark_status(
            capability_id,
            scope,
            RecommendationStatus.COMPLETED,
        )

    def mark_failed(
        self,
        capability_id: str,
        scope: str | None,
    ) -> None:
        self.mark_status(
            capability_id,
            scope,
            RecommendationStatus.FAILED,
        )

    def has_completed(
        self,
        capability_id: str,
        scope: str | None,
    ) -> bool:
        return (
            self.status_for(capability_id, scope)
            is RecommendationStatus.COMPLETED
        )

    def clear(self) -> None:
        self._statuses.clear()