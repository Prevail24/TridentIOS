from core.serpents.hunter import Hunter
from core.council.council_member import CouncilMember
from core.serpents.historian import Historian
from core.serpents.skeptic import Skeptic


class CouncilRegistry:
    """
    Holds the active Council members.

    Medusa convenes the registry.
    The registry owns membership, not deliberation.
    """

    def __init__(self):
        self._members: dict[str, CouncilMember] = {}

        self.register(Hunter())
        self.register(Historian())
        self.register(Skeptic())

    def register(self, member: CouncilMember) -> None:
        name = member.name.strip().lower()

        if not name:
            raise ValueError(
                "Council members must define a name."
            )

        self._members[name] = member

    def get(self, name: str) -> CouncilMember:
        key = name.strip().lower()

        if key not in self._members:
            raise KeyError(
                f"Council member not registered: {name}"
            )

        return self._members[key]

    def all(self) -> list[CouncilMember]:
        return list(self._members.values())