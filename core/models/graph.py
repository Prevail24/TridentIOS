from dataclasses import dataclass, field


@dataclass
class GraphNode:
    """
    One node inside an investigation graph.
    """

    id: str
    label: str
    children: list["GraphNode"] = field(default_factory=list)