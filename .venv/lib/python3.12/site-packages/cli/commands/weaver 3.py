from core.agents.weaver import Weaver
from core.engine import TridentEngine
from core.renderers.weaver_renderer import WeaverRenderer


def analyze_observation(observation_id):

    engine = TridentEngine()
    observation = engine.observations.open(observation_id)
    report = Weaver().analyze_observation(observation)

    WeaverRenderer().render(report)