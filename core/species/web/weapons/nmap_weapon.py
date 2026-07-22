from core.armory.nmap.sensor import NmapSensor
from core.kernel.mission_context import MissionContext
from core.models.tool_run import ToolRun
from core.weapons import Weapon


class NmapWeapon(Weapon):
    """
    Performs network service discovery using the existing
    Trident Nmap Sensor pipeline.

    The Weapon coordinates execution but does not parse,
    translate, persist, or analyze Nmap output itself.
    """

    name = "Nmap"

    description = (
        "Network service discovery."
    )

    def execute(
        self,
        context: MissionContext,
    ) -> ToolRun:
        target = context.target()

        self.awaken()

        sensor = NmapSensor(target)
        return sensor.collect()
