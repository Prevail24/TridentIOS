"""
═══════════════════════════════════════════════════════

                      MEDUSA

                Chief of Operations
                   Trident IOS

The Observer commands.
Medusa coordinates.
The Council reasons.
The Serpents explore.
The Loom remembers.

═══════════════════════════════════════════════════════
"""

from core.briefings.mission_brief import MissionBrief
from core.council.council import Council
from core.kernel.mission_context import MissionContext
from core.serpents.reporter import Reporter


class Medusa:
    """
    Chief of Operations for Trident IOS.

    Medusa coordinates operational systems.
    She does not perform specialist analysis herself.
    """

    def __init__(
        self,
        council: Council | None = None,
        reporter: Reporter | None = None,
    ) -> None:
        self.council = council or Council()
        self.reporter = reporter or Reporter()

    def brief(
        self,
        context: MissionContext | None = None,
    ) -> MissionBrief:
        """
        Convene the Council and return an operational briefing
        for the active mission.
        """
        mission_context = context or MissionContext()

        session = self.council.deliberate(
            mission_context
        )

        return self.reporter.brief(
            session
        )