import json
import subprocess

from core.adapters.base import ToolAdapter
from core.engine import TridentEngine
from core.parsers.httpx.json_parser import HttpxJsonParser
from core.services.httpx_observation_translator import (
    HttpxObservationTranslator,
)
from core.services.observation_engine import ObservationEngine


class HttpxAdapter(ToolAdapter):
    """
    Execute HTTPX and record its output as mission intelligence.
    """

    def __init__(self, target: str):
        self.target = target
        self.engine = TridentEngine()
        self.parser = HttpxJsonParser()
        self.translator = HttpxObservationTranslator()
        self.observation_engine = ObservationEngine()

    def execute(self) -> dict:
        mission_id = self.engine.state.get_active_mission()

        tool_run = self.engine.tool_runs.create(
            tool="httpx",
            target=self.target,
            mission_id=mission_id,
        )

        command = [
            "httpx",
            "-u",
            self.target,
            "-json",
            "-silent",
            "-title",
            "-status-code",
            "-tech-detect",
            "-server",
        ]

        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )

        records = [
            json.loads(line)
            for raw_line in result.stdout.splitlines()
            if (line := raw_line.strip())
        ]
        native_observations = self.parser.parse(records)
        observations = self.translator.translate(
            native_observations,
            mission_id=mission_id,
            tool_run_id=tool_run.id,
            evidence_id=None,
        )

        processed = []

        for observation in observations:
            tool_run.observations.append(observation.id)
            processed.append(
                self.observation_engine.process(observation)
            )

        self.engine.tool_runs.repository.save(tool_run)

        return {
            "tool_run": tool_run,
            "observations": observations,
            "processed": processed,
        }
