from core.services.loom_service import LoomService
from core.services.history_service import HistoryService

class HostProfileService:
    """
    Builds a complete profile for a host.
    """

    def __init__(self):
        self.loom = LoomService()
        self.history = HistoryService()

    def build(self, host: str):
        result = self.loom.graph_for_entity(host)

        if result is None:
            return None

        entity, graph = result
        history = self.history.build(host)

        profile = {
            "host": entity.value,

            "first_seen": history["first_seen"] if history else None,
            "last_seen": history["last_seen"] if history else None,
            "observation_count": history["observation_count"] if history else 0,

            "ports": [],
            "services": [],
            "products": [],
            "versions": [],
        }

        for relationship, port in self.loom.outgoing_relationships(entity.id):

            if port.entity_type != "port":
                continue

            profile["ports"].append(port.value)

            for rel2, service in self.loom.outgoing_relationships(port.id):

                if service.entity_type != "service":
                    continue

                profile["services"].append(service.value)

                for rel3, product in self.loom.outgoing_relationships(service.id):

                    if product.entity_type != "product":
                        continue

                    profile["products"].append(product.value)

                    for rel4, version in self.loom.outgoing_relationships(product.id):

                        if version.entity_type == "version":
                            profile["versions"].append(version.value)

        return profile