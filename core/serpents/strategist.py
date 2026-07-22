


"""
LEGACY / DISCONNECTED — DO NOT EXPAND
"""





















from core.serpents.skeptic import Skeptic


class Strategist:
    """
    Keeper of Plans.
    """

    def __init__(self):
        self.skeptic = Skeptic()

    def plan(self, host: str) -> list[str]:

        verified = self.skeptic.verify(host)

        plan = []

        for result in verified:

            if result["status"] != "verified":
                continue

            hypothesis = result["hypothesis"]

            if "web application" in hypothesis.lower():
                plan.append(
                    "Perform authenticated and unauthenticated web application reconnaissance."
                )

            elif "administrative access" in hypothesis.lower():
                plan.append(
                    "Review remote administration attack surface."
                )

            elif "mail" in hypothesis.lower():
                plan.append(
                    "Validate mail infrastructure configuration."
                )

        return plan