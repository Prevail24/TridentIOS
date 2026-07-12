from dataclasses import dataclass


@dataclass
class GraphEdge:
    source: str
    relationship: str
    target: str