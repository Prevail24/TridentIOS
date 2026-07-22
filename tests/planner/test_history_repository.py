import json

import pytest

from core.repositories.planner_history_repository import (
    PlannerHistoryRepository,
)


def test_missing_mission_history_is_empty(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    assert repository.load("MIS-2026-0001") == []


def test_round_trips_mission_history(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    records = [
        {
            "capability_id": "web.recon.technology-discovery",
            "scope": "10.10.11.10",
            "status": "completed",
        },
        {
            "capability_id": "web.recon.virtual-host-discovery",
            "scope": "paper.htb",
            "status": "failed",
        },
    ]

    filepath = repository.save(
        "MIS-2026-0001",
        records,
    )

    assert filepath.exists()
    assert repository.load("MIS-2026-0001") == records

    payload = json.loads(
        filepath.read_text(encoding="utf-8")
    )

    assert payload["mission_id"] == "MIS-2026-0001"
    assert payload["recommendations"] == records


def test_keeps_mission_histories_isolated(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    repository.save(
        "MIS-2026-0001",
        [
            {
                "capability_id": "web.recon.technology-discovery",
                "scope": "10.10.11.10",
                "status": "completed",
            }
        ],
    )

    repository.save(
        "MIS-2026-0002",
        [
            {
                "capability_id": "web.recon.technology-discovery",
                "scope": "10.10.11.10",
                "status": "failed",
            }
        ],
    )

    first = repository.load("MIS-2026-0001")
    second = repository.load("MIS-2026-0002")

    assert first[0]["status"] == "completed"
    assert second[0]["status"] == "failed"


def test_clear_removes_only_selected_mission(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    repository.save(
        "MIS-2026-0001",
        [
            {
                "capability_id": "web.recon.technology-discovery",
                "scope": "10.10.11.10",
                "status": "completed",
            }
        ],
    )

    repository.save(
        "MIS-2026-0002",
        [
            {
                "capability_id": "web.recon.technology-discovery",
                "scope": "10.10.11.11",
                "status": "completed",
            }
        ],
    )

    repository.clear("MIS-2026-0001")

    assert repository.load("MIS-2026-0001") == []
    assert repository.load("MIS-2026-0002") != []


def test_rejects_path_traversal_mission_id(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    with pytest.raises(
        ValueError,
        match="path separators",
    ):
        repository.load("../outside")
