from core.engine import TridentEngine


def archive_mission():
    engine = TridentEngine()

    mission_id = engine.state.get_active_mission()

    if not mission_id:
        print("No active mission.")
        return

    mission = engine.missions.archive(mission_id)

    engine.state.clear_active_mission()

    print("⚓ Mission Archived")
    print()
    print(mission.id)
    print(mission.title)
    print()
    print("Active mission cleared.")