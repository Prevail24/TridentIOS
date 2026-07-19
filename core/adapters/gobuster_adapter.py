import subprocess

from core.adapters.base import ToolAdapter
from core.engine import TridentEngine
from core.parsers.gobuster.parser import GobusterParser
from core.services.gobuster_observation_translator import (
    GobusterObservationTranslator,
)
from core.services.gobuster_vhost_observation_translator import (
    GobusterVhostObservationTranslator,
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
        mode: str = "dir",
        host_header: str | None = None,
        extensions: str | None = None,
        domain: str | None = None,
        append_domain: bool = True,
        status_codes_blacklist: str = "302,404",
        exclude_status: str | None = None,
        threads: int = 10,
    ):
        self.target = target
        self.wordlist = wordlist
        self.mode = mode
        self.host_header = host_header
        self.extensions = extensions
        self.domain = domain
        self.append_domain = append_domain
        self.status_codes_blacklist = status_codes_blacklist
        self.exclude_status = exclude_status
        self.threads = threads
        self.engine = TridentEngine()
        self.parser = GobusterParser()
        self.translator = GobusterObservationTranslator()
        self.vhost_translator = GobusterVhostObservationTranslator()
        self.observation_engine = ObservationEngine()

    def execute(self) -> dict:
        mission_id = self.engine.state.get_active_mission()

        tool_name = (
            "gobuster"
            if self.mode == "dir"
            else f"gobuster-{self.mode}"
        )

        tool_run = self.engine.tool_runs.create(
            tool=tool_name,
            target=self.target,
            mission_id=mission_id,
        )

        if self.mode == "dir":
            command = self._dir_command()
        elif self.mode == "vhost":
            command = self._vhost_command()
        else:
            raise ValueError(f"Unsupported Gobuster mode: {self.mode}")

        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )

        if self.mode == "vhost":
            native_observations = self.parser.parse_vhosts(
                result.stdout,
                base_url=self.target,
            )
            observations = self.vhost_translator.translate(
                native_observations,
                mission_id=mission_id,
                tool_run_id=tool_run.id,
                evidence_id=None,
            )
        else:
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

    def _dir_command(self) -> list[str]:
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

        if self.extensions:
            command.extend(["--extensions", self.extensions])

        return command

    def _vhost_command(self) -> list[str]:
        command = [
            "gobuster",
            "vhost",
            "--url",
            self.target,
            "--wordlist",
            self.wordlist,
            "--threads",
            str(self.threads),
            "--quiet",
            "--no-color",
            "--no-progress",
        ]

        if self.append_domain:
            command.append("--append-domain")

        if self.domain:
            command.extend(["--domain", self.domain])

        if self.exclude_status:
            command.extend(["--exclude-status", self.exclude_status])

        return command
