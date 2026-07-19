from abc import ABC


class Capability(ABC):
    """
    A Capability represents something Trident knows how to do.

    Examples:

    • Service Discovery
    • JWT Analysis
    • Directory Enumeration
    """

    name = ""
    description = ""

    def weapons(self):
        return []