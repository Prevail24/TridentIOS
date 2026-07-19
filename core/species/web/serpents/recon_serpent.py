from .serpent import Serpent


class ReconSerpent(Serpent):
    """
    Performs reconnaissance against web targets.
    """

    name = "Recon"

    description = (
        "Discovers web-facing infrastructure."
    )