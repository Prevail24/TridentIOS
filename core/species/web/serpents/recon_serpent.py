from core.serpents import Serpent
from core.species.web.capabilities import (
    ServiceDiscoveryCapability,
)


class ReconSerpent(Serpent):

    name = "Recon"

    description = (
        "Discovers web-facing infrastructure."
    )

    def __init__(self):
        self._capabilities = [
            ServiceDiscoveryCapability(),
        ]

    def capabilities(self):
        return list(self._capabilities)