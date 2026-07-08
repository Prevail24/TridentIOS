from core.sensors.base import Sensor
from core.adapters.nmap_adapter import NmapAdapter


class NmapSensor(Sensor):

    name = "nmap"

    def __init__(self, target):
        self.adapter = NmapAdapter(target)

    def collect(self):
        return self.adapter.execute()

    def emit(self):
        # Adapter already emits observations today.
        # We'll improve this later.
        return []