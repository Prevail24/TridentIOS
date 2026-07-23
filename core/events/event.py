from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
import uuid


@dataclass
class Event:
    """
    Base event for Trident IOS.
    """

    event_type: str

    payload: Any

    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))