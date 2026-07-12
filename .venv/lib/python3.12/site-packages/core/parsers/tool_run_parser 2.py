from datetime import datetime

from core.models.tool_run import ToolRun


class ToolRunParser:
    def serialize(self, run: ToolRun) -> str:
        return f"""# Tool Run

## Metadata

- ID: {run.id}
- Tool: {run.tool}
- Target: {run.target}
- Mission: {run.mission_id}
- Status: {run.status}
- Started: {run.started.isoformat()}
- Finished: {run.finished.isoformat()}
- Operator: {run.operator}

## Evidence

{self._list(run.evidence)}

## Observations

{self._list(run.observations)}

## Entities

{self._list(run.entities)}

## Notes

{run.notes}
"""

    def parse(self, markdown: str) -> ToolRun:
        metadata = {}
        current = None

        evidence = []
        observations = []
        entities = []
        notes = []

        for line in markdown.splitlines():
            line = line.rstrip()

            if line.startswith("## "):
                current = line[3:].strip().lower()
                continue

            if current == "metadata" and line.startswith("- "):
                key, value = line[2:].split(":", 1)
                metadata[key.strip()] = value.strip()
                continue

            if line.startswith("* "):
                value = line[2:].strip()

                if value == "None":
                    continue

                if current == "evidence":
                    evidence.append(value)
                elif current == "observations":
                    observations.append(value)
                elif current == "entities":
                    entities.append(value)

                continue

            if current == "notes":
                notes.append(line)

        return ToolRun(
            id=metadata["ID"],
            tool=metadata["Tool"],
            target=metadata["Target"],
            mission_id=self._none(metadata.get("Mission")),
            status=metadata.get("Status", "completed"),
            started=datetime.fromisoformat(metadata["Started"]),
            finished=datetime.fromisoformat(metadata["Finished"]),
            operator=self._none(metadata.get("Operator")),
            evidence=evidence,
            observations=observations,
            entities=entities,
            notes="\n".join(notes).strip(),
        )

    def _list(self, values: list[str]) -> str:
        if not values:
            return "* None"

        return "\n".join(f"* {item}" for item in values)

    def _none(self, value: str | None) -> str | None:
        if not value or value == "None":
            return None

        return value