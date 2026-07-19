from core.serpents import Serpent
from core.species.web.capabilities import (
    ContentDiscoveryCapability,
    ServiceDiscoveryCapability,
    TechnologyDiscoveryCapability,
)


class ReconSerpent(Serpent):

    name = "Recon"

    description = (
        "Discovers web-facing infrastructure."
    )

    def __init__(
        self,
        gobuster_wordlist: str | None = None,
    ):
        self._capabilities = [
            ServiceDiscoveryCapability(),
            TechnologyDiscoveryCapability(),
            ContentDiscoveryCapability(
                wordlist=gobuster_wordlist,
            ),
        ]

    def capabilities(self):
        return list(self._capabilities)
