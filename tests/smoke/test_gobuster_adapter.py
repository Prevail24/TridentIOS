from unittest.mock import patch

from core.armory.gobuster.adapter import GobusterAdapter


adapter = GobusterAdapter(
    target="http://orion.htb",
    wordlist="/tmp/wordlist.txt",
    status_codes_blacklist="302,404",
    threads=5,
)

with patch(
    "core.armory.gobuster.adapter.subprocess.run"
) as mocked_run:
    mocked_run.return_value.stdout = (
        "index.php (Status: 200) [Size: 12272]\n"
    )

    output = adapter.execute()

mocked_run.assert_called_once()

command = mocked_run.call_args.args[0]
options = mocked_run.call_args.kwargs

assert command == [
    "gobuster",
    "dir",
    "--url",
    "http://orion.htb",
    "--wordlist",
    "/tmp/wordlist.txt",
    "--threads",
    "5",
    "--status-codes-blacklist",
    "302,404",
    "--quiet",
    "--no-color",
    "--no-progress",
]

assert options == {
    "check": True,
    "capture_output": True,
    "text": True,
}

assert output == "index.php (Status: 200) [Size: 12272]\n"

print()
print("Gobuster Adapter")
print("-----------------")
print("Command construction: PASS")
