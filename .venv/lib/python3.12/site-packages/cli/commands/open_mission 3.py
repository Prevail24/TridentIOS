from core.engine import TridentEngine
from core.renderers.mission_renderer import MissionRenderer


def open_mission(mission_id: str):
    engine = TridentEngine()
    renderer = MissionRenderer()

    mission = engine.missions.open(mission_id)

    renderer.render(mission)
    engine.state.set_active_mission(mission.id)

    print()
    print("Recommended Next Action")
    print("-----------------------")
    print("TRD-PB-001 Quick Recon")
    print()
    print(f"Workspace: missions/{mission.id}/")