from core.weapons import Weapon


class NmapWeapon(Weapon):
    """
    Performs network service discovery using Nmap.

    (Implementation coming later.)
    """

    name = "Nmap"

    description = (
        "Network service discovery."
    )

    def execute(self, context):
        print("Running Nmap...")