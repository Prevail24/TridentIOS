from dataclasses import dataclass, field

from core.council.council_assessment import CouncilAssessment
from core.kernel.mission_context import MissionContext


@dataclass
class CouncilSession:
    """
    Represents one complete Council deliberation.

    The session contains the operational context
    and every assessment produced during the meeting.
    """

    context: MissionContext

    assessments: list[CouncilAssessment] = field(
        default_factory=list
    )

    def add(
        self,
        assessment: CouncilAssessment,
    ) -> None:
        """
        Record an assessment produced by a Council member.
        """
        self.assessments.append(assessment)