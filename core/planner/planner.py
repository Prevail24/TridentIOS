from core.planner.registry import PlannerRegistry


class Planner:

    def __init__(self):
        self.registry = PlannerRegistry()

    def plan(self, context):

        recommendations = []

        for rule in self.registry.rules():

            recommendation = rule.evaluate(context)

            if recommendation is not None:
                recommendations.append(recommendation)

        return recommendations

        