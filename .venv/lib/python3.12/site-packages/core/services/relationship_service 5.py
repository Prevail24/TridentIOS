from core.models.relationship import Relationship
from core.repositories.relationship_repository import RelationshipRepository
from core.services.relationship_id_generator import RelationshipIDGenerator


class RelationshipService:
    """
    Creates and manages links between objects in The Loom.
    """

    def __init__(self):
        self.repository = RelationshipRepository()
        self.id_generator = RelationshipIDGenerator()

    def create(self, source: str, relationship: str, target: str) -> Relationship:
        relationship_obj = Relationship(
            id=self.id_generator.generate(),
            source=source,
            relationship=relationship,
            target=target,
        )

        self.repository.save(relationship_obj)

        return relationship_obj

    def open(self, relationship_id: str) -> Relationship:
        return self.repository.open(relationship_id)

    def list(self):
        return self.repository.list()

    def count(self):
        return len(self.repository.list())