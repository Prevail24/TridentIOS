from core.council.council_assessment import CouncilAssessment
from core.council.council_member import CouncilMember
from core.kernel.mission_context import MissionContext
from core.services.chronicle_service import ChronicleService
from core.services.history_service import HistoryService


class Historian(CouncilMember):
    """
    Keeper of Time.

    Reconstructs investigations from canonical history
    and provides historical context to the Council.
    """

    name = "Historian"

    def __init__(self):
        self.chronicle = ChronicleService()
        self.history = HistoryService()

    def reconstruct(self, host: str):
        """
        Preserve the existing Chronicle interface.
        """
        return self.chronicle.build(host)

    def assess(
        self,
        context: MissionContext,
    ) -> CouncilAssessment:
        """
        Produce historical context for hosts in the active mission.
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
                summary="No active host history is available.",
                confidence=0.0,
                warnings=[
                    "Historian cannot reconstruct history "
                    "without an active mission host."
                ],
            )

        findings = []
        warnings = []
        historical_hosts = 0

        for host in hosts:
            history = self.history.build(host)

            if history is None:
                warnings.append(
                    f"No historical observations found for {host}."
                )
                continue

            historical_hosts += 1

            first_seen = history.get("first_seen")
            last_seen = history.get("last_seen")
            observation_count = history.get(
                "observation_count",
                0,
            )

            findings.append(
                f"{host} has {observation_count} historical observations."
            )

            if first_seen:
                findings.append(
                    f"{host} was first seen at {first_seen}."
                )

            if last_seen:
                findings.append(
                    f"{host} was last seen at {last_seen}."
                )

        if historical_hosts == 0:
            return CouncilAssessment(
                member=self.name,
                summary="No historical context identified.",
                confidence=0.25,
                findings=findings,
                warnings=warnings,
            )

        return CouncilAssessment(
            member=self.name,
            summary=(
                f"Historical context identified for "
                f"{historical_hosts} active mission host"
                f"{'s' if historical_hosts != 1 else ''}."
            ),
            confidence=1.0,
            findings=findings,
            warnings=warnings,
        )