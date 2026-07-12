from datetime import date

from core.config import Config


class EntityIDGenerator:
    """
    Generates Entity IDs.

    Example:
        ENT-2026-0001
    """

    def generate(self) -> str:
        year = date.today().year
        entity_root = Config.KNOWLEDGE_DIR / "entities" / str(year)
        entity_root.mkdir(parents=True, exist_ok=True)

        existing = sorted(entity_root.glob(f"ENT-{year}-*.md"))
        number = len(existing) + 1

        return f"ENT-{year}-{number:04d}"