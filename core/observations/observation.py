from dataclasses import dataclass

from core.observations.types import ObservationType


@dataclass(frozen=True)
class Observation:
    """
    A fact discovered during a mission.

    Observations are immutable value objects. Two observations with the
    same fields represent the same discovered fact.
    """

    type: ObservationType
    value: str
    source: str
    scope: str | None = None