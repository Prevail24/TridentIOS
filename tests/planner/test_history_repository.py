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



def test_round_trips_event_ledger(tmp_path):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    recommendations = [
        {
            "capability_id": "web.recon.technology-discovery",
            "scope": "10.10.11.10",
            "status": "completed",
        }
    ]

    events = [
        {
            "event_id": "EVENT-0001",
            "occurred_at": "2026-07-24T12:00:00+00:00",
            "mission_id": "MIS-2026-0001",
            "capability_id": "web.recon.technology-discovery",
            "scope": "10.10.11.10",
            "previous_status": None,
            "new_status": "accepted",
        },
        {
            "event_id": "EVENT-0002",
            "occurred_at": "2026-07-24T12:01:00+00:00",
            "mission_id": "MIS-2026-0001",
            "capability_id": "web.recon.technology-discovery",
            "scope": "10.10.11.10",
            "previous_status": "accepted",
            "new_status": "completed",
        },
    ]

    filepath = repository.save(
        "MIS-2026-0001",
        recommendations,
        events=events,
    )

    assert repository.load(
        "MIS-2026-0001"
    ) == recommendations

    assert repository.load_events(
        "MIS-2026-0001"
    ) == events

    payload = json.loads(
        filepath.read_text(encoding="utf-8")
    )

    assert payload["events"] == events


def test_legacy_history_without_events_loads_empty_ledger(
    tmp_path,
):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    repository.root.mkdir(
        parents=True,
        exist_ok=True,
    )

    filepath = (
        repository.root
        / "MIS-2026-0001.json"
    )

    filepath.write_text(
        json.dumps(
            {
                "mission_id": "MIS-2026-0001",
                "recommendations": [
                    {
                        "capability_id": (
                            "web.recon.technology-discovery"
                        ),
                        "scope": "10.10.11.10",
                        "status": "completed",
                    }
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    assert repository.load_events(
        "MIS-2026-0001"
    ) == []



def test_save_without_events_preserves_existing_ledger(
    tmp_path,
):
    repository = PlannerHistoryRepository(
        root=tmp_path / "planner_history"
    )

    events = [
        {
            "event_id": "EVENT-0001",
            "occurred_at": "2026-07-24T12:00:00+00:00",
            "mission_id": "MIS-2026-0001",
            "capability_id": "capability.one",
            "scope": "paper.htb",
            "previous_status": None,
            "new_status": "accepted",
        }
    ]

    repository.save(
        "MIS-2026-0001",
        [],
        events=events,
    )

    repository.save(
        "MIS-2026-0001",
        [
            {
                "capability_id": "capability.one",
                "scope": "paper.htb",
                "status": "completed",
            }
        ],
    )

    assert repository.load_events(
        "MIS-2026-0001"
    ) == events
