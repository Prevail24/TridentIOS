from core.council.council import Council
from core.council.council_assessment import CouncilAssessment
from core.kernel.mission_context import MissionContext


class FakeCouncilMember:
    def __init__(
        self,
        assessment: CouncilAssessment,
    ) -> None:
        self.assessment = assessment
        self.received_context = None

    def assess(
        self,
        context: MissionContext,
    ) -> CouncilAssessment:
        self.received_context = context
        return self.assessment


class FakeCouncilRegistry:
    def __init__(
        self,
        members: list[FakeCouncilMember],
    ) -> None:
        self.members = members

    def all(self) -> list[FakeCouncilMember]:
        return self.members


def test_council_deliberates():
    context = MissionContext()

    hunter_assessment = CouncilAssessment(
        member="Hunter",
        summary="HTTP exposure requires investigation.",
        confidence=0.9,
        recommendations=["Investigate HTTP"],
    )

    oracle_assessment = CouncilAssessment(
        member="Oracle",
        summary="The target may expose a web application.",
        confidence=0.8,
        findings=[
            "A web application may be present.",
        ],
    )

    hunter = FakeCouncilMember(hunter_assessment)
    oracle = FakeCouncilMember(oracle_assessment)

    registry = FakeCouncilRegistry(
        [hunter, oracle]
    )

    council = Council(registry=registry)

    session = council.deliberate(context)

    assert session.context is context
    assert session.assessments == [
        hunter_assessment,
        oracle_assessment,
    ]

    assert hunter.received_context is context
    assert oracle.received_context is context