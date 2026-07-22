from abc import ABC


class Serpent(ABC):
    """
    Base contract for every Trident Serpent.

    A Serpent is a specialist belonging to a Species.

    Serpents:
    - organize Capabilities
    - do not execute tools directly
    - do not create observations directly
    """

    name: str = ""
    description: str = ""

    def capabilities(self) -> list:
        """
        Return the Capabilities owned by this Serpent.
        """
        return []

    def awaken(self) -> None:
        print(f"🐍 {self.name} Serpent awakened.")