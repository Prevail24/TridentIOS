import json
from datetime import UTC, datetime
from pathlib import Path


class CaseManager:
    """Handles creation and management of investigation cases."""

    ROOT = Path("cases")

    def __init__(self):
        self.ROOT.mkdir(exist_ok=True)

    def create_case(self, target: str, run_id: str) -> dict:
        """Create a new investigation case."""

        existing = sorted(self.ROOT.glob("CASE-*"))
        case_number = len(existing) + 1

        case_id = f"CASE-{case_number:04}"

        case_dir = self.ROOT / case_id
        case_dir.mkdir(exist_ok=True)

        mission = {
            "case_id": case_id,
            "target": target,
            "run_id": run_id,
            "status": "ACTIVE",
            "created": datetime.now(UTC).isoformat()
        }

        with open(case_dir / "mission.json", "w") as f:
            json.dump(mission, f, indent=4)

        return mission