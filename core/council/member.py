from abc import ABC, abstractmethod

from core.council.assessment import CouncilAssessment
from core.kernel.mission_context import MissionContext


class CouncilMember(ABC):
    """
    Base interface implemented by every Council member.
    """

    name: str

    @abstractmethod
    def assess(
        self,
        mission: MissionContext,
    ) -> CouncilAssessment:
        ...