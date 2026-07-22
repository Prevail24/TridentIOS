from core.species.species import Species
from core.species.web.serpents import ReconSerpent


class WebSpecies(Species):
    """
    Species #001

    Investigates web-facing infrastructure.
    """

    name = "Web"

    description = (
        "Investigates web-facing infrastructure."
    )

    def __init__(self) -> None:
        self._serpents = [
            ReconSerpent(),
        ]

    def serpents(self) -> list:
        return list(self._serpents)