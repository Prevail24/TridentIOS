from dataclasses import dataclass, field

from core.models.entity import Entity


@dataclass
class CreateEntityResult:
    entity: Entity
    filepath: str
    success: bool = True
    warnings: list[str] = field(default_factory=list)