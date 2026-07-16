from core.engine import TridentEngine
from core.parsers.httpx.json_parser import HttpxJsonParser
from core.armory.httpx.sensor import HttpxSensor
from core.services.httpx_observation_translator import (
    HttpxObservationTranslator,
)
from core.services.observation_engine import ObservationEngine


class HttpxService:
    """
    Orchestrates the complete HTTPX observation pipeline.
    """

    def __init__(self):
        self.engine = TridentEngine()
        self.parser = HttpxJsonParser()
        self.translator = HttpxObservationTranslator()
        self.observation_engine = ObservationEngine()

    def run(self, target: str):
        mission_id = self.engine.state.get_active_mission()

        tool_run = self.engine.tool_runs.create(
            tool="httpx",
            target=target,
            mission_id=mission_id,
        )

        sensor = HttpxSensor(target)
        raw_records = sensor.collect()

        native_observations = self.parser.parse(raw_records)

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