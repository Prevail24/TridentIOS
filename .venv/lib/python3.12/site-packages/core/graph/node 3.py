from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    entity_type: str
    value: str