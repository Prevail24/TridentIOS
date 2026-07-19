from core.species.species import Species
from .serpents.recon_serpent import ReconSerpent


class WebSpecies(Species):

    name = "Web"

    description = (
        "Investigates web-facing infrastructure."
    )

    def available_serpents(self):
        return self.serpents

    def __init__(self):
        self.serpents = [
            ReconSerpent(),
        ]