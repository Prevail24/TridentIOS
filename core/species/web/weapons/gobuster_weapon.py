from core.armory.gobuster.sensor import GobusterSensor
from core.kernel.mission_context import MissionContext
from core.weapons import Weapon


class GobusterWeapon(Weapon):
    """
    Discover content beneath HTTP surfaces already observed by Trident.
    """

    name = "Gobuster"
    description = "HTTP content and path discovery."

    def __init__(
        self,
        wordlist: str | None = None,
        *,
        status_codes_blacklist: str = "302,404",
        threads: int = 10,
    ):
        self.wordlist = wordlist
        self.status_codes_blacklist = status_codes_blacklist
        self.threads = threads

    def execute(self, context: MissionContext) -> list[dict]:
        if not self.wordlist:
            raise RuntimeError(
                "Gobuster requires an operator-selected wordlist."
            )

        targets = list(
            dict.fromkeys(
                str(surface["url"])
                for surface in context.web_surfaces()
                if surface.get("url")
            )
        )

        if not targets:
            raise RuntimeError(
                "Gobuster requires an observed HTTP surface."
            )

        self.awaken()

        return [
            GobusterSensor(
                target=target,
                wordlist=self.wordlist,
                status_codes_blacklist=self.status_codes_blacklist,
                threads=self.threads,
            ).collect()
            for target in targets
        ]
