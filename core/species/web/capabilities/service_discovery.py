from core.capabilities.capability import Capability
from core.species.web.weapons import NmapWeapon


class ServiceDiscoveryCapability(Capability):
    id = "web.recon.service-discovery"
    name = "Service Discovery"
    description = (
        "Discover exposed network services."
    )

    def __init__(self):
        self._weapons = [
            NmapWeapon(),
        ]

    def weapons(self):
        return list(self._weapons)