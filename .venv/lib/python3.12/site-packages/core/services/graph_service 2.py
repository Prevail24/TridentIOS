from core.models.entity_graph import EntityGraph
from core.models.graph_edge import GraphEdge
from core.services.relationship_service import RelationshipService


class GraphService:

    def __init__(self):

        self.relationships = RelationshipService()

    def build_entity_graph(self, entity_id: str):

        graph = EntityGraph(center=entity_id)

        for relationship in self.relationships.list():

            if relationship.source == entity_id:

                graph.edges.append(
                    GraphEdge(
                        source=relationship.source,
                        relationship=relationship.relationship,
                        target=relationship.target,
                    )
                )

            elif relationship.target == entity_id:

                graph.edges.append(
                    GraphEdge(
                        source=relationship.source,
                        relationship=relationship.relationship,
                        target=relationship.target,
                    )
                )

        return graph