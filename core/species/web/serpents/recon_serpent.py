from core.serpents import Serpent
from core.species.web.capabilities import (
    ArtifactRetrievalCapability,
    ContentDiscoveryCapability,
    ServiceDiscoveryCapability,
    TechnologyDiscoveryCapability,
    VirtualHostDiscoveryCapability,
)


class ReconSerpent(Serpent):

    name = "Recon"

    description = (
        "Discovers web-facing infrastructure."
    )

    def __init__(
        self,
        gobuster_wordlist: str | None = None,
        vhost_target: str | None = None,
        vhost_domain: str | None = None,
        vhost_wordlist: str | None = None,
        artifact_url: str | None = None,
        artifact_host_header: str | None = None,
    ):
        self._capabilities = [
            ServiceDiscoveryCapability(),
            TechnologyDiscoveryCapability(),
            ContentDiscoveryCapability(
                wordlist=gobuster_wordlist,
            ),
            VirtualHostDiscoveryCapability(
                target=vhost_target,
                domain=vhost_domain,
                wordlist=vhost_wordlist,
            ),
            ArtifactRetrievalCapability(
                url=artifact_url,
                host_header=artifact_host_header,
            ),
        ]

    def capabilities(self):
        return list(self._capabilities)
