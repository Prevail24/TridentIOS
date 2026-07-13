from core.services.state_service import StateService


class MissionContext:
    """
    Provides active mission awareness to the Trident kernel.

    StateService is the canonical source for runtime mission state.
    """

    def __init__(self):
        self.state = StateService()

    def current_mission_id(self) -> str | None:
        return self.state.get_active_mission()

    def require_mission_id(self) -> str:
        mission_id = self.current_mission_id()

        if mission_id is None:
            raise RuntimeError(
                "No active mission. Start or activate a mission first."
            )

        return mission_id

    def enrich(self, payload: dict) -> dict:
        return {
            "mission_id": self.current_mission_id(),
            **payload,
        }