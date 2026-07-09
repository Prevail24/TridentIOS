from core.graph.edge import Edge
from core.graph.entity_types import EntityType
from core.graph.knowledge_graph import KnowledgeGraph
from core.graph.node import Node
from core.graph.relationship_types import RelationshipType


class GraphBuilder:
    """
    Builds graph relationships from structured intelligence.
    """

    def __init__(self):
        self.graph = KnowledgeGraph()

    def add_host_port_service(
        self,
        host_value: str,
        port_value: str,
        service_value: str | None = None,
        product_value: str | None = None,
        version_value: str | None = None,
    ):
        host = self.graph.add_node(Node(EntityType.HOST, host_value))
        port = self.graph.add_node(Node(EntityType.PORT, str(port_value)))

        self.graph.add_edge(
            Edge(host, RelationshipType.HAS_PORT, port)
        )

        if service_value:
            service = self.graph.add_node(
                Node(EntityType.SERVICE, service_value)
            )
            self.graph.add_edge(
                Edge(port, RelationshipType.RUNS_SERVICE, service)
            )

        if product_value:
            product = self.graph.add_node(
                Node(EntityType.PRODUCT, product_value)
            )
            self.graph.add_edge(
                Edge(service if service_value else port, RelationshipType.HAS_PRODUCT, product)
            )

        if version_value:
            version = self.graph.add_node(
                Node(EntityType.VERSION, version_value)
            )
            self.graph.add_edge(
                Edge(product if product_value else port, RelationshipType.HAS_VERSION, version)
            )

        return self.graph