from dataclasses import dataclass, field


@dataclass(frozen=True)
class CouncilAssessment:
    """
    Canonical assessment produced by a Council member.

    Assessments are reasoned opinions based on canonical
    observations.

    They are never evidence.

    They never create observations.

    They never modify the Loom.
    """

    member: str

    summary: str

    confidence: float = 1.0

    findings: list[str] = field(default_factory=list)

    recommendations: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)