import pytest

from core.command.capability_router import (
    CapabilityExecutionError,
    CapabilityRouter,
)
from core.planner.recommendation import (
    Recommendation,
    RecommendationStatus,
)


class FakeWeapon:
    def __init__(self):
        self.contexts = []

    def execute(self, context):
        self.contexts.append(context)
        return {"executed": True}


class FakeCapability:
    id = "web.recon.technology-discovery"

    def __init__(self, weapon):
        self._weapon = weapon

    def weapons(self):
        return [self._weapon]


class FakeSerpent:
    def __init__(self, capability):
        self._capability = capability

    def capabilities(self):
        return [self._capability]


def build_router():
    weapon = FakeWeapon()
    capability = FakeCapability(weapon)
    serpent = FakeSerpent(capability)

    return CapabilityRouter([serpent]), weapon


def test_executes_ready_recommendation():
    router, weapon = build_router()
    context = object()

    recommendation = Recommendation(
        capability_id="web.recon.technology-discovery",
        reason="HTTP service requires technology discovery.",
    )

    results = router.execute_recommendation(
        recommendation,
        context,
    )

    assert results == [{"executed": True}]
    assert weapon.contexts == [context]


def test_rejects_non_pending_recommendation():
    router, weapon = build_router()

    recommendation = Recommendation(
        capability_id="web.recon.technology-discovery",
        reason="Recommendation was already accepted.",
        status=RecommendationStatus.ACCEPTED,
    )

    with pytest.raises(
        CapabilityExecutionError,
        match="not executable",
    ):
        router.execute_recommendation(
            recommendation,
            object(),
        )

    assert weapon.contexts == []
