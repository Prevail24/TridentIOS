from urllib.parse import urlparse

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

            # Prefer the original probe target when HTTPX used a Host
            # header. Otherwise, use the observed endpoint URL.
            target = (
                surface.get("probe_url")
                or surface.get("url")
            )

            domain = urlparse(
                redirect_location
            ).hostname

            inputs = []
            required_inputs = []

            if target:
                inputs.append(("target", target))
            else:
                required_inputs.append("target")

            if domain:
                inputs.append(("domain", domain))
            else:
                required_inputs.append("domain")

            # The Planner cannot safely choose an operator's wordlist.
            required_inputs.append("wordlist")

            return Recommendation(
                capability_id="web.recon.virtual-host-discovery",
                reason=(
                    f"HTTP endpoint {target or 'Unknown'} redirects "
                    f"to {redirect_location}, which may indicate a "
                    "canonical hostname or additional virtual-host "
                    "routing."
                ),
                confidence="High",
                inputs=tuple(inputs),
                required_inputs=tuple(required_inputs),
                rule=self.__class__.__name__,
            )

        return None