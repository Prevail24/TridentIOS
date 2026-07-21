from core.planner.ranking import rank
from core.planner.recommendation import (
    Recommendation,
    RecommendationPriority,
)


def test_empty_list():
    assert rank([]) == []


def test_single_item():
    recommendation = Recommendation(
        capability_id="one",
        reason="Only recommendation.",
    )

    assert rank([recommendation]) == [recommendation]


def test_priority_order():
    low = Recommendation(
        capability_id="low",
        reason="Low priority.",
        priority=RecommendationPriority.LOW,
    )

    high = Recommendation(
        capability_id="high",
        reason="High priority.",
        priority=RecommendationPriority.HIGH,
    )

    ordered = rank([low, high])

    assert ordered == [high, low]


def test_confidence_order():
    medium = Recommendation(
        capability_id="medium",
        reason="Medium confidence.",
        confidence="Medium",
    )

    high = Recommendation(
        capability_id="high",
        reason="High confidence.",
        confidence="High",
    )

    ordered = rank([medium, high])

    assert ordered == [high, medium]


def test_capability_id_breaks_ties():
    bravo = Recommendation(
        capability_id="bravo",
        reason="Tie.",
    )

    alpha = Recommendation(
        capability_id="alpha",
        reason="Tie.",
    )

    ordered = rank([bravo, alpha])

    assert ordered[0].capability_id == "alpha"