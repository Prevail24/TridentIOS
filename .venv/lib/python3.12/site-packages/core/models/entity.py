from dataclasses import dataclass, field


class EntityType:
    EMAIL = "email"
    IP = "ip"
    DOMAIN = "domain"
    URL = "url"
    USERNAME = "username"
    PHONE = "phone"
    PERSON = "person"
    ORGANIZATION = "organization"
    LOCATION = "location"
    UNKNOWN = "unknown"


@dataclass
class Entity:
    """
    A real-world object discovered during an investigation.
    """

    id: str
    entity_type: str
    value: str
    display_name: str | None = None

    confidence: float = 1.0
    status: str = "active"

    observations: list[str] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

    @property
    def label(self) -> str:
        return self.display_name or self.value

    def add_observation(self, observation_id: str):
        if observation_id not in self.observations:
            self.observations.append(observation_id)

    def add_evidence(self, evidence_id: str):
        if evidence_id not in self.evidence:
            self.evidence.append(evidence_id)

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)