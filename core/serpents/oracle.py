from core.council.council_assessment import CouncilAssessment
from core.council.council_member import CouncilMember
from core.kernel.mission_context import MissionContext
from core.services.host_profile_service import HostProfileService


class Oracle(CouncilMember):
    """
    Keeper of Hypotheses.

    Forms evidence-grounded interpretations from current mission
    intelligence.

    Oracle never creates facts. She interprets facts already
    present in Mission Context.
    """

    name = "Oracle"

    def __init__(self):
        self.profiles = HostProfileService()

    def hypothesize(self, host: str) -> list[dict]:
        """
        Preserve the original historical host-profile interface.

        This method may include accumulated cross-mission knowledge.
        Current Council deliberation should use assess().
        """
        profile = self.profiles.build(host)

        if profile is None:
            return []

        hypotheses = []

        products = {
            str(product).lower()
            for product in profile.get("products", [])
        }

        services = {
            str(service).lower()
            for service in profile.get("services", [])
        }

        if any("apache" in product for product in products):
            hypotheses.append(
                {
                    "confidence": "high",
                    "hypothesis": (
                        "Host is likely serving a traditional "
                        "web application."
                    ),
                }
            )

        if "ssh" in services:
            hypotheses.append(
                {
                    "confidence": "medium",
                    "hypothesis": (
                        "Host likely supports remote "
                        "administrative access."
                    ),
                }
            )

        if "smtp" in services:
            hypotheses.append(
                {
                    "confidence": "medium",
                    "hypothesis": (
                        "Host may function as a mail relay "
                        "or mail server."
                    ),
                }
            )

        return hypotheses

    def assess(
        self,
        context: MissionContext,
    ) -> CouncilAssessment:
        """
        Produce deterministic hypotheses from active-mission
        intelligence.
        """
        ports = context.open_ports()
        web_surfaces = context.web_surfaces()

        if not ports:
            return CouncilAssessment(
                member=self.name,
                summary="Insufficient mission intelligence for analysis.",
                confidence=0.0,
                warnings=[
                    "Oracle cannot form a grounded hypothesis "
                    "without confirmed network services."
                ],
            )

        services = {
            str(item.get("service", "")).lower()
            for item in ports
            if item.get("service")
        }

        products = {
            str(item.get("product", "")).lower()
            for item in ports
            if item.get("product")
        }

        findings = []
        recommendations = []
        warnings = []
        confidence = 0.5

        has_ssh = (
            "ssh" in services
            or any("openssh" in product for product in products)
        )

        has_http = (
            bool(web_surfaces)
            or "http" in services
            or "https" in services
        )

        has_nginx = any(
            "nginx" in product
            for product in products
        )

        has_apache = any(
            "apache" in product
            for product in products
        )

        if has_ssh:
            findings.append(
                "The target likely supports remote "
                "administrative access."
            )
            confidence += 0.1

        if has_http:
            findings.append(
                "The target exposes a reachable web application surface."
            )
            recommendations.append(
                "Prioritize targeted web application enumeration."
            )
            confidence += 0.15

        if has_nginx:
            findings.append(
                "The web surface appears to be served or proxied by nginx."
            )
            confidence += 0.1

        if has_apache:
            findings.append(
                "The web surface appears to include Apache infrastructure."
            )
            confidence += 0.1

        if has_ssh and has_http:
            findings.append(
                "The coexistence of SSH and HTTP is consistent "
                "with a remotely administered Linux web server."
            )
            confidence += 0.1

        if web_surfaces:
            redirect_count = sum(
                1
                for surface in web_surfaces
                if surface.get("status_code")
                in {301, 302, 303, 307, 308}
            )

            if redirect_count:
                findings.append(
                    f"{redirect_count} observed HTTP surface"
                    f"{'s' if redirect_count != 1 else ''} "
                    "returned a redirect."
                )
                recommendations.append(
                    "Follow redirects and identify their destination "
                    "before drawing conclusions about the application."
                )
                confidence += 0.05

        if not web_surfaces and has_http:
            warnings.append(
                "A web-capable service exists, but no HTTP endpoint "
                "observation is available."
            )
            recommendations.append(
                "Collect HTTP endpoint evidence before increasing confidence."
            )
            confidence -= 0.2

        confidence = max(
            0.0,
            min(1.0, confidence),
        )

        if has_http and has_ssh:
            summary = (
                "The target most likely represents a remotely "
                "administered web server."
            )
        elif has_http:
            summary = (
                "The target most likely exposes a web-focused "
                "application surface."
            )
        elif has_ssh:
            summary = (
                "The target most likely supports remote "
                "system administration."
            )
        else:
            summary = (
                "The current service profile does not yet support "
                "a strong operational hypothesis."
            )

        return CouncilAssessment(
            member=self.name,
            summary=summary,
            confidence=confidence,
            findings=findings,
            recommendations=recommendations,
            warnings=warnings,
        )