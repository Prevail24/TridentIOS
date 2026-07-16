import subprocess


class GobusterAdapter:
    """
    Executes Gobuster directory enumeration and returns raw stdout.

    The adapter owns tool execution only.
    It does not create canonical observations or perform reasoning.
    """

    def __init__(
        self,
        target: str,
        wordlist: str,
        *,
        status_codes_blacklist: str = "302,404",
        threads: int = 10,
    ):
        self.target = target
        self.wordlist = wordlist
        self.status_codes_blacklist = status_codes_blacklist
        self.threads = threads

    def execute(self) -> str:
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

        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )

        return result.stdout
