from core.services.active_mission_service import ActiveMissionService


class MissionContext:
    """
    Provides mission awareness to the Trident Kernel.
    """

    def __init__(self):
        self.active_mission = ActiveMissionService()

    def current_mission_id(self):
        return self.active_mission.current()

    def require_mission_id(self):
        mission_id = self.current_mission_id()

        if mission_id is None:
            raise RuntimeError(
                "No active mission. Start one with: trident mission start <name>"
            )

        return mission_id

    def enrich(self, payload: dict):
        return {
            "mission_id": self.current_mission_id(),
            **payload,
        }