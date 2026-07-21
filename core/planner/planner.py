from core.planner.registry import PlannerRegistry
from core.planner.ranking import rank


class Planner:

    def __init__(self):
        self.registry = PlannerRegistry()

    def plan(self, context):

        recommendations = []

        for rule in self.registry.rules():

            recommendation = rule.evaluate(context)

            if recommendation is not None:
                recommendations.append(recommendation)

        return rank(recommendations)