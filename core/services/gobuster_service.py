from core.armory.gobuster.sensor import GobusterSensor
from core.engine import TridentEngine
from core.services.gobuster_observation_translator import (
    GobusterObservationTranslator,
)
from core.services.observation_engine import ObservationEngine


class GobusterService:
    """
    Orchestrates the complete Gobuster observation pipeline.
    """

    def __init__(self):
        self.engine = TridentEngine()
        self.translator = GobusterObservationTranslator()
        self.observation_engine = ObservationEngine()

    def run(
        self,
        target: str,
        wordlist: str,
        *,
        status_codes_blacklist: str = "302,404",
        threads: int = 10,
    ):
        mission_id = self.engine.state.get_active_mission()

        tool_run = self.engine.tool_runs.create(
            tool="gobuster",
            target=target,
            mission_id=mission_id,
        )

        sensor = GobusterSensor(
            target=target,
            wordlist=wordlist,
            status_codes_blacklist=status_codes_blacklist,
            threads=threads,
        )

        raw_output = sensor.collect()
        native_observations = sensor.normalize(raw_output)

        canonical_observations = self.translator.translate(
            native_observations,
            mission_id=mission_id,
            tool_run_id=tool_run.id,
            evidence_id=None,
        )

        processed = []

        for observation in canonical_observations:
            tool_run.observations.append(observation.id)

            processed.append(
                self.observation_engine.process(observation)
            )

        self.engine.tool_runs.repository.save(tool_run)

        return {
            "tool_run": tool_run,
            "observations": canonical_observations,
            "processed": processed,
        }
