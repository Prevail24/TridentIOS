from datetime import UTC, datetime
from pathlib import Path

from core.config import Config


class IdGenerator:
    """
    Generates consistent Trident IDs.

    Examples:
    MIS-2026-0001
    RUN-2026-0001
    ENT-2026-0001
    OBS-2026-0001
    REL-2026-0001
    """

    COLLECTIONS = {
        "MIS": "missions",
        "RUN": "tool_runs",
        "ENT": "entities",
        "OBS": "observations",
        "REL": "relationships",
    }

    @classmethod
    def next(cls, prefix: str) -> str:
        if prefix not in cls.COLLECTIONS:
            raise ValueError(f"Unknown ID prefix: {prefix}")

        year = datetime.now(UTC).year
        root = Config.KNOWLEDGE_DIR / cls.COLLECTIONS[prefix]
        root.mkdir(parents=True, exist_ok=True)

        existing = list(root.glob(f"{prefix}-{year}-*.md"))

        return f"{prefix}-{year}-{len(existing) + 1:04d}"
