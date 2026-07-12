from core.services.cartographer_service import Cartographer


class AnalystService:
    """
    Performs intelligence analysis over The Loom.
    """

    def __init__(self):
        self.cartographer = Cartographer()

    def analyze_entity(self, entity_id: str):

        graph = self.cartographer.entity_graph(entity_id)

        return {
            "entity": graph.center,
            "connections": len(graph.edges),
            "edges": graph.edges,
        }