from core.rendering.terminal_renderer import TerminalRenderer
from core.engine import TridentEngine


def open_observation(observation_id: str):
    renderer = TerminalRenderer()
    renderer.banner("Open Observation")
    engine = TridentEngine()
    observation = engine.observations.open(observation_id)
    renderer.observation_card(observation)