from email.message import Message
from types import SimpleNamespace

import pytest

import core.adapters.http_download_adapter as adapter_module
import core.services.http_download_service as service_module
from core.config import Config
from core.engine import TridentEngine
from core.species.web.weapons import HttpDownloadWeapon
from core.services.http_download_service import HttpDownloadService


class FakeHttpResponse:
    status = 200

    def __init__(self, body: bytes):
        self.body = body
        self.headers = Message()
        self.headers["Content-Type"] = "application/zip"
        self.headers[
            "Content-Disposition"
        ] = 'attachment; filename="paperwork-archive-v1.02.zip"'

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def read(self):
        return self.body

    def geturl(self):
        return "http://paperwork.htb/download/archive"


def test_http_download_weapon_requires_operator_url():
    with pytest.raises(RuntimeError, match="operator-selected URL"):
        HttpDownloadWeapon().execute(SimpleNamespace())


def test_http_download_service_preserves_cli_compatibility(monkeypatch):
    expected_result = {
        "tool_run": SimpleNamespace(id="RUN-2026-0001"),
        "observations": [],
        "processed": [],
    }

    class StubHttpDownloadSensor:
        def __init__(self, url, *, host_header=None):
            assert url == "http://paperwork.htb/download/archive"
            assert host_header == "paperwork.htb"

        def collect(self):
            return expected_result

    monkeypatch.setattr(
        service_module,
        "HttpDownloadSensor",
        StubHttpDownloadSensor,
    )

    result = HttpDownloadService().run(
        "http://paperwork.htb/download/archive",
        host_header="paperwork.htb",
    )

    assert result is expected_result


def test_http_download_adapter_stores_artifact_observation(
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

    body = b"paperwork archive bytes"
    requests = []

    def fake_urlopen(request, timeout):
        assert timeout == 20
        requests.append(request)
        return FakeHttpResponse(body)

    monkeypatch.setattr(
        adapter_module,
        "urlopen",
        fake_urlopen,
    )

    engine = TridentEngine()
    mission = engine.missions.create(
        title="Artifact Retrieval",
        mission_type="recon",
        objective="Retrieve linked artifacts.",
        scope="192.0.2.10",
    ).mission
    engine.state.set_active_mission(mission.id)

    result = HttpDownloadWeapon(
        url="http://192.0.2.10/download/archive",
        host_header="paperwork.htb",
    ).execute(SimpleNamespace())

    tool_run = result["tool_run"]
    observation = result["observations"][0]
    data = observation.data

    assert requests[0].get_header("Host") == "paperwork.htb"
    assert tool_run.tool == "http_download"
    assert tool_run.mission_id == mission.id
    assert len(tool_run.evidence) == 1
    assert len(tool_run.observations) == 1

    evidence_path = knowledge_dir / "evidence" / "http"
    stored = next(evidence_path.glob("RUN-*-paperwork-archive-v1.02.zip"))

    assert stored.read_bytes() == body
    assert data == {
        "source_url": "http://192.0.2.10/download/archive",
        "final_url": "http://paperwork.htb/download/archive",
        "host_header": "paperwork.htb",
        "evidence_path": str(stored),
        "filename": "paperwork-archive-v1.02.zip",
        "content_type": "application/zip",
        "size": len(body),
        "sha256": (
            "9f8b19fc614c5f4830087d7fccb305a9"
            "ad8951aa0a4629dda474dfb530f1e039"
        ),
        "status_code": 200,
    }
    assert observation.category == "http_artifact"
    assert observation.evidence_id == str(stored)
