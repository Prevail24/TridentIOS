from dataclasses import replace

from core.planner.history import PlannerHistory
from core.planner.ranking import rank
from core.planner.recommendation import RecommendationStatus
from core.planner.registry import PlannerRegistry


class Planner:

    def __init__(
        self,
        history: PlannerHistory | None = None,
    ):
        self.registry = PlannerRegistry()
        self.history = (
            history
            if history is not None
            else PlannerHistory()
        )

    def plan(self, context):
        recommendations = []

        for rule in self.registry.rules():
            recommendation = rule.evaluate(context)

            if recommendation is None:
                continue

            stored_status = self.history.status_for(
                recommendation.capability_id,
                recommendation.scope,
            )

            # Completed work should not be recommended again for the
            # same capability and scope.
            if stored_status is RecommendationStatus.COMPLETED:
                continue

            # Failed work becomes eligible for another operator-approved
            # attempt. Other stored lifecycle states remain visible.
            if (
                stored_status is not None
                and stored_status is not RecommendationStatus.FAILED
            ):
                recommendation = replace(
                    recommendation,
                    status=stored_status,
                )

            recommendations.append(recommendation)

        return rank(recommendations)