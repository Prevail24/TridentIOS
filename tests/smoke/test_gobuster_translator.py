from core.models.web_path_observation import WebPathObservation
from core.services.gobuster_observation_translator import (
    GobusterObservationTranslator,
)


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

translator = GobusterObservationTranslator()

canonical = translator.translate(
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

print()
print("Gobuster Translator")
print("--------------------")
print(f"Observation: {observation.id}")
print(f"Category: {observation.category}")
print("PASS")
