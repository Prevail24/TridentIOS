from core.planner.rule import PlannerRule
from core.planner.recommendation import Recommendation


class HTTPServiceRule(PlannerRule):

    name = "HTTP Service Discovery"

    def evaluate(self, context):

        if not context.web_surfaces():
            return None

        return Recommendation(
            capability_id="web.recon.technology-discovery",
            reason="HTTP services were discovered during reconnaissance.",
            confidence="High",
            rule=self.name,
        )