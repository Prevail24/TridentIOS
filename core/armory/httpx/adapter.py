import json
import subprocess
from pathlib import Path


class HttpxAdapter:
    """
    Executes ProjectDiscovery httpx and returns parsed JSON records.

    The adapter owns tool execution only.
    It does not create entities, relationships, graphs, or render output.
    """

    def __init__(self, target: str):
        self.target = target

    def execute(self) -> list[dict]:
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

        observations = []

        for line in result.stdout.splitlines():
            line = line.strip()

            if not line:
                continue

            observations.append(json.loads(line))

        return observations