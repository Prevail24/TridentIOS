from types import SimpleNamespace

import pytest

import core.species.web.weapons.nmap_weapon as nmap_weapon_module
from core.armory.nmap.sensor import NmapSensor
from core.kernel.mission_context import MissionContext
from core.species.web.capabilities import ServiceDiscoveryCapability
from core.species.web.serpents import ReconSerpent
from core.species.web.weapons import NmapWeapon


def test_mission_context_opens_active_mission(monkeypatch):
    context = MissionContext.__new__(MissionContext)
    mission = SimpleNamespace(scope="scanme.nmap.org")
    context.missions = SimpleNamespace(open=lambda mission_id: mission)

    monkeypatch.setattr(context, "require_mission_id", lambda: "MIS-2026-0001")

    assert context.current_mission() is mission


def test_mission_context_resolves_active_mission_target(monkeypatch):
    context = MissionContext.__new__(MissionContext)
    mission = SimpleNamespace(scope="  scanme.nmap.org  ")

    monkeypatch.setattr(context, "current_mission", lambda: mission)

    assert context.target() == "scanme.nmap.org"


def test_mission_context_rejects_empty_target(monkeypatch):
    context = MissionContext.__new__(MissionContext)
    mission = SimpleNamespace(scope="   ")

    monkeypatch.setattr(context, "current_mission", lambda: mission)

    with pytest.raises(RuntimeError, match="no operational target"):
        context.target()


def test_recon_serpent_delegates_nmap_execution_to_sensor(monkeypatch):
    collected = {}
    expected_run = object()

    class StubNmapSensor:
        def __init__(self, target):
            collected["target"] = target

        def collect(self):
            collected["called"] = True
            return expected_run

    monkeypatch.setattr(nmap_weapon_module, "NmapSensor", StubNmapSensor)

    serpent = ReconSerpent()
    capability = serpent.capabilities()[0]
    weapon = capability.weapons()[0]
    context = SimpleNamespace(target=lambda: "scanme.nmap.org")

    result = weapon.execute(context)

    assert isinstance(capability, ServiceDiscoveryCapability)
    assert isinstance(weapon, NmapWeapon)
    assert collected == {
        "target": "scanme.nmap.org",
        "called": True,
    }
    assert result is expected_run


def test_nmap_sensor_uses_production_adapter():
    sensor = NmapSensor("scanme.nmap.org")

    assert sensor.adapter.__class__.__module__ == "core.adapters.nmap_adapter"
