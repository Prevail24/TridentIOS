import pytest

from core.config import Config


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
