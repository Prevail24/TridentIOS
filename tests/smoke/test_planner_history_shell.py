from cli.observer_shell import ObserverShell
from core.config import Config
from core.planner.recommendation import RecommendationStatus
from core.services.state_service import StateService


CAPABILITY_ID = "web.recon.technology-discovery"
SCOPE = "10.10.11.10"
MISSION_ID = "MIS-2026-0001"


def test_shell_reloads_active_mission_planner_history(
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

    first_shell = ObserverShell()

    assert first_shell.planner.history.mission_id == MISSION_ID

    first_shell.planner.history.mark_completed(
        CAPABILITY_ID,
        SCOPE,
    )

    # Simulate closing and restarting the Observer shell.
    second_shell = ObserverShell()

    assert second_shell.planner.history.mission_id == MISSION_ID
    assert (
        second_shell.planner.history.status_for(
            CAPABILITY_ID,
            SCOPE,
        )
        is RecommendationStatus.COMPLETED
    )
