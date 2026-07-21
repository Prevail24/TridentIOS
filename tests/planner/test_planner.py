from core.planner.planner import Planner
from core.planner.recommendation import Recommendation


class MatchingRule:
    name = "Matching Rule"

    def evaluate(self, context):
        return Recommendation(
            capability="Technology Discovery",
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
    assert recommendations[0].capability == "Technology Discovery"
    assert recommendations[0].rule == "Matching Rule"


def test_planner_returns_empty_list_when_no_rules_match():
    class EmptyRegistry:
        def rules(self):
            return [NonMatchingRule()]

    planner = Planner()
    planner.registry = EmptyRegistry()

    recommendations = planner.plan(FakeMissionContext())

    assert recommendations == []