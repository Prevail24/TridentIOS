from core.models.entity import Entity
from core.repositories.entity_repository import EntityRepository
from core.services.entity_id_generator import EntityIDGenerator


class EntityService:
    """
    Business logic for Entity objects.
    """

    def __init__(self):
        self.repository = EntityRepository()
        self.id_generator = EntityIDGenerator()

    def create(
        self,
        type: str,
        value: str,
    ) -> Entity:

        entity = Entity(
            id=self.id_generator.generate(),
            type=type,
            value=value,
        )

        self.repository.save(entity)

        return entity

    def open(self, entity_id: str) -> Entity:
        return self.repository.open(entity_id)

    def list(self):
        return self.repository.list()

    def count(self):
        return len(self.repository.list())