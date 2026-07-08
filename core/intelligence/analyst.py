from core.intelligence.cartographer import Cartographer


class Analyst:
    """
    Performs intelligence analysis over The Loom.
    """

    def __init__(self):
        self.cartographer = Cartographer()

    def analyze_entity(self, entity_id: str):

        graph = self.cartographer.entity_graph(entity_id)

        analysis = {
            "entity": graph.center,
            "connections": len(graph.edges),
            "incoming": 0,
            "outgoing": 0,
            "relationships": [],
        }

        for edge in graph.edges:

            if edge.source == entity_id:
                analysis["outgoing"] += 1

            if edge.target == entity_id:
                analysis["incoming"] += 1

            analysis["relationships"].append(edge)

        return analysis