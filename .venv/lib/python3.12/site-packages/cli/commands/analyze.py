from core.intelligence.analyst import Analyst
from core.renderers.analysis_renderer import AnalysisRenderer


def analyze_entity(entity_id: str):

    analysis = Analyst().analyze_entity(
        entity_id
    )

    AnalysisRenderer().render(
        analysis
    )