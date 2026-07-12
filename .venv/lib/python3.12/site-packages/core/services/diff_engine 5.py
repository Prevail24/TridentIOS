from core.services.loom_service import LoomService


class DiffEngine:
    """
    Compares Trident knowledge graphs.
    """

    def __init__(self):
        self.loom = LoomService()

    def compare(self, entity_value: str):
        result = self.loom.graph_for_entity(entity_value)

        if result is None:
            return None

        entity, graph = result

        return {
            "entity": entity,
            "graph": graph,
        }