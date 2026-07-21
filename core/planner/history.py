from dataclasses import dataclass


@dataclass(frozen=True)
class RecommendationRecord:
    capability_id: str
    scope: str | None


class PlannerHistory:
    """
    Tracks completed recommendations for the lifetime of a planning session.
    """

    def __init__(self):
        self._completed: set[RecommendationRecord] = set()

    def mark_completed(
        self,
        capability_id: str,
        scope: str | None,
    ) -> None:
        self._completed.add(
            RecommendationRecord(
                capability_id,
                scope,
            )
        )

    def has_completed(
        self,
        capability_id: str,
        scope: str | None,
    ) -> bool:
        return RecommendationRecord(
            capability_id,
            scope,
        ) in self._completed

    def clear(self) -> None:
        self._completed.clear()