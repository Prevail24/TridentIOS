from abc import ABC


class Capability(ABC):
    """
    Base contract for every Trident Capability.

    A Capability represents something a Serpent knows
    how to perform.

    Capabilities choose Weapons.

    Capabilities never execute tools directly.
    """

    id: str = ""
    name: str = ""
    description: str = ""

    def weapons(self) -> list:
        return []

    def awaken(self):
        print(f"🧠 {self.name} Capability awakened.")