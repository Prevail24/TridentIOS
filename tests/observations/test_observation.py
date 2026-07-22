from dataclasses import FrozenInstanceError

import pytest

from core.observations import Observation, ObservationType


def test_observation_creation():
    observation = Observation(
        type=ObservationType.HOSTNAME,
        value="paper.htb",
        source="web.recon.virtual-host-discovery",
        scope="10.10.11.143",
    )

    assert observation.type is ObservationType.HOSTNAME
    assert observation.value == "paper.htb"
    assert observation.source == "web.recon.virtual-host-discovery"
    assert observation.scope == "10.10.11.143"


def test_scope_is_optional():
    observation = Observation(
        type=ObservationType.TECHNOLOGY,
        value="Apache",
        source="web.recon.technology-discovery",
    )

    assert observation.scope is None


def test_equal_observations_have_value_equality():
    first = Observation(
        type=ObservationType.PORT,
        value="80",
        source="network.port-scan",
        scope="10.10.11.143",
    )

    second = Observation(
        type=ObservationType.PORT,
        value="80",
        source="network.port-scan",
        scope="10.10.11.143",
    )

    assert first == second


def test_observation_is_immutable():
    observation = Observation(
        type=ObservationType.HOSTNAME,
        value="paper.htb",
        source="web.recon.virtual-host-discovery",
    )

    with pytest.raises(FrozenInstanceError):
        observation.value = "changed.htb"


def test_observation_type_behaves_like_string():
    observation_type = ObservationType.HOSTNAME

    assert observation_type == "hostname"
    assert str(observation_type) == "hostname"
    assert observation_type.value == "hostname"