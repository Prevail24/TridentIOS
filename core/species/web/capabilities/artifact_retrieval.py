from core.capabilities.capability import Capability
from core.species.web.weapons import HttpDownloadWeapon


class ArtifactRetrievalCapability(Capability):
    id = "web.recon.artifact-retrieval"
    name = "Artifact Retrieval"
    description = "Retrieve HTTP artifacts into mission evidence."

    def __init__(
        self,
        url: str | None = None,
        *,
        host_header: str | None = None,
    ):
        self._weapons = [
            HttpDownloadWeapon(
                url=url,
                host_header=host_header,
            ),
        ]

    def weapons(self):
        return list(self._weapons)
