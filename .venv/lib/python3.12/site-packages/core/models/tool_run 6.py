from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ToolRun:
    """
    Records the execution of a reconnaissance or intelligence tool.

    ToolRuns generate evidence and observations.
    They do not own entities.
    """

    id: str

    tool: str
    target: str

    mission_id: str | None = None

    status: str = "completed"

    started: datetime = field(default_factory=datetime.utcnow)
    finished: datetime = field(default_factory=datetime.utcnow)

    evidence: list[str] = field(default_factory=list)
    observations: list[str] = field(default_factory=list)
    entities: list[str] = field(default_factory=list)

    operator: str | None = None

    notes: str = ""