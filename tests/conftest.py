from pathlib import Path

import pytest

from core.config import Config


TESTS_DIR = Path(__file__).resolve().parent

# These files are legacy manual smoke scripts. They intentionally execute
# diagnostic workflows at module scope and do not define pytest tests.
#
# Pytest must not import them during collection because doing so writes to
# operational knowledge storage before fixtures can isolate the environment.
MANUAL_SMOKE_SCRIPTS = (
    "test_active_mission_service.py",
    "test_archivist.py",
    "test_chronicle_service.py",
    "test_diff_engine.py",
    "test_diff_service.py",
    "test_entity_engine.py",
    "test_entity_resolver.py",
    "test_event_bus.py",
    "test_graph_builder.py",
    "test_historian.py",
    "test_history_service.py",
    "test_host_profile.py",
    "test_hunter.py",
    "test_hunter_events.py",
    "test_knowledge_graph.py",
    "test_loom_repository.py",
    "test_loom_service.py",
    "test_mission_context.py",
    "test_mission_report_service.py",
    "test_nmap_graph_translator.py",
    "test_nmap_parser.py",
    "test_nmap_sensor.py",
    "test_nmap_translator.py",
    "test_observation_emitter.py",
    "test_observation_engine.py",
    "test_observation_event.py",
    "test_oracle.py",
    "test_sensor_registry.py",
    "test_sentinel.py",
    "test_snapshot_diff.py",
    "test_timeline_service.py",
    "test_tool_run_snapshot_service.py",
)

collect_ignore = [
    str(TESTS_DIR / "smoke" / filename)
    for filename in MANUAL_SMOKE_SCRIPTS
]


@pytest.fixture(autouse=True)
def isolate_test_storage(
    monkeypatch,
    tmp_path,
):
    """
    Run every pytest test inside temporary storage.

    This prevents tests from modifying Trident's real knowledge,
    evidence, logs, mission state, or observation directories.
    """
    knowledge_dir = tmp_path / "knowledge"

    monkeypatch.chdir(tmp_path)

    monkeypatch.setattr(
        Config,
        "KNOWLEDGE_DIR",
        knowledge_dir,
    )
    monkeypatch.setattr(
        Config,
        "OBSERVATIONS_DIR",
        knowledge_dir / "observations",
    )
    monkeypatch.setattr(
        Config,
        "LOGS_DIR",
        tmp_path / "logs",
    )
