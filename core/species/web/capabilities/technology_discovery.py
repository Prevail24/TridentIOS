from core.capabilities.capability import Capability
from core.species.web.weapons import HttpxWeapon


class TechnologyDiscoveryCapability(Capability):
    id = "web.recon.technology-discovery"
    name = "Technology Discovery"
    description = "Identify reachable HTTP endpoints and technologies."

    def __init__(self):
        self._weapons = [
            HttpxWeapon(),
        ]

    def weapons(self):
        return list(self._weapons)
