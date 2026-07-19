class SpeciesRegistry:
    """
    Holds every discovered Species.
    """

    def __init__(self):
        self._species = {}

    def register(self, species):
        self._species[species.name.lower()] = species

    def all(self):
        return list(self._species.values())