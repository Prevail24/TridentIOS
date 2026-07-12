from dataclasses import asdict
from pathlib import Path
from typing import Any

from core.models.entity import Entity


class EntityStorage:
    """
    Stores Entity records as Markdown files.

    Storage owns persistence only.
    """

    def __init__(self, root: Path | str = "knowledge/entities") -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def entity_path(self, entity_id: str) -> Path:
        return self.root / f"{entity_id}.md"

    def save(self, entity: Entity) -> Path:
        path = self.entity_path(entity.id)
        path.write_text(self._to_markdown(entity), encoding="utf-8")
        return path

    def load(self, entity_id: str) -> Entity:
        path = self.entity_path(entity_id)
        if not path.exists():
            raise FileNotFoundError(f"Entity not found: {entity_id}")

        data = self._from_markdown(path.read_text(encoding="utf-8"))
        return Entity(**data)

    def list(self) -> list[Entity]:
        entities = []

        for path in sorted(self.root.glob("ENT-*.md")):
            entities.append(self.load(path.stem))

        return entities

    def _to_markdown(self, entity: Entity) -> str:
        data = asdict(entity)

        lines = [
            f"# {entity.label}",
            "",
            "## Metadata",
            "",
        ]

        for key, value in data.items():
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

            if key in {"observations", "evidence", "tags"}:
                data[key] = self._parse_list(value)
            elif key == "confidence":
                data[key] = float(value)
            elif value == "None":
                data[key] = None
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