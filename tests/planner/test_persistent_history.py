import pytest

from core.planner.history import PlannerHistory
from core.planner.recommendation import RecommendationStatus
from core.repositories.planner_history_repository import (
    PlannerHistoryRepository,
)


CAPABILITY_ID = "web.recon.technology-discovery"
SCOPE = "10.10.11.10"


def test_persistent_history_survives_recreation(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    first_session = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    first_session.mark_completed(
        CAPABILITY_ID,
        SCOPE,
    )

    second_session = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    assert (
        second_session.status_for(CAPABILITY_ID, SCOPE)
        is RecommendationStatus.COMPLETED
    )


def test_persistent_history_keeps_missions_isolated(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    first_mission = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    second_mission = PlannerHistory(
        mission_id="MIS-2026-0002",
        repository=repository,
    )

    first_mission.mark_completed(
        CAPABILITY_ID,
        SCOPE,
    )

    second_mission.mark_failed(
        CAPABILITY_ID,
        SCOPE,
    )

    reloaded_first = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    reloaded_second = PlannerHistory(
        mission_id="MIS-2026-0002",
        repository=repository,
    )

    assert (
        reloaded_first.status_for(CAPABILITY_ID, SCOPE)
        is RecommendationStatus.COMPLETED
    )

    assert (
        reloaded_second.status_for(CAPABILITY_ID, SCOPE)
        is RecommendationStatus.FAILED
    )


def test_clear_removes_persistent_history(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    history = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    history.mark_completed(
        CAPABILITY_ID,
        SCOPE,
    )

    history.clear()

    reloaded = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    assert reloaded.status_for(CAPABILITY_ID, SCOPE) is None


def test_repository_requires_mission_id(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    with pytest.raises(
        ValueError,
        match="mission ID is required",
    ):
        PlannerHistory(repository=repository)
def test_recovers_unfinished_persistent_lifecycle_states(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    history = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    history.mark_accepted(
        "web.recon.technology-discovery",
        "10.10.11.10",
    )

    history.mark_running(
        "web.recon.virtual-host-discovery",
        "paper.htb",
    )

    history.mark_completed(
        "web.recon.content-discovery",
        "http://10.10.11.10",
    )

    assert history.recover_interrupted() == 2

    reloaded = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    assert (
        reloaded.status_for(
            "web.recon.technology-discovery",
            "10.10.11.10",
        )
        is RecommendationStatus.INTERRUPTED
    )

    assert (
        reloaded.status_for(
            "web.recon.virtual-host-discovery",
            "paper.htb",
        )
        is RecommendationStatus.INTERRUPTED
    )

    assert (
        reloaded.status_for(
            "web.recon.content-discovery",
            "http://10.10.11.10",
        )
        is RecommendationStatus.COMPLETED
    )


def test_recovery_is_noop_without_unfinished_work(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    history = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    history.mark_completed(
        CAPABILITY_ID,
        SCOPE,
    )

    assert history.recover_interrupted() == 0


def test_persistent_event_ledger_survives_recreation(
    tmp_path,
):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    first_session = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    first_session.mark_accepted(
        CAPABILITY_ID,
        SCOPE,
    )

    first_session.mark_running(
        CAPABILITY_ID,
        SCOPE,
    )

    expected_events = first_session.events()

    second_session = PlannerHistory(
        mission_id="MIS-2026-0001",
        repository=repository,
    )

    assert second_session.events() == expected_events

    assert all(
        event.mission_id == "MIS-2026-0001"
        for event in second_session.events()
    )
