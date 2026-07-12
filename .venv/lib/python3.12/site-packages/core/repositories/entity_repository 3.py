from pathlib import Path

from core.config import Config
from core.models.entity import Entity
from core.parsers.entity_parser import EntityParser


class EntityRepository:
    """
    Handles persistence for Entity objects.
    """

    def __init__(self):
        self.parser = EntityParser()

    def save(self, entity: Entity) -> Path:
        year = entity.id.split("-")[1]

        entity_root = (
            Config.KNOWLEDGE_DIR
            / "entities"
            / year
        )

        entity_root.mkdir(parents=True, exist_ok=True)

        filepath = entity_root / f"{entity.id}.md"

        markdown = self.parser.serialize(entity)
        filepath.write_text(markdown, encoding="utf-8")

        return filepath

    def open(self, entity_id: str) -> Entity:
        """
        Return one Entity object by ID.
        """
        year = entity_id.split("-")[1]

        filepath = (
            Config.KNOWLEDGE_DIR
            / "entities"
            / year
            / f"{entity_id}.md"
        )

        markdown = filepath.read_text(encoding="utf-8")

        return self.parser.parse(markdown)

    def list(self) -> list[Entity]:
        """
        Return all Entity objects stored in The Loom.
        """
        entity_root = Config.KNOWLEDGE_DIR / "entities"

        entity_items = []

        for file in sorted(entity_root.glob("**/*.md")):
            entity_items.append(self.open(file.stem))

        return entity_items

    def find_by_type_and_value(
        self,
        entity_type: str,
        value: str,
    ) -> Entity | None:
        """
        Return the canonical Entity matching the given type and normalized value.
        """
        for entity in self.list():
            if entity.entity_type == entity_type and entity.value == value:
                return entity

        return None