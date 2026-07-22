from dataclasses import dataclass

from core.planner.recommendation import RecommendationStatus
from core.repositories.planner_history_repository import (
    PlannerHistoryRepository,
)


@dataclass(frozen=True)
class RecommendationRecord:
    capability_id: str
    scope: str | None


class PlannerHistory:
    """
    Tracks recommendation lifecycle state.

    With no mission ID, history remains in memory.

    When bound to a mission, lifecycle state is persisted through a
    PlannerHistoryRepository and survives process restarts.
    """

    def __init__(
        self,
        mission_id: str | None = None,
        repository: PlannerHistoryRepository | None = None,
    ) -> None:
        if repository is not None and mission_id is None:
            raise ValueError(
                "A mission ID is required when using a "
                "Planner history repository."
            )

        if mission_id is not None:
            mission_id = mission_id.strip()

            if not mission_id:
                raise ValueError("Mission ID cannot be empty.")

        self.mission_id = mission_id
        self.repository = repository

        if self.mission_id is not None and self.repository is None:
            self.repository = PlannerHistoryRepository()

        self._statuses: dict[
            RecommendationRecord,
            RecommendationStatus,
        ] = {}

        self._load()

    def _load(self) -> None:
        if self.mission_id is None or self.repository is None:
            return

        for item in self.repository.load(self.mission_id):
            capability_id = item.get("capability_id")
            scope = item.get("scope")
            stored_status = item.get("status")

            if not isinstance(capability_id, str) or not capability_id:
                raise ValueError(
                    "Persisted Planner history contains an invalid "
                    "capability ID."
                )

            if scope is not None and not isinstance(scope, str):
                raise ValueError(
                    "Persisted Planner history contains an invalid scope."
                )

            try:
                status = RecommendationStatus(stored_status)
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    "Persisted Planner history contains an invalid status."
                ) from exc

            record = RecommendationRecord(
                capability_id=capability_id,
                scope=scope,
            )

            self._statuses[record] = status

    def _persist(
        self,
        statuses: dict[
            RecommendationRecord,
            RecommendationStatus,
        ],
    ) -> None:
        if self.mission_id is None or self.repository is None:
            return

        records = [
            {
                "capability_id": record.capability_id,
                "scope": record.scope,
                "status": status.value,
            }
            for record, status in sorted(
                statuses.items(),
                key=lambda item: (
                    item[0].capability_id,
                    item[0].scope or "",
                ),
            )
        ]

        self.repository.save(
            self.mission_id,
            records,
        )

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

        updated_statuses = dict(self._statuses)
        updated_statuses[record] = status

        # Persist before replacing in-memory state so a write failure
        # cannot make memory appear newer than durable storage.
        self._persist(updated_statuses)
        self._statuses = updated_statuses

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
        if self.mission_id is not None and self.repository is not None:
            self.repository.clear(self.mission_id)

        self._statuses.clear()
