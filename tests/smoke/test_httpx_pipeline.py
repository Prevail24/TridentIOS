from types import SimpleNamespace

import core.services.httpx_service as httpx_service_module
import core.species.web.weapons.httpx_weapon as httpx_weapon_module
from core.armory.httpx.sensor import HttpxSensor
from core.services.httpx_service import HttpxService
from core.species.web.weapons import HttpxWeapon


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


def test_httpx_weapon_retries_redirect_hostname_as_host_header(
    monkeypatch,
):
    calls = []

    def observation(data):
        return SimpleNamespace(data=data)

    class StubHttpxSensor:
        def __init__(self, target, *, host_header=None):
            calls.append((target, host_header))
            self.target = target
            self.host_header = host_header

        def collect(self):
            if self.host_header:
                return {
                    "tool_run": SimpleNamespace(id="RUN-vhost"),
                    "observations": [
                        observation(
                            {
                                "url": "http://paperwork.htb",
                                "probe_url": self.target,
                                "host_header": self.host_header,
                                "status_code": 200,
                            }
                        )
                    ],
                    "processed": [],
                }

            return {
                "tool_run": SimpleNamespace(id="RUN-ip"),
                "observations": [
                    observation(
                        {
                            "url": self.target,
                            "status_code": 301,
                            "redirect_location": (
                                "http://paperwork.htb/"
                            ),
                        }
                    )
                ],
                "processed": [],
            }

    monkeypatch.setattr(
        httpx_weapon_module,
        "HttpxSensor",
        StubHttpxSensor,
    )

    context = SimpleNamespace(
        open_ports=lambda: [
            {
                "host": "10.129.59.213",
                "port": 80,
                "service": "http",
            }
        ],
        target=lambda: "10.129.59.213",
    )

    result = HttpxWeapon().execute(context)

    assert calls == [
        ("http://10.129.59.213", None),
        ("http://10.129.59.213", "paperwork.htb"),
    ]
    assert [run.id for run in result["tool_runs"]] == [
        "RUN-ip",
        "RUN-vhost",
    ]
    assert len(result["observations"]) == 2
