from abc import ABC, abstractmethod

from core.planner.recommendation import Recommendation


class PlannerRule(ABC):
    """
    Base class for every deterministic planner rule.
    """

    name = "Unnamed Rule"

    @abstractmethod
    def evaluate(self, context) -> Recommendation | None:
        """
        Return a Recommendation if this rule matches,
        otherwise return None.
        """
        raise NotImplementedError