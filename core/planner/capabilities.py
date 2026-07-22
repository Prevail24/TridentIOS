DISPLAY_NAMES = {
    "web.recon.service-discovery": "Service Discovery",
    "web.recon.technology-discovery": "Technology Discovery",
    "web.recon.content-discovery": "Content Discovery",
    "web.recon.virtual-host-discovery": "Virtual Host Discovery",
    "web.recon.artifact-retrieval": "Artifact Retrieval",
}


def get_display_name(capability_id: str) -> str:
    """
    Return a human-readable name for a capability ID.

    Unknown capability IDs fall back to the ID itself so rendering
    remains safe when new capabilities are introduced.
    """
    return DISPLAY_NAMES.get(capability_id, capability_id)