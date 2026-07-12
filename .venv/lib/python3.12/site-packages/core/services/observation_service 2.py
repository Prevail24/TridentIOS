from core.events.event import Event
from core.events.event_bus import EventBus, event_bus
from core.models.observation import Observation
from core.repositories.observation_repository import ObservationRepository
from core.results.create_observation_result import CreateObservationResult
from core.services.id_generator import IdGenerator


class ObservationService:
    """
    Coordinates the creation and management of Observations.

    Successful creation publishes an ObservationCreated event
    to Trident's shared event bus.
    """

    def __init__(
        self,
        repository: ObservationRepository | None = None,
        bus: EventBus | None = None,
    ) -> None:
        self.repository = repository or ObservationRepository()
        self.bus = bus if bus is not None else event_bus

    def create(
        self,
        category: str,
        data: dict,
        mission_id: str | None = None,
        tool_run_id: str | None = None,
        evidence_id: str | None = None,
        confidence: float = 1.0,
    ) -> CreateObservationResult:
        observation_id = IdGenerator.next("OBS")

        observation = Observation(
            id=observation_id,
            mission_id=mission_id,
            tool_run_id=tool_run_id,
            evidence_id=evidence_id,
            category=category,
            data=data,
            confidence=confidence,
        )

        filepath = self.repository.save(observation)

        if mission_id:
            from core.services.mission_service import MissionService

            MissionService().add_observation(
                mission_id,
                observation.id,
            )

        self.bus.publish(
            Event(
                event_type="ObservationCreated",
                payload={
                    "observation_id": observation.id,
                    "mission_id": observation.mission_id,
                    "tool_run_id": observation.tool_run_id,
                    "evidence_id": observation.evidence_id,
                    "category": observation.category,
                    "data": observation.data,
                    "confidence": observation.confidence,
                    "observed_at": observation.observed_at.isoformat(),
                    "filepath": str(filepath),
                },
            )
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
    ) -> None:
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