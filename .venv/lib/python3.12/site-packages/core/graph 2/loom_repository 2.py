import json
from pathlib import Path

from core.graph.edge import Edge
from core.graph.knowledge_graph import KnowledgeGraph
from core.graph.node import Node


class LoomRepository:
    def __init__(self, path="knowledge/loom/loom.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def save(self, graph: KnowledgeGraph):
        data = {
            "nodes": [
                {"entity_type": node.entity_type, "value": node.value}
                for node in graph.nodes.values()
            ],
            "edges": [
                {
                    "source": {
                        "entity_type": edge.source.entity_type,
                        "value": edge.source.value,
                    },
                    "relationship": edge.relationship,
                    "target": {
                        "entity_type": edge.target.entity_type,
                        "value": edge.target.value,
                    },
                }
                for edge in graph.edges
            ],
        }

        self.path.write_text(json.dumps(data, indent=2))

    def load(self):
        graph = KnowledgeGraph()

        if not self.path.exists():
            return graph

        data = json.loads(self.path.read_text())

        for node_data in data.get("nodes", []):
            graph.add_node(
                Node(
                    node_data["entity_type"],
                    node_data["value"],
                )
            )

        for edge_data in data.get("edges", []):
            graph.add_edge(
                Edge(
                    Node(
                        edge_data["source"]["entity_type"],
                        edge_data["source"]["value"],
                    ),
                    edge_data["relationship"],
                    Node(
                        edge_data["target"]["entity_type"],
                        edge_data["target"]["value"],
                    ),
                )
            )

        return graph