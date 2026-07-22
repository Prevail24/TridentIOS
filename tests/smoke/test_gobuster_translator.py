from core.config import Config
from core.models.web_path_observation import WebPathObservation
from core.services.gobuster_observation_translator import (
    GobusterObservationTranslator,
)


def test_gobuster_translator_emits_canonical_observation(
    monkeypatch,
    tmp_path,
):
    monkeypatch.setattr(Config, "KNOWLEDGE_DIR", tmp_path / "knowledge")

    native = [
        WebPathObservation(
            base_url="http://orion.htb",
            path=".git",
            url="http://orion.htb/.git",
            status_code=403,
            content_length=162,
            redirect_location=None,
        )
    ]

    canonical = GobusterObservationTranslator().translate(
        native,
        mission_id="MISSION-SMOKE",
        tool_run_id="RUN-SMOKE",
        evidence_id=None,
    )

    assert len(canonical) == 1

    observation = canonical[0]

    assert observation.category == "web_path"
    assert observation.mission_id == "MISSION-SMOKE"
    assert observation.tool_run_id == "RUN-SMOKE"
    assert observation.confidence == 1.0
    assert observation.data == {
        "base_url": "http://orion.htb",
        "path": ".git",
        "url": "http://orion.htb/.git",
        "status_code": 403,
        "content_length": 162,
        "redirect_location": None,
    }
