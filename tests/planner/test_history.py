from core.planner.history import PlannerHistory
from core.planner.recommendation import RecommendationStatus


CAPABILITY_ID = "web.recon.technology-discovery"
SCOPE = "paper.htb"


def test_history_initially_empty():
    history = PlannerHistory()

    assert history.status_for(
        CAPABILITY_ID,
        SCOPE,
    ) is None

    assert not history.has_completed(
        CAPABILITY_ID,
        SCOPE,
    )


def test_mark_accepted():
    history = PlannerHistory()

    history.mark_accepted(
        CAPABILITY_ID,
        SCOPE,
    )

    assert (
        history.status_for(CAPABILITY_ID, SCOPE)
        is RecommendationStatus.ACCEPTED
    )

    assert not history.has_completed(
        CAPABILITY_ID,
        SCOPE,
    )


def test_lifecycle_can_advance_to_running_and_completed():
    history = PlannerHistory()

    history.mark_accepted(
        CAPABILITY_ID,
        SCOPE,
    )

    history.mark_running(
        CAPABILITY_ID,
        SCOPE,
    )

    assert (
        history.status_for(CAPABILITY_ID, SCOPE)
        is RecommendationStatus.RUNNING
    )

    history.mark_completed(
        CAPABILITY_ID,
        SCOPE,
    )

    assert (
        history.status_for(CAPABILITY_ID, SCOPE)
        is RecommendationStatus.COMPLETED
    )

    assert history.has_completed(
        CAPABILITY_ID,
        SCOPE,
    )


def test_mark_failed():
    history = PlannerHistory()

    history.mark_running(
        CAPABILITY_ID,
        SCOPE,
    )

    history.mark_failed(
        CAPABILITY_ID,
        SCOPE,
    )

    assert (
        history.status_for(CAPABILITY_ID, SCOPE)
        is RecommendationStatus.FAILED
    )

    assert not history.has_completed(
        CAPABILITY_ID,
        SCOPE,
    )


def test_scope_is_part_of_identity():
    history = PlannerHistory()

    history.mark_completed(
        CAPABILITY_ID,
        SCOPE,
    )

    assert not history.has_completed(
        CAPABILITY_ID,
        "10.10.11.143",
    )


def test_multiple_capabilities():
    history = PlannerHistory()

    history.mark_completed(
        "capability.one",
        SCOPE,
    )

    history.mark_failed(
        "capability.two",
        SCOPE,
    )

    assert history.has_completed(
        "capability.one",
        SCOPE,
    )

    assert (
        history.status_for(
            "capability.two",
            SCOPE,
        )
        is RecommendationStatus.FAILED
    )


def test_clear_history():
    history = PlannerHistory()

    history.mark_completed(
        CAPABILITY_ID,
        SCOPE,
    )

    history.clear()

    assert history.status_for(
        CAPABILITY_ID,
        SCOPE,
    ) is None

def test_entries_returns_sorted_read_only_snapshot():
    history = PlannerHistory()

    history.mark_completed(
        "web.recon.virtual-host-discovery",
        "paper.htb",
    )

    history.mark_failed(
        "web.recon.technology-discovery",
        "10.10.11.10",
    )

    entries = history.entries()

    assert isinstance(entries, tuple)
    assert len(entries) == 2

    assert (
        entries[0].capability_id
        == "web.recon.technology-discovery"
    )
    assert entries[0].scope == "10.10.11.10"
    assert entries[0].status is RecommendationStatus.FAILED

    assert (
        entries[1].capability_id
        == "web.recon.virtual-host-discovery"
    )
    assert entries[1].scope == "paper.htb"
    assert entries[1].status is RecommendationStatus.COMPLETED


def test_entries_filters_by_status():
    history = PlannerHistory()

    history.mark_completed(
        "web.recon.technology-discovery",
        "10.10.11.10",
    )

    history.mark_failed(
        "web.recon.virtual-host-discovery",
        "paper.htb",
    )

    entries = history.entries(
        status=RecommendationStatus.FAILED,
    )

    assert len(entries) == 1
    assert (
        entries[0].capability_id
        == "web.recon.virtual-host-discovery"
    )
    assert entries[0].status is RecommendationStatus.FAILED


def test_entries_filters_by_scope():
    history = PlannerHistory()

    history.mark_completed(
        "web.recon.technology-discovery",
        "10.10.11.10",
    )

    history.mark_status(
        "web.recon.virtual-host-discovery",
        "paper.htb",
        RecommendationStatus.INTERRUPTED,
    )

    entries = history.entries(
        scope="paper.htb",
    )

    assert len(entries) == 1
    assert (
        entries[0].capability_id
        == "web.recon.virtual-host-discovery"
    )
    assert entries[0].scope == "paper.htb"
    assert entries[0].status is RecommendationStatus.INTERRUPTED


def test_event_ledger_records_lifecycle_transitions():
    history = PlannerHistory()

    history.mark_accepted(CAPABILITY_ID, SCOPE)
    history.mark_running(CAPABILITY_ID, SCOPE)
    history.mark_completed(CAPABILITY_ID, SCOPE)

    events = history.events()

    assert isinstance(events, tuple)
    assert len(events) == 3

    assert events[0].previous_status is None
    assert (
        events[0].new_status
        is RecommendationStatus.ACCEPTED
    )

    assert (
        events[1].previous_status
        is RecommendationStatus.ACCEPTED
    )
    assert (
        events[1].new_status
        is RecommendationStatus.RUNNING
    )

    assert (
        events[2].previous_status
        is RecommendationStatus.RUNNING
    )
    assert (
        events[2].new_status
        is RecommendationStatus.COMPLETED
    )

    assert all(
        event.occurred_at.tzinfo is not None
        for event in events
    )

    assert len(
        {event.event_id for event in events}
    ) == 3


def test_repeating_current_status_does_not_duplicate_event():
    history = PlannerHistory()

    history.mark_accepted(CAPABILITY_ID, SCOPE)
    history.mark_accepted(CAPABILITY_ID, SCOPE)

    assert len(history.events()) == 1


def test_recovery_appends_interrupted_events():
    history = PlannerHistory()

    history.mark_accepted(
        "capability.one",
        "10.10.11.10",
    )

    history.mark_running(
        "capability.two",
        "paper.htb",
    )

    original_event_count = len(history.events())

    assert history.recover_interrupted() == 2

    recovery_events = history.events()[
        original_event_count:
    ]

    assert len(recovery_events) == 2

    assert {
        event.previous_status
        for event in recovery_events
    } == {
        RecommendationStatus.ACCEPTED,
        RecommendationStatus.RUNNING,
    }

    assert all(
        event.new_status
        is RecommendationStatus.INTERRUPTED
        for event in recovery_events
    )
