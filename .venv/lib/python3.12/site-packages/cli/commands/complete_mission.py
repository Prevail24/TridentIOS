from core.engine import TridentEngine


def complete_mission() -> None:
    engine = TridentEngine()

    mission_id = engine.state.get_active_mission()

    if not mission_id:
        print("No active mission.")
        print("Open one with: trident mission open <MISSION_ID>")
        return

    mission = engine.missions.complete(mission_id)

    print("🔱 Mission Completed")
    print()
    print(mission.id)
    print(mission.title)
    