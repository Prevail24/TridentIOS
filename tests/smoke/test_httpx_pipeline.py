from types import SimpleNamespace

import core.services.httpx_service as httpx_service_module
from core.armory.httpx.sensor import HttpxSensor
from core.services.httpx_service import HttpxService


def test_httpx_sensor_uses_production_adapter():
    sensor = HttpxSensor("192.0.2.10")

    assert sensor.adapter.__class__.__module__ == "core.adapters.httpx_adapter"


def test_httpx_service_preserves_cli_compatibility(monkeypatch):
    expected_result = {
        "tool_run": SimpleNamespace(id="RUN-2026-0001"),
        "observations": [],
        "processed": [],
    }

    class StubHttpxSensor:
        def __init__(self, target):
            assert target == "192.0.2.10"

        def collect(self):
            return expected_result

    monkeypatch.setattr(
        httpx_service_module,
        "HttpxSensor",
        StubHttpxSensor,
    )

    assert HttpxService().run("192.0.2.10") is expected_result
