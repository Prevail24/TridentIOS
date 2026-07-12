from core.engine import TridentEngine
from core.renderers.mission_renderer import MissionRenderer


def mission_status() -> None:
    engine = TridentEngine()

    mission_id = engine.state.get_active_mission()

    if not mission_id:
        print("No active mission.")
        print("Open one with: trident mission open <MISSION_ID>")
        return

    mission = engine.missions.open(mission_id)
    MissionRenderer().render(mission)

    print()
    print("Active Mission")
    print("--------------")
    print(mission.id)