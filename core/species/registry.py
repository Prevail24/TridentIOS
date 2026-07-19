from core.species.web import WebSpecies


class SpeciesRegistry:
    """
    Holds every discovered Species.
    """

    def __init__(self):
        self._species = {}

        self.register(WebSpecies())

    def register(self, species):
        self._species[species.name.lower()] = species

    def get(self, name):
        return self._species[name.lower()]

    def all(self):
        return list(self._species.values())
    
    def awaken(self):
        print(f"🐍 {self.name} Species awakened.")