from pathlib import Path


class ActiveMissionService:
    """
    Maintains the currently active mission.

    This service is intentionally tiny.
    It acts like Git's HEAD reference.
    """

    CURRENT_FILE = Path("knowledge/mission/current")

    def activate(self, mission_id: str) -> None:
        self.CURRENT_FILE.parent.mkdir(parents=True, exist_ok=True)
        self.CURRENT_FILE.write_text(mission_id)

    def current(self) -> str | None:
        if not self.CURRENT_FILE.exists():
            return None

        mission_id = self.CURRENT_FILE.read_text().strip()

        return mission_id or None

    def clear(self) -> None:
        if self.CURRENT_FILE.exists():
            self.CURRENT_FILE.unlink()

    def has_active(self) -> bool:
        return self.current() is not None