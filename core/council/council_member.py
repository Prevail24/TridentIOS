from abc import ABC, abstractmethod

from core.council.council_assessment import CouncilAssessment
from core.kernel.mission_context import MissionContext


class CouncilMember(ABC):
    """
    Base contract implemented by every Council specialist.
    """

    name: str

    @abstractmethod
    def assess(
        self,
        context: MissionContext,
    ) -> CouncilAssessment:
        """
        Produce an assessment from the current mission.
        """
        ...