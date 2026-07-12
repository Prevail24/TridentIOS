from dataclasses import dataclass
from datetime import date
from pathlib import Path

from core.models.mission import Mission
from core.repositories.mission_repository import MissionRepository


@dataclass
class CreateMissionResult:
    mission: Mission
    filepath: str
    success: bool = True


class MissionService:
    """
    Mission business logic.

    Service owns mission creation and state transitions.
    Repository owns persistence.
    """

    def __init__(self, repository: MissionRepository | None = None) -> None:
        self.repository = repository or MissionRepository()

    def create(
        self,
        title: str,
        mission_type: str,
        objective: str,
        scope: str,
        operator: str = "Prevail",
        priority: str = "normal",
    ) -> CreateMissionResult:
        mission_id = self._generate_id()

        mission = Mission(
            id=mission_id,
            title=title,
            mission_type=mission_type,
            objective=objective,
            scope=scope,
            operator=operator,
            priority=priority,
            created=date.today(),
            updated=date.today(),
        )

        filepath = self.repository.save(mission)

        return CreateMissionResult(
            mission=mission,
            filepath=str(filepath),
        )

    def open(self, mission_id: str) -> Mission:
        return self.repository.open(mission_id)

    def list(self) -> list[Mission]:
        return self.repository.list()

    def save(self, mission: Mission) -> Path:
        return self.repository.save(mission)

    def complete(self, mission_id: str) -> Mission:
        mission = self.open(mission_id)
        mission.complete()
        self.save(mission)
        return mission

    def archive(self, mission_id: str) -> Mission:
        mission = self.open(mission_id)
        mission.archive()
        self.save(mission)
        return mission

    def add_observation(self, mission_id: str, observation_id: str) -> Mission:
        mission = self.open(mission_id)
        mission.add_observation(observation_id)
        self.save(mission)
        return mission

    def count(self) -> int:
        return len(self.list())

    def _generate_id(self) -> str:
        year = date.today().year
        existing = [
            mission
            for mission in self.repository.list()
            if mission.id.startswith(f"MIS-{year}-")
        ]
        number = len(existing) + 1
        return f"MIS-{year}-{number:04d}"