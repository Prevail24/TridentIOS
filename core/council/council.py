from core.council.council_assessment import CouncilAssessment
from core.council.council_session import CouncilSession
from core.council.registry import CouncilRegistry
from core.kernel.mission_context import MissionContext


class Council:
    """
    Convenes the Intelligence Council.

    The Council performs no specialist analysis itself.
    It gathers assessments from every registered member
    and returns them to Medusa.
    """

    def __init__(
        self,
        registry: CouncilRegistry | None = None,
    ) -> None:
        self.registry = registry or CouncilRegistry()

    def deliberate(
        self,
        context: MissionContext,
    ) -> CouncilSession:
        """
        Convene every registered Council member.
        """
        session = CouncilSession(context)

        for member in self.registry.all():
            session.add(
                member.assess(context)
            )

        return session