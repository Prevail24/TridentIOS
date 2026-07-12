from datetime import date

from core.config import Config


class EvidenceIDGenerator:
    """
    Generates Evidence IDs.

    Example:
        EVD-2026-0001
    """

    def generate(self) -> str:
        year = date.today().year
        evidence_root = Config.KNOWLEDGE_DIR / "evidence" / str(year)
        evidence_root.mkdir(parents=True, exist_ok=True)

        existing = sorted(evidence_root.glob(f"EVD-{year}-*.md"))
        number = len(existing) + 1

        return f"EVD-{year}-{number:04d}"