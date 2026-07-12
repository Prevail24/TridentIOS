from core.services.id_generator import IdGenerator
from core.models.observation import Observation
from core.repositories.observation_repository import ObservationRepository


class ObservationEmitter:
    """
    Emits canonical Trident observations.
    """

    def __init__(self):
        self.repository = ObservationRepository()

    def emit(
        self,
        *,
        mission_id,
        tool_run_id,
        evidence_id,
        category,
        data,
        confidence=1.0,
    ) -> Observation:

        observation = Observation(
            id=IdGenerator.next("OBS"),
            mission_id=mission_id,
            tool_run_id=tool_run_id,
            evidence_id=evidence_id,
            category=category,
            data=data,
            confidence=confidence,
        )

        self.repository.save(observation)

        return observation