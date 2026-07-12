from pathlib import Path

from core.config import Config
from core.models.evidence import Evidence
from core.parsers.evidence_parser import EvidenceParser


class EvidenceRepository:
    """
    Handles persistence for Evidence objects.
    """

    def __init__(self):
        self.parser = EvidenceParser()

    def save(self, evidence: Evidence) -> Path:
        year = evidence.created.year

        evidence_root = (
            Config.KNOWLEDGE_DIR
            / "evidence"
            / str(year)
        )

        evidence_root.mkdir(parents=True, exist_ok=True)

        filepath = evidence_root / f"{evidence.id}.md"

        notes = "\n".join(
            f"- {note}"
            for note in evidence.notes
        )

        content = f"""# {evidence.title}

## Metadata

- ID: {evidence.id}
- Type: Evidence
- Evidence Type: {evidence.evidence_type}
- Source: {evidence.source}
- Observation: {evidence.observation_id}
- Author: {evidence.author}
- Status: {evidence.status}
- Updated: {evidence.updated}

---

# Notes

{notes}
"""

        filepath.write_text(content, encoding="utf-8")

        return filepath

    def open(self, evidence_id: str) -> Evidence:
        """
        Return one Evidence object by ID.
        """
        year = evidence_id.split("-")[1]

        filepath = (
            Config.KNOWLEDGE_DIR
            / "evidence"
            / year
            / f"{evidence_id}.md"
        )

        markdown = filepath.read_text(encoding="utf-8")

        return self.parser.parse(markdown)

    def list(self) -> list[Evidence]:
        """
        Return all Evidence objects stored in The Loom.
        """
        evidence_root = Config.KNOWLEDGE_DIR / "evidence"

        evidence_items = []

        for file in sorted(evidence_root.glob("**/*.md")):
            evidence_items.append(self.open(file.stem))

        return evidence_items