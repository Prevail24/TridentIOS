from dataclasses import dataclass, field
from datetime import date,datetime
from typing import Literal

 


@dataclass
class Mission:
    id: str
    name: str
    started_at: datetime
    status: str = "ACTIVE"

MissionStatus = Literal["active", "paused", "completed", "archived"]


@dataclass
class Mission:
    """
    A Mission represents a Trident operation.

    It is the source of truth for an investigation workspace.
    """

    id: str
    title: str
    mission_type: str
    objective: str
    scope: str
    operator: str
    created: date
    updated: date
    status: MissionStatus = "active"
    priority: str = "normal"

    playbooks: list[str] = field(default_factory=list)
    observations: list[str] = field(default_factory=list)
    entities: list[str] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    relationships: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

    def touch(self) -> None:
        self.updated = date.today()

    def add_playbook(self, playbook_id: str) -> None:
        if playbook_id not in self.playbooks:
            self.playbooks.append(playbook_id)
            self.touch()

    def add_observation(self, observation_id: str) -> None:
        if observation_id not in self.observations:
            self.observations.append(observation_id)
            self.touch()

    def add_entity(self, entity_id: str) -> None:
        if entity_id not in self.entities:
            self.entities.append(entity_id)
            self.touch()

    def add_evidence(self, evidence_id: str) -> None:
        if evidence_id not in self.evidence:
            self.evidence.append(evidence_id)
            self.touch()

    def add_relationship(self, relationship_id: str) -> None:
        if relationship_id not in self.relationships:
            self.relationships.append(relationship_id)
            self.touch()

    def pause(self) -> None:
        self.status = "paused"
        self.touch()

    def activate(self) -> None:
        self.status = "active"
        self.touch()

    def complete(self) -> None:
        self.status = "completed"
        self.touch()


    def archive(self) -> None:
        self.status = "archived"
        self.touch()