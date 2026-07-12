from core.models.mission import Mission
from core.storage.mission_storage import MissionStorage
import json
from pathlib import Path


class MissionRepository:
    """
    Repository for active mission workspaces.

    Repository owns retrieval and persistence coordination.
    Storage owns file format.
    Mission owns business state.
    """

    def __init__(self, storage: MissionStorage | None = None) -> None:
        self.storage = storage or MissionStorage()

    def save(self, mission: Mission):
        return self.storage.save(mission)

    def open(self, mission_id: str) -> Mission:
        return self.storage.load(mission_id)

    def list(self) -> list[Mission]:
        missions: list[Mission] = []

        for path in sorted(self.storage.root.glob("MIS-*/mission.md")):
            mission_id = path.parent.name
            missions.append(self.open(mission_id))

        return missions
    
