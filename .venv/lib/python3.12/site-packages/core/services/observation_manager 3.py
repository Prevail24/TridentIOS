from datetime import date

from core.models.observation import Observation
from core.storage.markdown_storage import MarkdownStorage
from core.services.id_generator import IDGenerator
from core.parsers.observation_parser import ObservationParser
from core.results.create_observation_result import CreateObservationResult

class ObservationManager:
    """
    Coordinates the creation and management of Observations.
    """

    def create(
        self,
        title: str,
        platform: str,
        category: str,
        difficulty: str,
        author: str = "Prevail",
        mission_id: str | None = None,
    ) -> CreateObservationResult:

        generator = IDGenerator()
        observation_id = generator.generate("OBS")

        observation = Observation(
            id=observation_id,
            type="Observation",
            title=title,
            author=author,
            created=date.today(),
            updated=date.today(),
            platform=platform,
            category=category,
            difficulty=difficulty,
            mission_id=mission_id,
        )

        storage = MarkdownStorage()
        filepath = storage.save(observation)

        if mission_id:
            from core.services.mission_service import MissionService

            MissionService().add_observation(
                mission_id,
                observation.id,
            )

        return CreateObservationResult(
            observation=observation,
            filepath=str(filepath),
        )
    
    def open(self, observation_id: str) -> Observation:
        storage = MarkdownStorage()
        markdown = storage.load(observation_id)
        
        parser = ObservationParser()
        return parser.parse(markdown)
    
    def list(self) -> list[Observation]:
        storage = MarkdownStorage()
        parser = ObservationParser()

        markdown_files = storage.list()

        observations = []

        for markdown in markdown_files:
            try:
                observations.append(parser.parse(markdown))
            except KeyError:
                continue

        return observations