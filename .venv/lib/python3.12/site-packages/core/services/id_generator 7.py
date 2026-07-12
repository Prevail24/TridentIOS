from datetime import datetime
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

    PATHS = {
        "MIS": Config.KNOWLEDGE_DIR / "missions",
        "RUN": Config.KNOWLEDGE_DIR / "tool_runs",
        "ENT": Config.KNOWLEDGE_DIR / "entities",
        "OBS": Config.KNOWLEDGE_DIR / "observations",
        "REL": Config.KNOWLEDGE_DIR / "relationships",
    }

    @classmethod
    def next(cls, prefix: str) -> str:
        if prefix not in cls.PATHS:
            raise ValueError(f"Unknown ID prefix: {prefix}")

        year = datetime.utcnow().year
        root = cls.PATHS[prefix]
        root.mkdir(parents=True, exist_ok=True)

        existing = list(root.glob(f"{prefix}-{year}-*.md"))

        return f"{prefix}-{year}-{len(existing) + 1:04d}"