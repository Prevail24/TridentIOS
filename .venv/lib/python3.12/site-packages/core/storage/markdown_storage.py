from pathlib import Path
from core.config import Config
from core.models.observation import Observation


class MarkdownStorage:
    """
    Saves and loads Observations from The Loom.
    """

    def save(self, observation: Observation) -> Path:
        year = observation.created.year
        folder = Config.OBSERVATIONS_DIR / str(year)
        folder.mkdir(parents=True, exist_ok=True)
        filepath = folder / f"{observation.id}.md"
        evidence = "\n".join(
            f"- {evidence_id}"
            for evidence_id in observation.evidence
        )

        notes = "\n".join(
            f"- {note}"
            for note in observation.notes
        )
        content = f"""# {observation.title}

## Metadata

- ID: {observation.id}
- Type: {observation.type}
- Author: {observation.author}
- Platform: {observation.platform}
- Category: {observation.category}
- Difficulty: {observation.difficulty}
- Status: {observation.status}
- Mission: {observation.mission_id or ""}

---

# Evidence

{evidence}

---

# Notes

{notes}
"""

        filepath.write_text(content, encoding="utf-8")

        return filepath

    def load(self, observation_id: str) -> str:
        """
        Loads a raw Observation markdown file.
        """

        observations_root = Path("knowledge/observations")

        matches = list(observations_root.glob(f"**/{observation_id}.md"))

        if not matches:
            raise FileNotFoundError(
                f"Observation '{observation_id}' was not found."
            )

        return matches[0].read_text(encoding="utf-8")

    def list(self) -> list[str]:
        """
        Lists all raw Observation markdown files.
        """

        observations_root = Config.OBSERVATIONS_DIR

        if not observations_root.exists():
            return []

        files = sorted(observations_root.glob("**/OBS-*.md"))

        return [
            file.read_text(encoding="utf-8")
            for file in files
        ]