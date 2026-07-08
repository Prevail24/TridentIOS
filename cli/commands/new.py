from core import engine
from core.rendering.terminal_renderer import TerminalRenderer
from core.engine import TridentEngine

def new_observation():
    renderer = TerminalRenderer()
    renderer.banner("Create New Observation")

    title = input("Challenge Name : ")
    platform = input("Platform       : ")
    category = input("Category       : ")
    difficulty = input("Difficulty     : ")
    mission_id = input("Mission ID     : ").strip() or None

    engine = TridentEngine()

    result = engine.observations.create(
        title=title,
        platform=platform,
        category=category,
        difficulty=difficulty,
        mission_id=mission_id,
    )

    renderer.success(
        "✓ Thread Successfully Woven",
        f"""Observation ID

{result.observation.id}

Saved To

{result.filepath}""",
    )

    renderer.observation_card(result.observation)