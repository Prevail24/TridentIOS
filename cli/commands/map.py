from core.agents.cartographer import Cartographer
from core.renderers.graph_renderer import GraphRenderer
from core.renderers.entity_graph_renderer import EntityGraphRenderer
from core.services.cartographer_service import Cartographer


def map_mission(mission_id: str):
    graph = Cartographer().map_mission(mission_id)
    GraphRenderer().render(graph)


def map_entity(entity_id: str):
    graph = Cartographer().entity_graph(entity_id)
    EntityGraphRenderer().render(graph)