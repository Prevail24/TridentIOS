from dataclasses import dataclass, field
from typing import Any


@dataclass
class Entity:
    """
    Canonical representation of an object discovered during a mission.
    """

    entity_type: str
    value: str

    observations: list[Any] = field(default_factory=list)

    def add_observation(self, observation):
        self.observations.append(observation)

    @property
    def observation_count(self):
        return len(self.observations)