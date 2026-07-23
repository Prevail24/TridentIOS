from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4

from core.planner.recommendation import RecommendationStatus
from core.repositories.planner_history_repository import (
    PlannerHistoryRepository,
)


@dataclass(frozen=True)
class RecommendationRecord:
    capability_id: str
    scope: str | None


@dataclass(frozen=True)
class PlannerHistoryEntry:
    capability_id: str
    scope: str | None
    status: RecommendationStatus


@dataclass(frozen=True)
class PlannerHistoryEvent:
    """
    Immutable record of one Planner lifecycle transition.
    """

    event_id: str
    occurred_at: datetime
    mission_id: str | None

    capability_id: str
    scope: str | None

    previous_status: RecommendationStatus | None
    new_status: RecommendationStatus


class PlannerHistory:
    """
    Tracks recommendation lifecycle state and transition history.

    With no mission ID, history remains in memory.

    When bound to a mission, both the latest lifecycle state and the
    immutable event ledger are persisted through a
    PlannerHistoryRepository.
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

        self._events: list[PlannerHistoryEvent] = []

        self._load()

    def _load(self) -> None:
        if self.mission_id is None or self.repository is None:
            return

        self._load_statuses()
        self._load_events()

    def _load_statuses(self) -> None:
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

    def _load_events(self) -> None:
        if self.mission_id is None or self.repository is None:
            return

        for item in self.repository.load_events(self.mission_id):
            event_id = item.get("event_id")
            occurred_at_value = item.get("occurred_at")
            stored_mission_id = item.get("mission_id")
            capability_id = item.get("capability_id")
            scope = item.get("scope")
            stored_previous_status = item.get(
                "previous_status"
            )
            stored_new_status = item.get("new_status")

            if not isinstance(event_id, str) or not event_id:
                raise ValueError(
                    "Persisted Planner event contains an invalid "
                    "event ID."
                )

            if (
                not isinstance(occurred_at_value, str)
                or not occurred_at_value
            ):
                raise ValueError(
                    "Persisted Planner event contains an invalid "
                    "timestamp."
                )

            try:
                occurred_at = datetime.fromisoformat(
                    occurred_at_value
                )
            except ValueError as exc:
                raise ValueError(
                    "Persisted Planner event contains an invalid "
                    "timestamp."
                ) from exc

            if (
                occurred_at.tzinfo is None
                or occurred_at.utcoffset() is None
            ):
                raise ValueError(
                    "Persisted Planner event timestamp must be "
                    "timezone-aware."
                )

            if stored_mission_id != self.mission_id:
                raise ValueError(
                    "Persisted Planner event mission ID does not "
                    "match its history."
                )

            if not isinstance(capability_id, str) or not capability_id:
                raise ValueError(
                    "Persisted Planner event contains an invalid "
                    "capability ID."
                )

            if scope is not None and not isinstance(scope, str):
                raise ValueError(
                    "Persisted Planner event contains an invalid scope."
                )

            try:
                previous_status = (
                    None
                    if stored_previous_status is None
                    else RecommendationStatus(
                        stored_previous_status
                    )
                )

                new_status = RecommendationStatus(
                    stored_new_status
                )
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    "Persisted Planner event contains an invalid status."
                ) from exc

            self._events.append(
                PlannerHistoryEvent(
                    event_id=event_id,
                    occurred_at=occurred_at,
                    mission_id=stored_mission_id,
                    capability_id=capability_id,
                    scope=scope,
                    previous_status=previous_status,
                    new_status=new_status,
                )
            )

    def _create_event(
        self,
        *,
        record: RecommendationRecord,
        previous_status: RecommendationStatus | None,
        new_status: RecommendationStatus,
    ) -> PlannerHistoryEvent:
        return PlannerHistoryEvent(
            event_id=f"PLE-{uuid4()}",
            occurred_at=datetime.now(UTC),
            mission_id=self.mission_id,
            capability_id=record.capability_id,
            scope=record.scope,
            previous_status=previous_status,
            new_status=new_status,
        )

    def _persist(
        self,
        statuses: dict[
            RecommendationRecord,
            RecommendationStatus,
        ],
        events: list[PlannerHistoryEvent],
    ) -> None:
        if self.mission_id is None or self.repository is None:
            return

        recommendation_records = [
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

        event_records = [
            {
                "event_id": event.event_id,
                "occurred_at": event.occurred_at.isoformat(),
                "mission_id": event.mission_id,
                "capability_id": event.capability_id,
                "scope": event.scope,
                "previous_status": (
                    None
                    if event.previous_status is None
                    else event.previous_status.value
                ),
                "new_status": event.new_status.value,
            }
            for event in events
        ]

        self.repository.save(
            self.mission_id,
            recommendation_records,
            events=event_records,
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

        previous_status = self._statuses.get(record)

        # Repeating the current status is not a lifecycle transition.
        if previous_status is status:
            return

        event = self._create_event(
            record=record,
            previous_status=previous_status,
            new_status=status,
        )

        updated_statuses = dict(self._statuses)
        updated_statuses[record] = status

        updated_events = [
            *self._events,
            event,
        ]

        # Persist before replacing in-memory state so a write failure
        # cannot make memory appear newer than durable storage.
        self._persist(
            updated_statuses,
            updated_events,
        )

        self._statuses = updated_statuses
        self._events = updated_events

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

    def entries(
        self,
        *,
        status: RecommendationStatus | None = None,
        scope: str | None = None,
    ) -> tuple[PlannerHistoryEntry, ...]:
        """
        Return a deterministic, read-only state snapshot.
        """
        matching_entries = [
            PlannerHistoryEntry(
                capability_id=record.capability_id,
                scope=record.scope,
                status=stored_status,
            )
            for record, stored_status in self._statuses.items()
            if (
                status is None
                or stored_status is status
            )
            and (
                scope is None
                or record.scope == scope
            )
        ]

        return tuple(
            sorted(
                matching_entries,
                key=lambda entry: (
                    entry.capability_id,
                    entry.scope or "",
                    entry.status.value,
                ),
            )
        )

    def events(self) -> tuple[PlannerHistoryEvent, ...]:
        """
        Return the immutable lifecycle ledger in event order.
        """
        return tuple(self._events)

    def recover_interrupted(self) -> int:
        """
        Convert unfinished lifecycle states into interrupted events.
        """
        recoverable_statuses = {
            RecommendationStatus.ACCEPTED,
            RecommendationStatus.RUNNING,
        }

        recoverable_records = sorted(
            (
                (record, status)
                for record, status in self._statuses.items()
                if status in recoverable_statuses
            ),
            key=lambda item: (
                item[0].capability_id,
                item[0].scope or "",
            ),
        )

        if not recoverable_records:
            return 0

        updated_statuses = dict(self._statuses)
        updated_events = list(self._events)

        for record, previous_status in recoverable_records:
            updated_statuses[
                record
            ] = RecommendationStatus.INTERRUPTED

            updated_events.append(
                self._create_event(
                    record=record,
                    previous_status=previous_status,
                    new_status=RecommendationStatus.INTERRUPTED,
                )
            )

        # Persist first so memory cannot move ahead of durable state.
        self._persist(
            updated_statuses,
            updated_events,
        )

        self._statuses = updated_statuses
        self._events = updated_events

        return len(recoverable_records)

    def clear(self) -> None:
        if self.mission_id is not None and self.repository is not None:
            self.repository.clear(self.mission_id)

        self._statuses.clear()
        self._events.clear()
