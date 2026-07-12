import json
from datetime import datetime

from core.models.observation import Observation


class ObservationParser:
    """
    Serializes and parses canonical Trident observations.
    """

    def serialize(self, observation: Observation) -> str:
        return f"""# Observation

## Metadata

- ID: {observation.id}
- Mission: {observation.mission_id}
- ToolRun: {observation.tool_run_id}
- Evidence: {observation.evidence_id}
- Category: {observation.category}
- Confidence: {observation.confidence}
- Observed At: {observation.observed_at.isoformat()}

## Data

```json
{json.dumps(observation.data, indent=2, sort_keys=True)}
```
"""

    def parse(self, markdown: str) -> Observation:
        metadata = {}
        data_lines = []
        in_data = False

        for line in markdown.splitlines():
            stripped = line.strip()

            if stripped == "```json":
                in_data = True
                continue

            if stripped == "```" and in_data:
                in_data = False
                continue

            if in_data:
                data_lines.append(line)
                continue

            if stripped.startswith("- ") and ":" in stripped:
                key, value = stripped[2:].split(":", 1)
                metadata[key.strip()] = value.strip()

        return Observation(
            id=metadata["ID"],
            mission_id=self._none(metadata.get("Mission")),
            tool_run_id=self._none(metadata.get("ToolRun")),
            evidence_id=self._none(metadata.get("Evidence")),
            category=metadata["Category"],
            data=json.loads("\n".join(data_lines)) if data_lines else {},
            confidence=float(metadata.get("Confidence", 1.0)),
            observed_at=datetime.fromisoformat(metadata["Observed At"]),
        )

    def _none(self, value: str | None) -> str | None:
        if not value or value == "None":
            return None

        return value