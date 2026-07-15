from core.council.council_assessment import CouncilAssessment
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
    ) -> list[CouncilAssessment]:
        """
        Convene every registered Council member.
        """
        return [
            member.assess(context)
            for member in self.registry.all()
        ]