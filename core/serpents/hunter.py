from core.services.host_profile_service import HostProfileService
from core.events.event import Event
from core.events.event_bus import EventBus, event_bus
from core.services.host_profile_service import HostProfileService

class Hunter:
    """
    Seeker of Opportunity.

    Examines a known host profile and identifies
    promising directions for further investigation.
    """
    CHANGE_RECOMMENDATIONS = {
        "http": [
            "Run HTTP content discovery.",
            "Fingerprint exposed web technologies.",
            "Review HTTP headers and application routes.",
        ],
        "https": [
            "Inspect TLS certificates and supported protocols.",
            "Enumerate virtual hosts and application routes.",
            "Review HTTPS security headers.",
        ],
        "ssh": [
            "Enumerate SSH configuration and authentication methods.",
            "Review host keys and supported algorithms.",
        ],
        "smtp": [
            "Investigate SMTP configuration and authorized enumeration paths.",
            "Review relay behavior and exposed server capabilities.",
        ],
        "dns": [
            "Compare DNS records and investigate newly exposed infrastructure.",
            "Review subdomains, name servers, and record changes.",
        ],
        "service": [
            "Fingerprint the changed service and verify its exposed version.",
            "Compare the service against previous host observations.",
        ],
        "system": [
            "Review the changed system observation and gather corroborating evidence.",
        ],
    }

    def __init__(self, bus: EventBus | None = None) -> None:
        self.bus = bus if bus is not None else event_bus
        self.profiles = HostProfileService()

    def handle(self, event: Event) -> None:
        if event.event_type != "InfrastructureChanged":
            return

        category = event.payload["category"]

        recommendations = self.CHANGE_RECOMMENDATIONS.get(
            category,
            [
                "Investigate the changed infrastructure.",
                "Gather another observation to verify the change.",
            ],
        )

        print(
            f"🎯 Hunter: {len(recommendations)} investigative leads identified."
        )

        self.bus.publish(
            Event(
                event_type="InvestigationRecommended",
                payload={
                    "category": category,
                    "recommendations": recommendations,
                    "reason": f"Sentinel detected a change in '{category}'.",
                    "previous": event.payload["previous"],
                    "current": event.payload["current"],
                    "observation_id": event.payload.get("observation_id"),
                    "mission_id": event.payload.get("mission_id"),
                    "recommended_by": "Hunter",
                },
            )
        )

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