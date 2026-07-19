from types import SimpleNamespace

from core.adapters.gobuster_adapter import GobusterAdapter
from core.config import Config


def test_gobuster_adapter_executes_observation_pipeline(
    monkeypatch,
    tmp_path,
):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(Config, "KNOWLEDGE_DIR", tmp_path / "knowledge")

    wordlist = tmp_path / "wordlist.txt"
    wordlist.write_text("index.php\n", encoding="utf-8")
    captured = {}

    def run_gobuster(command, **options):
        captured["command"] = command
        captured["options"] = options
        return SimpleNamespace(
            stdout="index.php (Status: 200) [Size: 12272]\n"
        )

    monkeypatch.setattr(
        "core.adapters.gobuster_adapter.subprocess.run",
        run_gobuster,
    )

    result = GobusterAdapter(
        target="http://orion.htb",
        wordlist=str(wordlist),
        status_codes_blacklist="302,404",
        threads=5,
    ).execute()

    assert captured["command"] == [
        "gobuster",
        "dir",
        "--url",
        "http://orion.htb",
        "--wordlist",
        str(wordlist),
        "--threads",
        "5",
        "--status-codes-blacklist",
        "302,404",
        "--quiet",
        "--no-color",
        "--no-progress",
    ]
    assert captured["options"] == {
        "check": True,
        "capture_output": True,
        "text": True,
    }
    assert result["tool_run"].tool == "gobuster"
    assert result["observations"][0].data["path"] == "index.php"
    assert len(result["processed"]) == 1
