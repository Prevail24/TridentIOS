from abc import ABC


class Serpent(ABC):
    """
    A Serpent is a specialist belonging to a Species.

    Serpents never execute tools directly.

    They choose Capabilities.
    """

    name = ""
    description = ""

    def capabilities(self):
        return []