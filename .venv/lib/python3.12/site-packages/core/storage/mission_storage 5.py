

from dataclasses import asdict
from datetime import date
from pathlib import Path
from typing import Any

from core.models.mission import Mission


class MissionStorage:
    """
    Stores active Mission records as Markdown files.

    Storage owns persistence only.
    It does not own mission business logic.
    """

    def __init__(self, root: Path | str = "missions") -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def mission_path(self, mission_id: str) -> Path:
        return self.root / mission_id / "mission.md"

    def workspace_path(self, mission_id: str) -> Path:
        return self.root / mission_id

    def create_workspace(self, mission_id: str) -> Path:
        workspace = self.workspace_path(mission_id)
        workspace.mkdir(parents=True, exist_ok=True)

        for folder in ["notes", "evidence", "screenshots", "reports"]:
            (workspace / folder).mkdir(exist_ok=True)

        for file_name in ["timeline.md", "entities.md", "observations.md", "relationships.md"]:
            file_path = workspace / file_name
            if not file_path.exists():
                title = file_name.replace(".md", "").replace("_", " ").title()
                file_path.write_text(f"# {title}\n", encoding="utf-8")

        return workspace

    def save(self, mission: Mission) -> Path:
        workspace = self.create_workspace(mission.id)
        path = workspace / "mission.md"
        path.write_text(self._to_markdown(mission), encoding="utf-8")
        return path

    def load(self, mission_id: str) -> Mission:
        path = self.mission_path(mission_id)
        if not path.exists():
            raise FileNotFoundError(f"Mission not found: {mission_id}")

        data = self._from_markdown(path.read_text(encoding="utf-8"))
        return Mission(**data)

    def _to_markdown(self, mission: Mission) -> str:
        data = asdict(mission)
        lines = [f"# {mission.title}", "", "## Metadata", ""]

        for key, value in data.items():
            if isinstance(value, date):
                value = value.isoformat()
            lines.append(f"- {key}: {value}")

        lines.extend(["", "## Notes", "", ""])
        return "\n".join(lines)

    def _from_markdown(self, content: str) -> dict[str, Any]:
        data: dict[str, Any] = {}

        for line in content.splitlines():
            if not line.startswith("- "):
                continue

            key, value = line[2:].split(":", 1)
            key = key.strip()
            value = value.strip()

            if key in {"created", "updated"}:
                data[key] = date.fromisoformat(value)
            elif key in {"playbooks", "observations", "entities", "evidence", "relationships", "tags"}:
                data[key] = self._parse_list(value)
            else:
                data[key] = value

        return data

    def _parse_list(self, value: str) -> list[str]:
        value = value.strip()

        if value == "[]":
            return []

        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                return []
            return [item.strip().strip("'\"") for item in inner.split(",")]

        return []