from abc import ABC


class Species(ABC):
    """
    Base class for every Trident Species.
    """

    name = ""
    description = ""

    def awaken(self):
        print(f"🐍 {self.name} Species awakened.")