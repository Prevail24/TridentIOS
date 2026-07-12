from dataclasses import dataclass

from core.models.relationship import Relationship


@dataclass
class CreateRelationshipResult:
    relationship: Relationship
    filepath: str
    success: bool = True