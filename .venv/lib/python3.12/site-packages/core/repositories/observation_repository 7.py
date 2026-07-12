from pathlib import Path

from core.config import Config
from core.models.observation import Observation
from core.parsers.observation_parser import ObservationParser


class ObservationRepository:
    """
    Handles persistence for canonical Observation objects.
    """

    def __init__(self):
        self.parser = ObservationParser()

    def save(self, observation: Observation) -> Path:
        observations_root = Config.KNOWLEDGE_DIR / "observations"
        observations_root.mkdir(parents=True, exist_ok=True)

        filepath = observations_root / f"{observation.id}.md"
        filepath.write_text(
            self.parser.serialize(observation),
            encoding="utf-8",
        )

        return filepath

    def open(self, observation_id: str) -> Observation:
        filepath = Config.KNOWLEDGE_DIR / "observations" / f"{observation_id}.md"
        markdown = filepath.read_text(encoding="utf-8")
        return self.parser.parse(markdown)

    def list(self) -> list[Observation]:
        observations_root = Config.KNOWLEDGE_DIR / "observations"
        observations_root.mkdir(parents=True, exist_ok=True)

        observations = []

        for file in sorted(observations_root.glob("OBS-*.md")):
            observations.append(self.open(file.stem))

        return observations