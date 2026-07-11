from core.services.host_profile_service import HostProfileService


class Hunter:
    """
    Seeker of Opportunity.

    Examines a known host profile and identifies
    promising directions for further investigation.
    """

    def __init__(self):
        self.profiles = HostProfileService()

    def hunt(self, host: str) -> list[str]:
        profile = self.profiles.build(host)

        if profile is None:
            return []

        ports = set(profile.get("ports", []))
        services = set(profile.get("services", []))
        products = set(profile.get("products", []))

        leads = []

        if "tcp/22" in ports or "ssh" in services:
            leads.append("Enumerate SSH configuration and authentication methods.")

        if "tcp/80" in ports or "http" in services:
            leads.append("Investigate the HTTP application surface.")

        if "tcp/443" in ports or "https" in services:
            leads.append("Inspect HTTPS certificates, virtual hosts, and application routes.")

        if "tcp/25" in ports or "smtp" in services:
            leads.append("Investigate SMTP configuration and authorized enumeration paths.")

        if any("Apache" in product for product in products):
            leads.append("Fingerprint Apache modules and exposed application paths.")

        if any("OpenSSH" in product for product in products):
            leads.append("Review the detected OpenSSH version and supported authentication methods.")

        return leads