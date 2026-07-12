from dataclasses import dataclass, field

from core.models.graph_edge import GraphEdge


@dataclass
class EntityGraph:
    center: str
    edges: list[GraphEdge] = field(default_factory=list)