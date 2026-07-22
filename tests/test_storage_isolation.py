from pathlib import Path

from core.config import Config
from core.services.active_mission_service import (
    ActiveMissionService,
)
from core.services.state_service import StateService


def test_storage_is_redirected_to_temporary_directory(
    tmp_path,
):
    assert Path.cwd() == tmp_path

    assert Config.KNOWLEDGE_DIR == (
        tmp_path / "knowledge"
    )
    assert Config.OBSERVATIONS_DIR == (
        tmp_path / "knowledge" / "observations"
    )
    assert Config.LOGS_DIR == (
        tmp_path / "logs"
    )

    assert Config.KNOWLEDGE_DIR != (
        Config.ROOT_DIR / "knowledge"
    )


def test_relative_runtime_state_is_also_isolated(
    tmp_path,
):
    state = StateService()

    assert state.state_dir.resolve() == (
        tmp_path / ".state"
    ).resolve()

    assert (
        ActiveMissionService.CURRENT_FILE.resolve()
        == (
            tmp_path
            / "knowledge"
            / "mission"
            / "current"
        ).resolve()
    )
