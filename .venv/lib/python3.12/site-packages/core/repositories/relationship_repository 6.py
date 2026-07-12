from pathlib import Path

from core.config import Config
from core.models.relationship import Relationship
from core.parsers.relationship_parser import RelationshipParser


class RelationshipRepository:
    """
    Repository for canonical relationships.
    """
    def find(
            self,
            *,
            source_id: str,
            target_id: str,
            relationship_type: str,
        ) -> Relationship | None:

            for relationship in self.list():
                if (
                    relationship.source_id == source_id
                    and relationship.target_id == target_id
                    and relationship.relationship_type == relationship_type
                ):
                    return relationship

            return None    

    def __init__(self):
        self.parser = RelationshipParser()

    def next_id(self) -> str:
        root = Config.KNOWLEDGE_DIR / "relationships"
        root.mkdir(parents=True, exist_ok=True)

        count = len(list(root.glob("REL-*.md"))) + 1

        return f"REL-2026-{count:04d}"

    def save(self, relationship: Relationship) -> Path:
        root = Config.KNOWLEDGE_DIR / "relationships"
        root.mkdir(parents=True, exist_ok=True)

        path = root / f"{relationship.id}.md"

        path.write_text(
            self.parser.serialize(relationship),
            encoding="utf-8",
        )

        return path

    def open(self, relationship_id: str) -> Relationship:
        path = (
            Config.KNOWLEDGE_DIR
            / "relationships"
            / f"{relationship_id}.md"
        )

        markdown = path.read_text(encoding="utf-8")

        return self.parser.parse(markdown)

    def list(self) -> list[Relationship]:
        root = Config.KNOWLEDGE_DIR / "relationships"
        root.mkdir(parents=True, exist_ok=True)

        relationships = []

        for file in sorted(root.glob("REL-*.md")):
            relationships.append(self.open(file.stem))

        return relationships