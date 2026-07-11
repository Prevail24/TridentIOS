from core.models.mission import Mission
from core.repositories.mission_repository import MissionRepository
from core.repositories.observation_repository import ObservationRepository


class Archivist:
    """
    Keeper of Memory.

    Retrieves canonical observations belonging to a Mission.
    """

    def __init__(self):
        self.missions = MissionRepository()
        self.observations = ObservationRepository()

    def retrieve(self, mission: Mission | str) -> list:
        """
        Return the canonical observations attached to a mission.

        Accepts either a Mission object or a mission ID.
        """
        if isinstance(mission, str):
            mission = self.missions.open(mission)

        retrieved = []

        for observation_id in mission.observations:
            retrieved.append(
                self.observations.open(observation_id)
            )

        return retrieved