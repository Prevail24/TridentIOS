from core.planner.history import PlannerHistory


def test_history_initially_empty():
    history = PlannerHistory()

    assert not history.has_completed(
        "web.recon.technology-discovery",
        "paper.htb",
    )


def test_mark_completed():
    history = PlannerHistory()

    history.mark_completed(
        "web.recon.technology-discovery",
        "paper.htb",
    )

    assert history.has_completed(
        "web.recon.technology-discovery",
        "paper.htb",
    )


def test_scope_is_part_of_identity():
    history = PlannerHistory()

    history.mark_completed(
        "web.recon.technology-discovery",
        "paper.htb",
    )

    assert not history.has_completed(
        "web.recon.technology-discovery",
        "10.10.11.143",
    )


def test_multiple_capabilities():
    history = PlannerHistory()

    history.mark_completed(
        "capability.one",
        "paper.htb",
    )

    history.mark_completed(
        "capability.two",
        "paper.htb",
    )

    assert history.has_completed(
        "capability.one",
        "paper.htb",
    )

    assert history.has_completed(
        "capability.two",
        "paper.htb",
    )


def test_clear_history():
    history = PlannerHistory()

    history.mark_completed(
        "capability.one",
        "paper.htb",
    )

    history.clear()

    assert not history.has_completed(
        "capability.one",
        "paper.htb",
    )