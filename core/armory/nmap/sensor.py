from core.armory.sensor import Sensor
from core.adapters.nmap_adapter import NmapAdapter

class NmapSensor(Sensor):
    name = "nmap"
    version = "0.1.0"

    produces = [
        "host",
        "port",
        "service",
        "product",
        "version",
    ]

    def __init__(self, target: str):
        self.target = target
        self.adapter = NmapAdapter(target)

    def collect(self):
        return self.adapter.execute()

    def normalize(self, raw_data):
        return raw_data

    def emit(self, observations):
        return {
            "sensor": self.name,
            "target": self.target,
            "observations": len(observations) if observations else 0,
        }