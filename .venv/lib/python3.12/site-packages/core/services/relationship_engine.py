from core.models.relationship import Relationship
from core.repositories.relationship_repository import RelationshipRepository


class RelationshipEngine:
    """
    Creates canonical relationships between entities.
    """

    def __init__(self):
        self.repository = RelationshipRepository()

    def create(
        self,
        *,
        source_id: str,
        target_id: str,
        relationship_type: str,
        confidence: float = 1.0,
    ) -> Relationship:

        existing = self.repository.find(
            source_id=source_id,
            target_id=target_id,
            relationship_type=relationship_type,
        )

        if existing:
            return existing

        relationship = Relationship(
            id=self.repository.next_id(),
            source_id=source_id,
            target_id=target_id,
            relationship_type=relationship_type,
            confidence=confidence,
        )

        self.repository.save(relationship)

        return relationship