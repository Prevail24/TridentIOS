from core.services.host_profile_service import HostProfileService
from core.events.event import Event
from core.events.event_bus import EventBus, event_bus
from core.council.council_assessment import CouncilAssessment
from core.council.council_member import CouncilMember
from core.kernel.mission_context import MissionContext



class Hunter(CouncilMember):
    """
    Seeker of Opportunity.

    Examines a known host profile and identifies
    promising directions for further investigation.
    """

    name = "Hunter"

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
        self.context = MissionContext()

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
            """
            Generate leads from current-mission intelligence.

            Historical host knowledge remains available through
            HostProfileService, but active recommendations must be
            grounded in the active mission.
            """
            try:
                ports = self.context.open_ports()
            except RuntimeError:
                return []

            host_ports = [
                item
                for item in ports
                if item.get("host") == host
            ]

            services = {
                str(item.get("service", "")).lower()
                for item in host_ports
            }

            products = {
                str(item.get("product", "")).lower()
                for item in host_ports
                if item.get("product")
            }

            port_numbers = {
                item.get("port")
                for item in host_ports
            }

            leads = []

            if 22 in port_numbers or "ssh" in services:
                leads.append(
                    "Enumerate SSH configuration and authentication methods."
                )

            if 80 in port_numbers or "http" in services:
                leads.append(
                    "Investigate the HTTP application surface."
                )

            if 443 in port_numbers or "https" in services:
                leads.append(
                    "Inspect HTTPS certificates, virtual hosts, and application routes."
                )

            if 25 in port_numbers or "smtp" in services:
                leads.append(
                    "Investigate SMTP configuration and authorized enumeration paths."
                )

            if any("nginx" in product for product in products):
                leads.append(
                    "Fingerprint nginx configuration and exposed application paths."
                )

            if any("apache" in product for product in products):
                leads.append(
                    "Fingerprint Apache modules, virtual hosts, and exposed application paths."
                )

            if any("iis" in product for product in products):
                leads.append(
                    "Enumerate IIS modules, virtual directories, and installed applications."
                )

            if any("openssh" in product for product in products):
                leads.append(
                    "Review the detected OpenSSH version and supported authentication methods."
                )

            return leads
    
    def assess(
        self,
        context: MissionContext,
    ) -> CouncilAssessment:
        """
        Produce Hunter's current-mission assessment.

        The existing hunt() interface remains available for
        compatibility with strike orchestration.
        """
        ports = context.open_ports()

        hosts = sorted(
            {
                str(item.get("host"))
                for item in ports
                if item.get("host")
            }
        )

        if not hosts:
            return CouncilAssessment(
                member=self.name,
                summary="No active host intelligence is available.",
                confidence=0.0,
                warnings=[
                    "Hunter cannot recommend an investigative path "
                    "without a discovered host."
                ],
            )

        recommendations = []

        for host in hosts:
            for lead in self.hunt(host):
                if lead not in recommendations:
                    recommendations.append(lead)

        if not recommendations:
            return CouncilAssessment(
                member=self.name,
                summary="No investigative opportunities identified.",
                confidence=0.5,
                findings=[
                    f"{len(hosts)} host or hosts reviewed."
                ],
            )

        return CouncilAssessment(
            member=self.name,
            summary=(
                f"{len(recommendations)} investigative "
                "opportunities identified."
            ),
            confidence=1.0,
            findings=[
                f"{len(hosts)} active mission host or hosts reviewed."
            ],
            recommendations=recommendations,
        )