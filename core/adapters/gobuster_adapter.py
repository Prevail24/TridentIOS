import subprocess

from core.adapters.base import ToolAdapter
from core.engine import TridentEngine
from core.parsers.gobuster.parser import GobusterParser
from core.services.gobuster_observation_translator import (
    GobusterObservationTranslator,
)
from core.services.observation_engine import ObservationEngine


class GobusterAdapter(ToolAdapter):
    """
    Execute Gobuster and record discovered paths as mission intelligence.
    """

    def __init__(
        self,
        target: str,
        wordlist: str,
        *,
        host_header: str | None = None,
        status_codes_blacklist: str = "302,404",
        threads: int = 10,
    ):
        self.target = target
        self.wordlist = wordlist
        self.host_header = host_header
        self.status_codes_blacklist = status_codes_blacklist
        self.threads = threads
        self.engine = TridentEngine()
        self.parser = GobusterParser()
        self.translator = GobusterObservationTranslator()
        self.observation_engine = ObservationEngine()

    def execute(self) -> dict:
        mission_id = self.engine.state.get_active_mission()

        tool_run = self.engine.tool_runs.create(
            tool="gobuster",
            target=self.target,
            mission_id=mission_id,
        )

        command = [
            "gobuster",
            "dir",
            "--url",
            self.target,
            "--wordlist",
            self.wordlist,
            "--threads",
            str(self.threads),
            "--status-codes-blacklist",
            self.status_codes_blacklist,
            "--quiet",
            "--no-color",
            "--no-progress",
        ]

        if self.host_header:
            command.extend(["--headers", f"Host: {self.host_header}"])

        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )

        native_observations = self.parser.parse(
            result.stdout,
            base_url=self.target,
        )
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
