from core.capabilities.capability import Capability


class ServiceDiscoveryCapability(Capability):
    """
    Discovers exposed network services.
    """

    name = "Service Discovery"

    description = (
        "Discovers exposed network services."
    )