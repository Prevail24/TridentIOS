from core.planner.planner import Planner
from core.planner.recommendation import (
    Recommendation,
    RecommendationPriority,
    RecommendationStatus,
)


class MatchingRule:
    name = "Matching Rule"

    def evaluate(self, context):
        return Recommendation(
            capability_id="web.recon.technology-discovery",
            reason="A matching condition was found.",
            confidence="High",
            rule=self.name,
        )


class NonMatchingRule:
    name = "Non-Matching Rule"

    def evaluate(self, context):
        return None


class FakeRegistry:
    def rules(self):
        return [
            MatchingRule(),
            NonMatchingRule(),
        ]


class FakeMissionContext:
    pass


def test_planner_collects_matching_recommendations():
    planner = Planner()
    planner.registry = FakeRegistry()

    recommendations = planner.plan(FakeMissionContext())

    assert len(recommendations) == 1
    assert (
        recommendations[0].capability_id
        == "web.recon.technology-discovery"
    )
    assert recommendations[0].rule == "Matching Rule"
    assert recommendations[0].executable is True
    assert (
        recommendations[0].priority
        is RecommendationPriority.MEDIUM
    )
    assert (
        recommendations[0].status
        is RecommendationStatus.PENDING
    )

def test_non_pending_recommendation_is_not_executable():
    recommendation = Recommendation(
        capability_id="web.recon.technology-discovery",
        reason="Technology discovery already accepted.",
        status=RecommendationStatus.ACCEPTED,
    )

    assert recommendation.executable is False


def test_planner_returns_empty_list_when_no_rules_match():
    class EmptyRegistry:
        def rules(self):
            return [NonMatchingRule()]

    planner = Planner()
    planner.registry = EmptyRegistry()

    recommendations = planner.plan(FakeMissionContext())

    assert recommendations == []

def test_recommendation_captures_planning_metadata():
    recommendation = Recommendation(
        capability_id="web.recon.virtual-host-discovery",
        reason="A redirect indicates hostname-based routing.",
        priority=RecommendationPriority.HIGH,
        scope="10.10.11.10",
        evidence=(
            "HTTP endpoint redirects to http://paper.htb/",
        ),
        requires=(
            "HTTP Service",
            "Redirect Hostname",
        ),
        produces=(
            "Virtual Host",
            "Hostname",
        ),
    )

    assert recommendation.scope == "10.10.11.10"
    assert recommendation.priority is RecommendationPriority.HIGH
    assert recommendation.evidence == (
        "HTTP endpoint redirects to http://paper.htb/",
    )
    assert recommendation.requires == (
        "HTTP Service",
        "Redirect Hostname",
    )
    assert recommendation.produces == (
        "Virtual Host",
        "Hostname",
    )