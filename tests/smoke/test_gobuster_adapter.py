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


def test_gobuster_adapter_adds_extensions_and_host_header(
    monkeypatch,
    tmp_path,
):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(Config, "KNOWLEDGE_DIR", tmp_path / "knowledge")

    wordlist = tmp_path / "wordlist.txt"
    wordlist.write_text("index\n", encoding="utf-8")
    captured = {}

    def run_gobuster(command, **options):
        captured["command"] = command
        return SimpleNamespace(
            stdout="index.php (Status: 200) [Size: 12272]\n"
        )

    monkeypatch.setattr(
        "core.adapters.gobuster_adapter.subprocess.run",
        run_gobuster,
    )

    GobusterAdapter(
        target="http://10.129.36.93",
        wordlist=str(wordlist),
        host_header="research.bedside.htb",
        extensions="php,txt,bak",
    ).execute()

    assert "--headers" in captured["command"]
    assert "Host: research.bedside.htb" in captured["command"]
    assert captured["command"][-2:] == [
        "--extensions",
        "php,txt,bak",
    ]


def test_gobuster_adapter_executes_vhost_pipeline(
    monkeypatch,
    tmp_path,
):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(Config, "KNOWLEDGE_DIR", tmp_path / "knowledge")

    wordlist = tmp_path / "wordlist.txt"
    wordlist.write_text("research\n", encoding="utf-8")
    captured = {}

    def run_gobuster(command, **options):
        captured["command"] = command
        return SimpleNamespace(
            stdout="research.bedside.htb Status: 200 [Size: 3152]\n"
        )

    monkeypatch.setattr(
        "core.adapters.gobuster_adapter.subprocess.run",
        run_gobuster,
    )

    result = GobusterAdapter(
        target="http://10.129.36.93",
        wordlist=str(wordlist),
        mode="vhost",
        domain="bedside.htb",
        exclude_status="301",
        threads=30,
    ).execute()

    assert captured["command"] == [
        "gobuster",
        "vhost",
        "--url",
        "http://10.129.36.93",
        "--wordlist",
        str(wordlist),
        "--threads",
        "30",
        "--quiet",
        "--no-color",
        "--no-progress",
        "--append-domain",
        "--domain",
        "bedside.htb",
        "--exclude-status",
        "301",
    ]
    assert result["tool_run"].tool == "gobuster-vhost"
    assert result["observations"][0].category == "web_vhost"
    assert (
        result["observations"][0].data["hostname"]
        == "research.bedside.htb"
    )
