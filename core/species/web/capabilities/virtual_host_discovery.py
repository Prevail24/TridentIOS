from core.capabilities.capability import Capability
from core.species.web.weapons import GobusterVhostWeapon


class VirtualHostDiscoveryCapability(Capability):
    id = "web.recon.virtual-host-discovery"
    name = "Virtual Host Discovery"
    description = "Discover HTTP virtual hosts for known web targets."

    def __init__(
        self,
        target: str | None = None,
        domain: str | None = None,
        wordlist: str | None = None,
    ):
        self._weapons = [
            GobusterVhostWeapon(
                target=target,
                domain=domain,
                wordlist=wordlist,
            ),
        ]

    def weapons(self):
        return list(self._weapons)
