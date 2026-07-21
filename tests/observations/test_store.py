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

def test_find_combines_type_and_scope_filters():
    store = ObservationStore()

    expected = make_observation(
        ObservationType.HOSTNAME,
        "paper.htb",
        scope="10.10.11.143",
    )

    wrong_type = make_observation(
        ObservationType.PORT,
        "80",
        scope="10.10.11.143",
    )

    wrong_scope = make_observation(
        ObservationType.HOSTNAME,
        "admin.paper.htb",
        scope="10.10.11.200",
    )

    store.add(expected)
    store.add(wrong_type)
    store.add(wrong_scope)

    assert store.find(
        observation_type=ObservationType.HOSTNAME,
        scope="10.10.11.143",
    ) == (expected,)


def test_find_can_filter_by_value():
    store = ObservationStore()

    port_80 = make_observation(
        ObservationType.PORT,
        "80",
    )

    port_443 = make_observation(
        ObservationType.PORT,
        "443",
    )

    store.add(port_80)
    store.add(port_443)

    assert store.find(
        observation_type=ObservationType.PORT,
        value="80",
        scope="paper.htb",
    ) == (port_80,)


def test_find_returns_empty_tuple_when_nothing_matches():
    store = ObservationStore()

    assert store.find(
        observation_type=ObservationType.HOSTNAME,
        scope="missing.htb",
    ) == ()


def test_exists_returns_true_for_matching_observation():
    store = ObservationStore()

    store.add(
        make_observation(
            ObservationType.PORT,
            "80",
        )
    )

    assert store.exists(
        observation_type=ObservationType.PORT,
        value="80",
        scope="paper.htb",
    )


def test_exists_returns_false_when_nothing_matches():
    store = ObservationStore()

    assert not store.exists(
        observation_type=ObservationType.TECHNOLOGY,
        value="Apache",
        scope="paper.htb",
    )


def test_find_can_explicitly_match_unscoped_observations():
    store = ObservationStore()

    unscoped = make_observation(
        ObservationType.HOSTNAME,
        "paper.htb",
        scope=None,
    )

    scoped = make_observation(
        ObservationType.HOSTNAME,
        "admin.paper.htb",
        scope="10.10.11.143",
    )

    store.add(unscoped)
    store.add(scoped)

    assert store.find(scope=None) == (unscoped,)