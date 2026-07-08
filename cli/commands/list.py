from core.rendering.terminal_renderer import TerminalRenderer
from core.engine import TridentEngine


def list_observations():
    renderer = TerminalRenderer()
    renderer.banner("Observation Archive")
    engine = TridentEngine()
    observations = engine.observations.list()
    renderer.archive(observations)

def list_missions():
    renderer = TerminalRenderer()
    renderer.banner("Mission Archive")

    engine = TridentEngine()
    missions = engine.missions.list()

    if not missions:
        renderer.info(
            "No Missions Found",
            "Create one with: trident mission new",
        )
        return

    active = [m for m in missions if m.status == "active"]
    completed = [m for m in missions if m.status == "completed"]
    archived = [m for m in missions if m.status == "archived"]

    sections = [
        ("🟢 ACTIVE", active),
        ("🔵 COMPLETED", completed),
        ("⚫ ARCHIVED", archived),
    ]

    for title, group in sections:
        if not group:
            continue

        print()
        print(title)
        print("-" * 40)

        for mission in group:
            print(mission.id)
            print(mission.title)
            print()

    print("-" * 40)
    print(f"Total Missions: {len(missions)}")