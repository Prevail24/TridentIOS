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
            raise ValueError(
                "Mission ID cannot contain path separators."
            )

        return self.root / f"{mission_id}.json"

    def _load_payload(self, mission_id: str) -> dict:
        filepath = self._path_for(mission_id)

        if not filepath.exists():
            return {
                "mission_id": mission_id,
                "recommendations": [],
                "events": [],
            }

        payload = json.loads(
            filepath.read_text(encoding="utf-8")
        )

        if not isinstance(payload, dict):
            raise ValueError(
                "Planner history payload must be an object."
            )

        stored_mission_id = payload.get("mission_id")

        if stored_mission_id != mission_id:
            raise ValueError(
                "Planner history mission ID does not match its file."
            )

        recommendations = payload.get(
            "recommendations",
            [],
        )

        if not isinstance(recommendations, list):
            raise ValueError(
                "Planner history recommendations must be a list."
            )

        # Older Planner history files predate the event ledger.
        events = payload.get("events", [])

        if not isinstance(events, list):
            raise ValueError(
                "Planner history events must be a list."
            )

        return {
            "mission_id": mission_id,
            "recommendations": recommendations,
            "events": events,
        }

    def load(self, mission_id: str) -> list[dict]:
        """
        Return the latest recommendation states for a mission.
        """
        return self._load_payload(
            mission_id
        )["recommendations"]

    def load_events(self, mission_id: str) -> list[dict]:
        """
        Return the immutable lifecycle event ledger for a mission.

        Legacy history files without an events field return an empty
        ledger.
        """
        return self._load_payload(
            mission_id
        )["events"]

    def save(
        self,
        mission_id: str,
        recommendations: list[dict],
        *,
        events: list[dict] | None = None,
    ) -> Path:
        """
        Atomically replace the complete persisted Planner history.
        """
        if not isinstance(recommendations, list):
            raise ValueError(
                "Planner history recommendations must be a list."
            )

        if events is None:
            # Preserve an existing ledger for callers using the
            # pre-ledger save signature.
            events = self.load_events(mission_id)

        if not isinstance(events, list):
            raise ValueError(
                "Planner history events must be a list."
            )

        filepath = self._path_for(mission_id)
        filepath.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        payload = {
            "mission_id": mission_id,
            "recommendations": recommendations,
            "events": events,
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
