from dataclasses import dataclass, field

from core.models.observation import Observation


@dataclass
class CreateObservationResult:
    """
    Represents the outcome of creating a new Observation.
    """

    observation: Observation
    filepath: str

    success: bool = True
    warnings: list[str] = field(default_factory=list)