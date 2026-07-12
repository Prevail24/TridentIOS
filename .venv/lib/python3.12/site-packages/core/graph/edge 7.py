from dataclasses import dataclass

from .node import Node


@dataclass
class Edge:
    source: Node
    relationship: str
    target: Node