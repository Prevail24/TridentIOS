from types import SimpleNamespace

import pytest

import core.services.gobuster_service as gobuster_service_module
import core.species.web.weapons.gobuster_weapon as gobuster_weapon_module
from core.services.gobuster_service import GobusterService
from core.species.web.weapons import GobusterWeapon


def test_gobuster_weapon_requires_operator_wordlist():
    context = SimpleNamespace(web_surfaces=lambda: [])

    with pytest.raises(RuntimeError, match="operator-selected wordlist"):
        GobusterWeapon().execute(context)


def test_gobuster_weapon_requires_observed_http_surface():
    context = SimpleNamespace(web_surfaces=lambda: [])

    with pytest.raises(RuntimeError, match="observed HTTP surface"):
        GobusterWeapon(wordlist="wordlist.txt").execute(context)


def test_gobuster_weapon_scans_each_unique_http_surface(monkeypatch):
    collected = []

    class StubGobusterSensor:
        def __init__(self, target, wordlist, **options):
            collected.append((target, wordlist, options))
            self.target = target

        def collect(self):
            return {"target": self.target}

    monkeypatch.setattr(
        gobuster_weapon_module,
        "GobusterSensor",
        StubGobusterSensor,
    )

    context = SimpleNamespace(
        web_surfaces=lambda: [
            {"url": "https://example.test"},
            {"url": "https://example.test"},
            {"url": "http://admin.example.test"},
        ]
    )

    results = GobusterWeapon(
        wordlist="wordlist.txt",
        threads=7,
    ).execute(context)

    assert [result["target"] for result in results] == [
        "https://example.test",
        "http://admin.example.test",
    ]
    assert collected == [
        (
            "https://example.test",
            "wordlist.txt",
            {
                "host_header": None,
                "status_codes_blacklist": "302,404",
                "threads": 7,
            },
        ),
        (
            "http://admin.example.test",
            "wordlist.txt",
            {
                "host_header": None,
                "status_codes_blacklist": "302,404",
                "threads": 7,
            },
        ),
    ]


def test_gobuster_weapon_uses_probe_url_and_host_header(monkeypatch):
    collected = []

    class StubGobusterSensor:
        def __init__(self, target, wordlist, **options):
            collected.append((target, wordlist, options))

        def collect(self):
            return {"ok": True}

    monkeypatch.setattr(
        gobuster_weapon_module,
        "GobusterSensor",
        StubGobusterSensor,
    )

    context = SimpleNamespace(
        web_surfaces=lambda: [
            {
                "url": "http://10.129.59.213",
                "status_code": 301,
                "redirect_location": "http://paperwork.htb/",
            },
            {
                "url": "http://paperwork.htb",
                "probe_url": "http://10.129.59.213",
                "host_header": "paperwork.htb",
                "status_code": 200,
            },
        ]
    )

    results = GobusterWeapon(
        wordlist="wordlist.txt",
    ).execute(context)

    assert results == [{"ok": True}]
    assert collected == [
        (
            "http://10.129.59.213",
            "wordlist.txt",
            {
                "host_header": "paperwork.htb",
                "status_codes_blacklist": "302,404",
                "threads": 10,
            },
        )
    ]


def test_gobuster_service_preserves_cli_compatibility(monkeypatch):
    expected_result = {
        "tool_run": SimpleNamespace(id="RUN-2026-0001"),
        "observations": [],
        "processed": [],
    }

    class StubGobusterSensor:
        def __init__(self, **arguments):
            assert arguments == {
                "target": "https://example.test",
                "wordlist": "wordlist.txt",
                "host_header": None,
                "status_codes_blacklist": "302,404",
                "threads": 10,
            }

        def collect(self):
            return expected_result

    monkeypatch.setattr(
        gobuster_service_module,
        "GobusterSensor",
        StubGobusterSensor,
    )

    result = GobusterService().run(
        target="https://example.test",
        wordlist="wordlist.txt",
    )

    assert result is expected_result
