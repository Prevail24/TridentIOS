from abc import ABC


class Species(ABC):
    """
    Base class for every Trident Species.

    A Species represents an investigative domain.

    Examples:

    - Web
    - Malware
    - OSINT
    - Cloud
    - Active Directory
    """

    name: str = ""
    description: str = ""