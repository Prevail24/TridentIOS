from core.armory.httpx.sensor import HttpxSensor
from core.kernel.mission_context import MissionContext
from core.weapons import Weapon


class HttpxWeapon(Weapon):
    """
    Fingerprint the active mission's HTTP surface through HTTPX.
    """

    name = "HTTPX"
    description = "HTTP technology and endpoint discovery."

    def execute(self, context: MissionContext) -> dict:
        target = context.target()

        self.awaken()

        return HttpxSensor(target).collect()
