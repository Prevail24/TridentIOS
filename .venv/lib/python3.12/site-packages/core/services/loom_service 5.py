from collections import defaultdict

from core.repositories.entity_repository import EntityRepository
from core.repositories.relationship_repository import RelationshipRepository


class LoomService:
    """
    Queries and formats Trident's knowledge graph.
    """

    def __init__(self):
        self.entities = EntityRepository()
        self.relationships = RelationshipRepository()

    def graph_for_entity(self, entity_value: str):
        entities = self.entities.list()
        relationships = self.relationships.list()

        entity = next(
            (
                e
                for e in entities
                if e.value == entity_value
            ),
            None,
        )

        if entity is None:
            return None

        entity_lookup = {
            e.id: e
            for e in entities
        }

        graph = defaultdict(list)

        for rel in relationships:
            if rel.source_id == entity.id:
                graph[rel.relationship_type].append(
                    entity_lookup.get(rel.target_id)
                )

        return entity, graph

    def outgoing_relationships(self, entity_id: str):
        entities = {
            e.id: e
            for e in self.entities.list()
        }

        results = []

        for rel in self.relationships.list():
            if rel.source_id != entity_id:
                continue

            target = entities.get(rel.target_id)

            if target is None:
                continue

            results.append((rel, target))

        return results