from core.graph.knowledge_graph import KnowledgeGraph
from core.graph.node import Node
from core.graph.edge import Edge
from core.graph.entity_types import EntityType
from core.graph.relationship_types import RelationshipType


graph = KnowledgeGraph()

host = graph.add_node(
    Node(
        EntityType.HOST,
        "45.33.32.156",
    )
)

port = graph.add_node(
    Node(
        EntityType.PORT,
        "22",
    )
)

graph.add_edge(
    Edge(
        host,
        RelationshipType.HAS_PORT,
        port,
    )
)

print()
print("KNOWLEDGE GRAPH")
print("----------------")
print("Nodes:", graph.node_count())
print("Edges:", graph.edge_count())