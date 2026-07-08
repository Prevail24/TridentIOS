from dataclasses import dataclass

from core.services.observation_service import ObservationService


@dataclass
class WeaverReport:
    health: str
    empty_observations: int
    orphaned_observations: int
    duplicate_evidence: int


class WeaverBrief:
    """
    Performs health checks on The Loom.

    The Weaver does not modify knowledge.
    It only evaluates it.
    """

    def __init__(self):
        self.observations = ObservationService()

    def generate(self) -> WeaverReport:

        observations = self.observations.list()

        empty = 0
        orphaned = 0

        for observation in observations:

            if len(observation.evidence) == 0:
                empty += 1

            if not observation.mission_id:
                orphaned += 1

        health = "GOOD"

        if empty >= 3:
            health = "WARNING"

        if empty >= 5:
            health = "CRITICAL"

        return WeaverReport(
            health=health,
            empty_observations=empty,
            orphaned_observations=orphaned,
            duplicate_evidence=0,
        )