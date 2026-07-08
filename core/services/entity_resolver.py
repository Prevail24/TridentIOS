from core.models.entity import Entity
from core.repositories.entity_repository import EntityRepository
from datetime import date

class EntityResolver:
    """
    Resolves raw discovered values into canonical Loom Entities.

    Nothing should create Entities directly without going through this resolver.
    """

    def __init__(self):
        self.repository = EntityRepository()

    def normalize(self, entity_type: str, value: str) -> str:
        value = value.strip()

        if entity_type in {"domain", "email", "url", "hostname", "hash"}:
            return value.lower()

        if entity_type == "cve":
            return value.upper().replace(" ", "-")

        return value

    def resolve(
        self,
        entity_type: str,
        value: str,
        display_name: str | None = None,
    ) -> Entity | None:
        """
        Return the canonical Entity.

        Later this will:
        - normalize the value
        - search existing entities
        - return existing if found
        - create new if missing
        """
        normalized_value = self.normalize(entity_type, value)

        existing = self.repository.find_by_type_and_value(
            entity_type,
            normalized_value,
        )

        if existing:
            return existing

        entity = Entity(
            id=self._generate_id(),
            entity_type=entity_type,
            value=normalized_value,
            display_name=display_name,
        )

        self.repository.save(entity)
        return entity

    def _generate_id(self) -> str:
        year = date.today().year

        existing = self.repository.list()
        number = len(existing) + 1

        return f"ENT-{year}-{number:04d}"