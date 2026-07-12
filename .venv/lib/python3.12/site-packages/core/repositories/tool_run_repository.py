from pathlib import Path

from core.config import Config
from core.models.tool_run import ToolRun
from core.parsers.tool_run_parser import ToolRunParser


class ToolRunRepository:
    def __init__(self):
        self.parser = ToolRunParser()

    def save(self, run: ToolRun) -> Path:
        runs_root = Config.KNOWLEDGE_DIR / "tool_runs"
        runs_root.mkdir(parents=True, exist_ok=True)

        filepath = runs_root / f"{run.id}.md"
        filepath.write_text(
            self.parser.serialize(run),
            encoding="utf-8",
        )

        return filepath

    def open(self, run_id: str) -> ToolRun:
        filepath = Config.KNOWLEDGE_DIR / "tool_runs" / f"{run_id}.md"
        markdown = filepath.read_text(encoding="utf-8")
        return self.parser.parse(markdown)

    def list(self) -> list[ToolRun]:
        runs_root = Config.KNOWLEDGE_DIR / "tool_runs"
        runs_root.mkdir(parents=True, exist_ok=True)

        runs = []

        for file in sorted(runs_root.glob("RUN-*.md")):
            runs.append(self.open(file.stem))

        return runs