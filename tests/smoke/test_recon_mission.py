import json
from pathlib import Path
from types import SimpleNamespace

from core.command.medusa import Medusa
from core.config import Config
from core.engine import TridentEngine
from core.kernel.mission_context import MissionContext
from core.species.web.serpents import ReconSerpent


NMAP_XML = """<?xml version="1.0" encoding="UTF-8"?>
<nmaprun scanner="nmap">
  <host>
    <status state="up" />
    <address addr="192.0.2.10" addrtype="ipv4" />
    <ports>
      <port protocol="tcp" portid="22">
        <state state="open" />
        <service name="ssh" product="OpenSSH" version="9.6" />
      </port>
      <port protocol="tcp" portid="80">
        <state state="open" />
        <service name="http" product="nginx" version="1.24.0" />
      </port>
    </ports>
  </host>
</nmaprun>
"""


def test_recon_mission_produces_operational_brief(
    monkeypatch,
    tmp_path,
):
    monkeypatch.chdir(tmp_path)

    knowledge_dir = tmp_path / "knowledge"
    monkeypatch.setattr(Config, "KNOWLEDGE_DIR", knowledge_dir)
    monkeypatch.setattr(
        Config,
        "OBSERVATIONS_DIR",
        knowledge_dir / "observations",
    )

    def run_nmap(command, check):
        assert check is True
        assert command[:3] == ["nmap", "-sV", "-oX"]
        assert command[-1] == "192.0.2.10"
        Path(command[3]).write_text(NMAP_XML, encoding="utf-8")

    monkeypatch.setattr(
        "core.adapters.nmap_adapter.subprocess.run",
        run_nmap,
    )

    engine = TridentEngine()
    mission = engine.missions.create(
        title="Vertical Slice Recon",
        mission_type="recon",
        objective="Discover the target's exposed services.",
        scope="192.0.2.10",
    ).mission
    engine.state.set_active_mission(mission.id)

    context = MissionContext()
    wordlist = tmp_path / "content-wordlist.txt"
    wordlist.write_text("admin\n.git\n", encoding="utf-8")
    recon = ReconSerpent(gobuster_wordlist=str(wordlist))
    capability = recon.capabilities()[0]
    weapon = capability.weapons()[0]

    run = weapon.execute(context)
    nmap_brief = Medusa().brief(context)

    assert run.mission_id == mission.id
    assert run.target == "192.0.2.10"
    assert len(run.observations) == 2

    assert context.current_mission().id == mission.id
    assert context.target() == "192.0.2.10"
    assert [port["port"] for port in context.open_ports()] == [22, 80]
    assert {service["service"] for service in context.services()} == {
        "http",
        "ssh",
    }

    assert nmap_brief.mission_id == mission.id
    assert nmap_brief.target == "192.0.2.10"
    assert "web server" in nmap_brief.executive_summary
    assert any(
        "HTTP reconnaissance" in action
        for action in nmap_brief.priority_actions
    )

    def run_httpx(command, check, capture_output, text):
        assert check is True
        assert capture_output is True
        assert text is True
        assert command[:3] == ["httpx", "-u", "192.0.2.10"]

        return SimpleNamespace(
            stdout=json.dumps(
                {
                    "url": "http://192.0.2.10",
                    "host": "192.0.2.10",
                    "host_ip": "192.0.2.10",
                    "port": "80",
                    "scheme": "http",
                    "status_code": 200,
                    "title": "Trident Target",
                    "webserver": "nginx",
                    "tech": ["nginx"],
                }
            )
        )

    monkeypatch.setattr(
        "core.adapters.httpx_adapter.subprocess.run",
        run_httpx,
    )

    technology_discovery = recon.capabilities()[1]
    httpx_weapon = technology_discovery.weapons()[0]
    httpx_result = httpx_weapon.execute(context)
    httpx_brief = Medusa().brief(context)

    assert httpx_result["tool_run"].mission_id == mission.id
    assert len(httpx_result["observations"]) == 1
    assert len(context.runs()) == 2
    assert context.web_surfaces()[0]["url"] == "http://192.0.2.10"

    assert httpx_brief.mission_id == mission.id
    assert httpx_brief.target == "192.0.2.10"

    def run_gobuster(command, check, capture_output, text):
        assert check is True
        assert capture_output is True
        assert text is True
        assert command[:4] == [
            "gobuster",
            "dir",
            "--url",
            "http://192.0.2.10",
        ]
        assert command[4:6] == ["--wordlist", str(wordlist)]

        return SimpleNamespace(
            stdout=(
                "admin (Status: 200) [Size: 512]\n"
                ".git (Status: 403) [Size: 162]\n"
            )
        )

    monkeypatch.setattr(
        "core.adapters.gobuster_adapter.subprocess.run",
        run_gobuster,
    )

    content_discovery = recon.capabilities()[2]
    gobuster_weapon = content_discovery.weapons()[0]
    gobuster_results = gobuster_weapon.execute(context)
    brief = Medusa().brief(context)

    assert len(gobuster_results) == 1
    assert gobuster_results[0]["tool_run"].mission_id == mission.id
    assert len(gobuster_results[0]["observations"]) == 2
    assert len(context.runs()) == 3

    web_paths = [
        observation.data["path"]
        for observation in context.mission_observations()
        if observation.category == "web_path"
    ]
    assert web_paths == ["admin", ".git"]

    assert brief.mission_id == mission.id
    assert brief.target == "192.0.2.10"
    assert brief.council_members == [
        "Hunter",
        "Historian",
        "Skeptic",
        "Oracle",
    ]
    assert "web server" in brief.executive_summary
    assert brief.key_findings
    assert brief.priority_actions
    assert brief.warnings
