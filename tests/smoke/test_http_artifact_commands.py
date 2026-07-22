from types import SimpleNamespace

from cli.commands.http_artifact import (
    build_upload_url,
    fetch_uploaded_artifact,
)
from cli.observer_shell import ObserverShell


def test_build_upload_url_adds_uploads_path():
    assert (
        build_upload_url(
            "http://research.bedside.htb",
            "case marker.pdf",
        )
        == "http://research.bedside.htb/uploads/case%20marker.pdf"
    )


def test_build_upload_url_defaults_to_http_for_bare_host():
    assert (
        build_upload_url("10.129.36.93", "probe.png")
        == "http://10.129.36.93/uploads/probe.png"
    )


def test_fetch_uploaded_artifact_delegates_to_download(monkeypatch):
    calls = []
    expected = {"tool_run": SimpleNamespace(id="RUN-2026-0001")}

    def fake_fetch_http_artifact(url, *, host_header=None):
        calls.append((url, host_header))
        return expected

    monkeypatch.setattr(
        "cli.commands.http_artifact.fetch_http_artifact",
        fake_fetch_http_artifact,
    )

    result = fetch_uploaded_artifact(
        "http://10.129.36.93",
        "sample.pdf",
        host_header="research.bedside.htb",
    )

    assert result is expected
    assert calls == [
        (
            "http://10.129.36.93/uploads/sample.pdf",
            "research.bedside.htb",
        )
    ]


def test_observer_fetch_upload_updates_context(monkeypatch, capsys):
    observation = SimpleNamespace(
        data={
            "source_url": "http://10.129.36.93/uploads/sample.pdf",
            "filename": "sample.pdf",
            "evidence_path": "knowledge/evidence/http/RUN-sample.pdf",
            "sha256": "a" * 64,
            "size": 12,
            "content_type": "application/pdf",
        }
    )
    result = {
        "tool_run": SimpleNamespace(id="RUN-2026-0002"),
        "observations": [observation],
    }
    calls = []

    def fake_fetch_uploaded_artifact(
        base_url,
        filename,
        *,
        host_header=None,
    ):
        calls.append((base_url, filename, host_header))
        return result

    monkeypatch.setattr(
        "cli.observer_shell.fetch_uploaded_artifact",
        fake_fetch_uploaded_artifact,
    )

    shell = ObserverShell({})
    shell.run_fetch_upload(
        "fetch-upload http://10.129.36.93 sample.pdf --host research.bedside.htb"
    )

    output = capsys.readouterr().out

    assert calls == [
        (
            "http://10.129.36.93",
            "sample.pdf",
            "research.bedside.htb",
        )
    ]
    assert shell.context["http_download_run_id"] == "RUN-2026-0002"
    assert shell.context["http_artifacts"] == 1
    assert "sample.pdf" in output
