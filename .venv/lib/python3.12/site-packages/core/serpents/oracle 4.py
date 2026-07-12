from core.services.host_profile_service import HostProfileService


class Oracle:
    """
    Keeper of Hypotheses.
    """

    def __init__(self):
        self.profiles = HostProfileService()

    def hypothesize(self, host: str):

        profile = self.profiles.build(host)

        if profile is None:
            return []

        hypotheses = []

        products = profile["products"]
        services = profile["services"]

        if any("Apache" in p for p in products):

            hypotheses.append({
                "confidence": "high",
                "hypothesis":
                    "Host is likely serving a traditional web application."
            })

        if "ssh" in services:

            hypotheses.append({
                "confidence": "medium",
                "hypothesis":
                    "Host likely supports remote administrative access."
            })

        if "smtp" in services:

            hypotheses.append({
                "confidence": "medium",
                "hypothesis":
                    "Host may function as a mail relay or mail server."
            })

        return hypotheses