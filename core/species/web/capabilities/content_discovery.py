from core.capabilities.capability import Capability
from core.species.web.weapons import GobusterWeapon


class ContentDiscoveryCapability(Capability):
    name = "Content Discovery"
    description = "Discover paths beneath observed HTTP surfaces."

    def __init__(self, wordlist: str | None = None):
        self._weapons = [
            GobusterWeapon(wordlist=wordlist),
        ]

    def weapons(self):
        return list(self._weapons)
