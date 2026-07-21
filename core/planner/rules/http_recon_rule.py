from core.planner.rule import PlannerRule
from core.planner.recommendation import Recommendation


class HTTPReconRule(PlannerRule):
    """
    Recommend HTTP reconnaissance when an HTTP service
    has been discovered but no endpoint observations exist.
    """

    def evaluate(self, context):

        if not context.has_service("http"):
            return None

        if context.has_web_surface():
            return None

        return Recommendation(
            capability_id="web.recon.technology-discovery",
            reason=(
                "HTTP service detected but HTTP reconnaissance "
                "has not yet been performed."
            ),
            confidence="High",
            rule=self.__class__.__name__,
)