from datetime import date

from core.models.observation import Observation
from core.services.id_generator import IdGenerator
from core.results.create_observation_result import CreateObservationResult
from core.repositories.observation_repository import ObservationRepository

class ObservationService:
    """
    Coordinates the creation and management of Observations.
    """

    def __init__(self):
        self.repository = ObservationRepository()

    def create(
        self,
        title: str,
        platform: str,
        category: str,
        difficulty: str,
        author: str = "Prevail",
        mission_id: str | None = None,
    ) -> CreateObservationResult:

        generator = IdGenerator()
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

        filepath = self.repository.save(observation)

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
        return self.repository.open(observation_id)

    def add_evidence(
        self,
        observation_id: str,
        evidence_id: str,
    ):
        """
        Attach evidence to an Observation.
        """

        observation = self.open(observation_id)
        observation.add_evidence(evidence_id)
        self.repository.save(observation)

    def list(self) -> list[Observation]:
        return self.repository.list()

    def count(self) -> int:
        """
        Return the total number of Observations stored in The Loom.
        """
        return len(self.repository.list())