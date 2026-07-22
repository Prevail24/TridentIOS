import json
from pathlib import Path

from core.config import Config


class PlannerHistoryRepository:
    """
    Persists Planner recommendation lifecycle state by mission.

    Each mission owns an independent history file beneath:

        knowledge/planner_history/<MISSION-ID>.json
    """

    def __init__(self, root: Path | None = None) -> None:
        self.root = (
            root
            if root is not None
            else Config.KNOWLEDGE_DIR / "planner_history"
        )

    def _path_for(self, mission_id: str) -> Path:
        mission_id = mission_id.strip()

        if not mission_id:
            raise ValueError("Mission ID cannot be empty.")

        if Path(mission_id).name != mission_id:
            raise ValueError("Mission ID cannot contain path separators.")

        return self.root / f"{mission_id}.json"

    def load(self, mission_id: str) -> list[dict]:
        """
        Return persisted recommendation records for a mission.

        A mission without existing history begins with an empty list.
        """
        filepath = self._path_for(mission_id)

        if not filepath.exists():
            return []

        payload = json.loads(
            filepath.read_text(encoding="utf-8")
        )

        stored_mission_id = payload.get("mission_id")

        if stored_mission_id != mission_id:
            raise ValueError(
                "Planner history mission ID does not match its file."
            )

        recommendations = payload.get("recommendations", [])

        if not isinstance(recommendations, list):
            raise ValueError(
                "Planner history recommendations must be a list."
            )

        return recommendations

    def save(
        self,
        mission_id: str,
        recommendations: list[dict],
    ) -> Path:
        """
        Atomically replace the persisted history for a mission.
        """
        filepath = self._path_for(mission_id)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        payload = {
            "mission_id": mission_id,
            "recommendations": recommendations,
        }

        temporary_path = filepath.with_suffix(".tmp")

        temporary_path.write_text(
            json.dumps(
                payload,
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

        temporary_path.replace(filepath)

        return filepath

    def clear(self, mission_id: str) -> None:
        """
        Delete persisted Planner history for one mission.
        """
        filepath = self._path_for(mission_id)

        if filepath.exists():
            filepath.unlink()
