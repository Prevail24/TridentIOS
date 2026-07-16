from core.council.council_assessment import CouncilAssessment
from core.council.council_member import CouncilMember
from core.kernel.mission_context import MissionContext


class Skeptic(CouncilMember):
    """
    Keeper of Verification.

    Evaluates the completeness and evidentiary quality
    of the active investigation.
    """

    name = "Skeptic"

    def assess(
        self,
        context: MissionContext,
    ) -> CouncilAssessment:
        runs = context.runs()
        ports = context.open_ports()
        web_surfaces = context.web_surfaces()
        observations = context.mission_observations()

        findings = [
            f"{len(runs)} tool runs completed.",
            f"{len(observations)} mission observations recorded.",
            f"{len(ports)} open ports identified.",
        ]

        recommendations = []
        warnings = []

        confidence = 1.0

        if not observations:
            confidence -= 0.5
            warnings.append(
                "No canonical observations are available."
            )

        if len(runs) < 2:
            confidence -= 0.2
            warnings.append(
                "Only one reconnaissance source has been executed."
            )
            recommendations.append(
                "Gather corroborating evidence from an additional sensor."
            )

        if not ports:
            confidence -= 0.2
            warnings.append(
                "No open ports have been confirmed."
            )

        http_ports = {
            item["port"]
            for item in ports
            if str(item.get("service", "")).lower()
            in {"http", "https"}
            or item["port"] in {80, 443, 8000, 8080, 8443}
        }

        if http_ports and not web_surfaces:
            confidence -= 0.2
            warnings.append(
                "HTTP-capable services were detected without "
                "corroborating HTTP endpoint observations."
            )
            recommendations.append(
                "Run HTTP reconnaissance against the discovered web surface."
            )

        if web_surfaces:
            findings.append(
                f"{len(web_surfaces)} HTTP surface observations recorded."
            )

            if len(web_surfaces) == 1:
                confidence -= 0.1
                warnings.append(
                    "Only one HTTP endpoint observation is available."
                )
                recommendations.append(
                    "Gather additional web reconnaissance before "
                    "raising confidence."
                )

        confidence = max(
            0.0,
            min(1.0, confidence),
        )

        if confidence >= 0.8:
            quality = "strong"
        elif confidence >= 0.5:
            quality = "moderate"
        else:
            quality = "limited"

        return CouncilAssessment(
            member=self.name,
            summary=(
                f"Mission evidence quality is {quality}."
            ),
            confidence=confidence,
            findings=findings,
            recommendations=recommendations,
            warnings=warnings,
        )