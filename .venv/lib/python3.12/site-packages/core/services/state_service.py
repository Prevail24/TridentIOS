from pathlib import Path


class StateService:
    """
    Maintains lightweight runtime state for Trident.

    Examples:
        - Active Mission
        - Future active playbook
        - Future active workspace
    """

    def __init__(self):
        self.state_dir = Path(".state")
        self.state_dir.mkdir(exist_ok=True)

        self.active_mission_file = self.state_dir / "active_mission"

    def set_active_mission(self, mission_id: str):
        self.active_mission_file.write_text(
            mission_id,
            encoding="utf-8",
        )

    def get_active_mission(self) -> str | None:
        if not self.active_mission_file.exists():
            return None

        return self.active_mission_file.read_text(
            encoding="utf-8"
        ).strip()

    def clear_active_mission(self):
        if self.active_mission_file.exists():
            self.active_mission_file.unlink()