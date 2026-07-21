from core.observations.observation import Observation
from core.observations.types import ObservationType


class ObservationStore:
    """
    In-memory collection of observations discovered during a mission.

    Exact duplicate observations are stored only once.
    Discovery order is preserved.
    """

    def __init__(self) -> None:
        self._observations: list[Observation] = []
        self._seen: set[Observation] = set()

    def add(self, observation: Observation) -> bool:
        """
        Add an observation to the store.

        Returns True when the observation was added.
        Returns False when an exact duplicate already exists.
        """

        if observation in self._seen:
            return False

        self._observations.append(observation)
        self._seen.add(observation)

        return True

    def all(self) -> tuple[Observation, ...]:
        """
        Return all observations in discovery order.
        """

        return tuple(self._observations)

    def find_by_type(
        self,
        observation_type: ObservationType,
    ) -> tuple[Observation, ...]:
        """
        Return observations matching the requested type.
        """

        return tuple(
            observation
            for observation in self._observations
            if observation.type is observation_type
        )

    def find_by_scope(
        self,
        scope: str | None,
    ) -> tuple[Observation, ...]:
        """
        Return observations matching the requested scope.
        """

        return tuple(
            observation
            for observation in self._observations
            if observation.scope == scope
        )

    def contains(self, observation: Observation) -> bool:
        return observation in self._seen

    def clear(self) -> None:
        self._observations.clear()
        self._seen.clear()

    def __len__(self) -> int:
        return len(self._observations)