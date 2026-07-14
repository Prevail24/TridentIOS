from dataclasses import dataclass, field


@dataclass
class CouncilAssessment:
    """
    Standard response returned by every Council member.
    """

    member: str
    title: str

    findings: list[str] = field(default_factory=list)

    confidence: float = 1.0