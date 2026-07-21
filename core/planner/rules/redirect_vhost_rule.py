from core.planner.recommendation import Recommendation
from core.planner.rule import PlannerRule


class RedirectVhostRule(PlannerRule):
    """
    Recommend virtual-host discovery when an HTTP endpoint redirects
    to another hostname and no virtual hosts have been discovered yet.
    """

    name = "Redirect Virtual Host Rule"

    def evaluate(self, context) -> Recommendation | None:
        # Do not recommend work that has already produced results.
        if context.web_vhosts():
            return None

        for surface in context.web_surfaces():
            redirect_location = surface.get("redirect_location")

            if not redirect_location:
                continue

            return Recommendation(
                capability_id="web.recon.virtual-host-discovery",
                reason=(
                    f"HTTP endpoint {surface.get('url', 'Unknown')} redirects "
                    f"to {redirect_location}, which may indicate a canonical "
                    "hostname or additional virtual-host routing."
                ),
                confidence="High",
                required_inputs=(
                    "target",
                    "domain",
                    "wordlist",
                ),
                rule=self.__class__.__name__,
            )

        return None