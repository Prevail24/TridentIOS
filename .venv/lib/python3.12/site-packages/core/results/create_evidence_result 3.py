from dataclasses import dataclass, field

from core.models.evidence import Evidence


@dataclass
class CreateEvidenceResult:
    evidence: Evidence
    filepath: str
    success: bool = True
    warnings: list[str] = field(default_factory=list)