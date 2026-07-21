from core.planner.rules.http_recon_rule import HTTPReconRule
from core.planner.rules.redirect_vhost_rule import RedirectVhostRule


class PlannerRegistry:
    """
    Provides the deterministic rules evaluated by the Planner.
    """

    def rules(self):
        return [
            HTTPReconRule(),
            RedirectVhostRule(),
        ]