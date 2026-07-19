from abc import ABC


class Serpent(ABC):
    """
    Base class for all Serpents.

    A Serpent specializes in one investigative discipline.
    """

    name = ""
    description = ""

    def strike(self):
        print(f"🐍 {self.name} Serpent strikes.")