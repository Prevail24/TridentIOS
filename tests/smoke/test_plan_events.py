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


def seed_events(shell):
    history = shell.planner.history

    history.mark_accepted(
        TECH_CAPABILITY,
        TARGET_SCOPE,
    )
    history.mark_running(
        TECH_CAPABILITY,
        TARGET_SCOPE,
    )
    history.mark_completed(
        TECH_CAPABILITY,
        TARGET_SCOPE,
    )

    history.mark_accepted(
        VHOST_CAPABILITY,
        VHOST_SCOPE,
    )
    history.mark_failed(
        VHOST_CAPABILITY,
        VHOST_SCOPE,
    )


def test_plan_events_displays_complete_ledger(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)
    seed_events(shell)

    shell.show_plan_events("plan events")

    output = capsys.readouterr().out

    assert "PLANNER EVENTS" in output
    assert f"Mission : {MISSION_ID}" in output
    assert TECH_CAPABILITY in output
    assert VHOST_CAPABILITY in output
    assert "none -> accepted" in output
    assert "accepted -> running" in output
    assert "running -> completed" in output
    assert "accepted -> failed" in output


def test_plan_events_filters_by_new_status(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)
    seed_events(shell)

    shell.show_plan_events(
        "plan events --status failed"
    )

    output = capsys.readouterr().out

    assert "Status  : failed" in output
    assert VHOST_CAPABILITY in output
    assert TECH_CAPABILITY not in output
    assert "accepted -> failed" in output


def test_plan_events_filters_by_scope(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)
    seed_events(shell)

    shell.show_plan_events(
        f"plan events --scope {TARGET_SCOPE}"
    )

    output = capsys.readouterr().out

    assert f"Scope   : {TARGET_SCOPE}" in output
    assert TECH_CAPABILITY in output
    assert VHOST_CAPABILITY not in output


def test_plan_events_latest_selects_newest_events(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)
    seed_events(shell)

    shell.show_plan_events(
        "plan events --latest 2"
    )

    output = capsys.readouterr().out

    assert "Latest  : 2" in output
    assert VHOST_CAPABILITY in output
    assert TECH_CAPABILITY not in output

    assert output.index(
        "none -> accepted"
    ) < output.index(
        "accepted -> failed"
    )


def test_plan_events_combines_filters(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)
    seed_events(shell)

    shell.show_plan_events(
        "plan events "
        "--status completed "
        f"--scope {TARGET_SCOPE} "
        "--latest 1"
    )

    output = capsys.readouterr().out

    assert TECH_CAPABILITY in output
    assert VHOST_CAPABILITY not in output
    assert "running -> completed" in output


def test_plan_events_rejects_unknown_status(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)

    shell.show_plan_events(
        "plan events --status vanished"
    )

    output = capsys.readouterr().out

    assert "Unknown Planner status: vanished" in output
    assert "Valid statuses:" in output


def test_plan_events_rejects_non_integer_latest(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)

    shell.show_plan_events(
        "plan events --latest many"
    )

    output = capsys.readouterr().out

    assert "--latest must be a positive integer." in output


def test_plan_events_rejects_non_positive_latest(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)

    shell.show_plan_events(
        "plan events --latest 0"
    )

    output = capsys.readouterr().out

    assert "--latest must be a positive integer." in output


def test_plan_events_reports_empty_query(
    monkeypatch,
    tmp_path,
    capsys,
):
    shell = build_shell(monkeypatch, tmp_path)

    shell.show_plan_events("plan events")

    output = capsys.readouterr().out

    assert "No Planner events match this query." in output
