from dataclasses import dataclass


@dataclass
class Relationship:
    source: str
    target: str

    relationship: str

    confidence: float = 1.0