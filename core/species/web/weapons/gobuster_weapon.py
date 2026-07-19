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

        targets = self._targets(context)

        if not targets:
            raise RuntimeError(
                "Gobuster requires an observed HTTP surface."
            )

        self.awaken()

        return [
            GobusterSensor(
                target=target["url"],
                wordlist=self.wordlist,
                host_header=target["host_header"],
                status_codes_blacklist=self.status_codes_blacklist,
                threads=self.threads,
            ).collect()
            for target in targets
        ]

    def _targets(self, context: MissionContext) -> list[dict]:
        targets = []
        seen = set()

        for surface in context.web_surfaces():
            if self._is_redirect_only(surface):
                continue

            url = surface.get("probe_url") or surface.get("url")

            if not url:
                continue

            target = {
                "url": str(url),
                "host_header": surface.get("host_header"),
            }
            key = (target["url"], target["host_header"])

            if key in seen:
                continue

            seen.add(key)
            targets.append(target)

        return targets

    def _is_redirect_only(self, surface: dict) -> bool:
        status_code = surface.get("status_code")

        return (
            status_code in {301, 302, 303, 307, 308}
            and surface.get("redirect_location")
            and not surface.get("host_header")
        )
