from datetime import datetime

from core.models.relationship import Relationship


class RelationshipParser:
    """
    Serializes and parses canonical relationships.
    """

    def serialize(self, relationship: Relationship) -> str:
        return f"""# Relationship

## Metadata

- ID: {relationship.id}
- Source: {relationship.source_id}
- Target: {relationship.target_id}
- Type: {relationship.relationship_type}
- Confidence: {relationship.confidence}
- Created At: {relationship.created_at.isoformat()}
"""

    def parse(self, markdown: str) -> Relationship:
        metadata = {}

        for line in markdown.splitlines():
            line = line.strip()

            if line.startswith("- ") and ":" in line:
                key, value = line[2:].split(":", 1)
                metadata[key.strip()] = value.strip()

        return Relationship(
            id=metadata["ID"],
            source_id=metadata["Source"],
            target_id=metadata["Target"],
            relationship_type=metadata["Type"],
            confidence=float(metadata["Confidence"]),
            created_at=datetime.fromisoformat(
                metadata["Created At"]
            ),
        )