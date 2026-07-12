from dataclasses import dataclass, field
from datetime import date
from typing import Any


@dataclass
class Thread:
    """
    Base knowledge object for The Loom.

    A Thread represents one durable unit of knowledge.
    Examples include Observations, Techniques, Tools, Lessons,
    Patterns, Discoveries, Journals, and Playbooks.
    """

    id: str
    type: str
    title: str
    author: str
    created: date
    updated: date
    status: str = "active"
    confidence: int = 0
    tags: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)
    provenance: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def is_active(self) -> bool:
        return self.status == "active"

    def add_tag(self, tag: str) -> None:
        clean_tag = tag.strip().lower()

        if clean_tag and clean_tag not in self.tags:
            self.tags.append(clean_tag)

    def add_link(self, thread_id: str) -> None:
        clean_id = thread_id.strip()

        if clean_id and clean_id not in self.links:
            self.links.append(clean_id)

    def update_confidence(self, confidence: int) -> None:
        if confidence < 0 or confidence > 5:
            raise ValueError("Confidence must be between 0 and 5.")

        self.confidence = confidence