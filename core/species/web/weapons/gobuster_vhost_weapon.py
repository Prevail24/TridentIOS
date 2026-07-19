from core.armory.gobuster.sensor import GobusterSensor
from core.kernel.mission_context import MissionContext
from core.weapons import Weapon


class GobusterVhostWeapon(Weapon):
    """
    Discover virtual hosts for an HTTP target and parent domain.
    """

    name = "Gobuster Vhost"
    description = "HTTP virtual host discovery."

    def __init__(
        self,
        target: str | None = None,
        domain: str | None = None,
        wordlist: str | None = None,
        *,
        exclude_status: str | None = "301",
        threads: int = 10,
    ):
        self.target = target
        self.domain = domain
        self.wordlist = wordlist
        self.exclude_status = exclude_status
        self.threads = threads

    def execute(self, context: MissionContext) -> dict:
        if not self.target:
            raise RuntimeError(
                "Gobuster vhost requires an operator-selected target."
            )

        if not self.domain:
            raise RuntimeError(
                "Gobuster vhost requires an operator-selected domain."
            )

        if not self.wordlist:
            raise RuntimeError(
                "Gobuster vhost requires an operator-selected wordlist."
            )

        self.awaken()

        return GobusterSensor(
            target=self.target,
            wordlist=self.wordlist,
            mode="vhost",
            domain=self.domain,
            append_domain=True,
            exclude_status=self.exclude_status,
            threads=self.threads,
        ).collect()
