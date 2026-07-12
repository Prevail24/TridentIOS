from datetime import datetime

from core.models.tool_run import ToolRun
from core.repositories.tool_run_repository import ToolRunRepository


class ToolRunService:
    """
    Creates and manages ToolRun records.

    Every scanner or importer should create a ToolRun
    before producing evidence or observations.
    """

    def __init__(self):
        self.repository = ToolRunRepository()

    def create(
        self,
        tool: str,
        target: str,
        mission_id: str | None = None,
        operator: str | None = None,
    ) -> ToolRun:

        run = ToolRun(
            id=self._generate_id(),
            tool=tool,
            target=target,
            mission_id=mission_id,
            operator=operator,
            started=datetime.utcnow(),
            finished=datetime.utcnow(),
            status="completed",
        )

        self.repository.save(run)

        return run

    def get(self, run_id: str) -> ToolRun:
        return self.repository.open(run_id)

    def list(self) -> list[ToolRun]:
        return self.repository.list()

    def _generate_id(self) -> str:
        year = datetime.utcnow().year
        number = len(self.repository.list()) + 1

        return f"RUN-{year}-{number:04d}"