from datetime import date

from core.config import Config


class RelationshipIDGenerator:
    """
    Generates Relationship IDs.

    Example:
        REL-2026-0001
    """

    def generate(self) -> str:

        year = date.today().year

        relationship_root = (
            Config.KNOWLEDGE_DIR
            / "relationships"
            / str(year)
        )

        relationship_root.mkdir(
            parents=True,
            exist_ok=True,
        )

        existing = sorted(
            relationship_root.glob(
                f"REL-{year}-*.md"
            )
        )

        number = len(existing) + 1

        return f"REL-{year}-{number:04d}"