from cli.observer_shell import ObserverShell
from core.config import Config
from core.services.state_service import StateService


MISSION_ID = "MIS-2026-0001"
TECH_CAPABILITY = "web.recon.technology-discovery"
VHOST_CAPABILITY = "web.recon.virtual-host-discovery"
TARGET_SCOPE = "10.10.11.10"
VHOST_SCOPE = "paper.htb"


def build_shell(
    monkeypatch,
    tmp_path,
):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        Config,
        "KNOWLEDGE_DIR",
        tmp_path / "knowledge",
    )

    StateService().set_active_mission(MISSION_ID)

    return ObserverShell({})


def seed_history(shell):
    shell.planner.history.mark_completed(
        TECH_CAPABILITY,
        TARGET_SCOPE,
    )

    shell.planner.history.mark_failed(
        VHOST_CAPABILITY,
        VHOST_SCOPE,
    )


def test_plan_history_displays_all_entries(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)
    seed_history(shell)

    shell.show_plan_history("plan history")

    output = capsys.readouterr().out

    assert "PLANNER HISTORY" in output
    assert f"Mission : {MISSION_ID}" in output
    assert TECH_CAPABILITY in output
    assert VHOST_CAPABILITY in output
    assert "Status : completed" in output
    assert "Status : failed" in output
    assert f"Scope  : {TARGET_SCOPE}" in output
    assert f"Scope  : {VHOST_SCOPE}" in output


def test_plan_history_filters_by_status(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)
    seed_history(shell)

    shell.show_plan_history(
        "plan history --status failed"
    )

    output = capsys.readouterr().out

    assert "Status  : failed" in output
    assert VHOST_CAPABILITY in output
    assert TECH_CAPABILITY not in output


def test_plan_history_filters_by_scope(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)
    seed_history(shell)

    shell.show_plan_history(
        f"plan history --scope {TARGET_SCOPE}"
    )

    output = capsys.readouterr().out

    assert f"Scope   : {TARGET_SCOPE}" in output
    assert TECH_CAPABILITY in output
    assert VHOST_CAPABILITY not in output


def test_plan_history_combines_filters(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)
    seed_history(shell)

    shell.show_plan_history(
        "plan history "
        "--status completed "
        f"--scope {TARGET_SCOPE}"
    )

    output = capsys.readouterr().out

    assert TECH_CAPABILITY in output
    assert VHOST_CAPABILITY not in output


def test_plan_history_rejects_unknown_status(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)

    shell.show_plan_history(
        "plan history --status vanished"
    )

    output = capsys.readouterr().out

    assert "Unknown Planner status: vanished" in output
    assert "Valid statuses:" in output


def test_plan_history_reports_empty_query(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)

    shell.show_plan_history("plan history")

    output = capsys.readouterr().out

    assert "No Planner history matches this query." in output
