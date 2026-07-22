from core.planner.recommendation import (
    Recommendation,
    RecommendationPriority,
)

_PRIORITY_ORDER = {
    RecommendationPriority.CRITICAL: 0,
    RecommendationPriority.HIGH: 1,
    RecommendationPriority.MEDIUM: 2,
    RecommendationPriority.LOW: 3,
}

_CONFIDENCE_ORDER = {
    "High": 0,
    "Medium": 1,
    "Low": 2,
}


def rank(
    recommendations: list[Recommendation],
) -> list[Recommendation]:
    """
    Return recommendations ordered from highest value to lowest.

    Ordering:
        1. Priority
        2. Confidence
        3. Capability ID (deterministic tie-breaker)
    """

    return sorted(
        recommendations,
        key=lambda recommendation: (
            _PRIORITY_ORDER[recommendation.priority],
            _CONFIDENCE_ORDER.get(
                recommendation.confidence,
                99,
            ),
            recommendation.capability_id,
        ),
    )