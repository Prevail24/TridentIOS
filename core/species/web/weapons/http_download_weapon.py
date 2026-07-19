from core.armory.http_download.sensor import HttpDownloadSensor
from core.kernel.mission_context import MissionContext
from core.weapons import Weapon


class HttpDownloadWeapon(Weapon):
    """
    Retrieve an operator-selected HTTP artifact as mission evidence.
    """

    name = "HTTP Download"
    description = "Download HTTP artifacts into mission evidence."

    def __init__(
        self,
        url: str | None = None,
        *,
        host_header: str | None = None,
    ):
        self.url = url
        self.host_header = host_header

    def execute(self, context: MissionContext) -> dict:
        if not self.url:
            raise RuntimeError(
                "HTTP Download requires an operator-selected URL."
            )

        self.awaken()

        return HttpDownloadSensor(
            self.url,
            host_header=self.host_header,
        ).collect()
