from core.services.host_profile_service import HostProfileService


class Hunter:
    """
    Seeker of Opportunity.

    Examines known intelligence and suggests
    the next investigative targets.
    """

    def __init__(self):
        self.profiles = HostProfileService()

    def hunt(self, host: str) -> list[str]:

        profile = self.profiles.build(host)

        if profile is None:
            return []

        recommendations = []

        #
        # HTTPS available?
        #
        if "tcp/443" in profile["ports"]:
            recommendations.append(
                "Investigate HTTPS attack surface."
            )

        #
        # SSH exposed?
        #
        if "ssh" in profile["services"]:
            recommendations.append(
                "Enumerate SSH configuration."
            )

        #
        # Apache detected?
        #
        if any(
            "Apache" in product
            for product in profile["products"]
        ):
            recommendations.append(
                "Fingerprint Apache modules."
            )

        return recommendations