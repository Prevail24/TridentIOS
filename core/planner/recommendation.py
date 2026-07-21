from dataclasses import dataclass


@dataclass(frozen=True)
class Recommendation:
    """
    A deterministic recommendation produced by the Planner.
    """

    capability_id: str
    reason: str
    confidence: str = "Medium"
    available: bool = True
    rule: str | None = None
    required_inputs: tuple[str, ...] = ()

    @property
    def executable(self) -> bool:
        """
        Return True when the recommendation is available
        and requires no additional operator input.
        """
        return self.available and not self.required_inputs