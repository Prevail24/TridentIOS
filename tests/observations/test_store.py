from core.observations import (
    Observation,
    ObservationStore,
    ObservationType,
)


def make_observation(
    observation_type: ObservationType,
    value: str,
    scope: str | None = "paper.htb",
) -> Observation:
    return Observation(
        type=observation_type,
        value=value,
        source="test-capability",
        scope=scope,
    )


def test_store_is_initially_empty():
    store = ObservationStore()

    assert len(store) == 0
    assert store.all() == ()


def test_add_observation():
    store = ObservationStore()
    observation = make_observation(
        ObservationType.HOSTNAME,
        "paper.htb",
    )

    added = store.add(observation)

    assert added is True
    assert len(store) == 1
    assert store.all() == (observation,)
    assert store.contains(observation)


def test_exact_duplicate_is_not_added_twice():
    store = ObservationStore()
    observation = make_observation(
        ObservationType.PORT,
        "80",
    )

    first_add = store.add(observation)
    second_add = store.add(observation)

    assert first_add is True
    assert second_add is False
    assert len(store) == 1


def test_store_preserves_discovery_order():
    store = ObservationStore()

    hostname = make_observation(
        ObservationType.HOSTNAME,
        "paper.htb",
    )

    port = make_observation(
        ObservationType.PORT,
        "80",
    )

    technology = make_observation(
        ObservationType.TECHNOLOGY,
        "Apache",
    )

    store.add(hostname)
    store.add(port)
    store.add(technology)

    assert store.all() == (
        hostname,
        port,
        technology,
    )


def test_find_by_type():
    store = ObservationStore()

    hostname = make_observation(
        ObservationType.HOSTNAME,
        "paper.htb",
    )

    technology = make_observation(
        ObservationType.TECHNOLOGY,
        "Apache",
    )

    store.add(hostname)
    store.add(technology)

    assert store.find_by_type(
        ObservationType.HOSTNAME
    ) == (hostname,)


def test_find_by_scope():
    store = ObservationStore()

    first = make_observation(
        ObservationType.PORT,
        "80",
        scope="paper.htb",
    )

    second = make_observation(
        ObservationType.PORT,
        "443",
        scope="admin.paper.htb",
    )

    store.add(first)
    store.add(second)

    assert store.find_by_scope(
        "paper.htb"
    ) == (first,)


def test_clear_removes_all_observations():
    store = ObservationStore()

    observation = make_observation(
        ObservationType.HOSTNAME,
        "paper.htb",
    )

    store.add(observation)
    store.clear()

    assert len(store) == 0
    assert store.all() == ()
    assert not store.contains(observation)