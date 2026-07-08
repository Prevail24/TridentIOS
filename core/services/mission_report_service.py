from core.services.host_profile_service import HostProfileService
from core.services.chronicle_service import ChronicleService


class MissionReportService:
    """
    Builds a plain-text mission report for a host.
    """

    def __init__(self):
        self.profiles = HostProfileService()
        self.chronicles = ChronicleService()

    def build(self, host: str):
        profile = self.profiles.build(host)
        chronicle = self.chronicles.build(host)

        if profile is None:
            return None

        lines = []

        lines.append("═══════════════════════════════")
        lines.append("        MISSION REPORT")
        lines.append("═══════════════════════════════")
        lines.append("")
        lines.append(f"Target: {profile['host']}")
        lines.append("")
        lines.append("SUMMARY")
        lines.append("-------")
        lines.append(f"Open Ports   : {len(profile['ports'])}")
        lines.append(f"Services     : {len(profile['services'])}")
        lines.append(f"Products     : {len(profile['products'])}")
        lines.append(f"Versions     : {len(profile['versions'])}")
        lines.append(f"Observations : {profile['observation_count']}")
        lines.append("")
        lines.append("HISTORY")
        lines.append("-------")
        lines.append(f"First Seen : {profile['first_seen']}")
        lines.append(f"Last Seen  : {profile['last_seen']}")
        lines.append("")
        lines.append("SERVICES")
        lines.append("--------")

        for service in sorted(profile["services"]):
            lines.append(f"• {service}")

        lines.append("")
        lines.append("PRODUCTS")
        lines.append("--------")

        for product in sorted(profile["products"]):
            lines.append(f"• {product}")

        lines.append("")
        lines.append("MISSION CHRONICLE")
        lines.append("-----------------")

        for entry in chronicle:
            lines.append("")
            lines.append(str(entry["timestamp"]))
            lines.append(f"Observations: {entry['count']}")

            if entry["services"]:
                lines.append("Services:")
                for service in entry["services"]:
                    lines.append(f"  • {service}")

            if entry["products"]:
                lines.append("Products:")
                for product in entry["products"]:
                    lines.append(f"  • {product}")

            if entry["versions"]:
                lines.append("Versions:")
                for version in entry["versions"]:
                    lines.append(f"  • {version}")

        return "\n".join(lines)