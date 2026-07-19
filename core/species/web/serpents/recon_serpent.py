from core.serpents import Serpent


class ReconSerpent(Serpent):
    """
    The reconnaissance specialist of the Web Species.

    Recon Serpent establishes initial visibility of a target
    before deeper enumeration or analysis begins.
    """

    name = "Recon"

    description = (
        "Discovers and profiles web-facing infrastructure."
    )