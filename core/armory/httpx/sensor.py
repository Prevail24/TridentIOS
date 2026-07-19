from core.armory.sensor import Sensor
from core.adapters.httpx_adapter import HttpxAdapter


class HttpxSensor(Sensor):
    name = "httpx"
    version = "0.1.0"

    produces = [
        "url",
        "host",
        "ip_address",
        "http_status",
        "page_title",
        "web_server",
        "technology",
    ]

    def __init__(self, target: str):
        self.target = target
        self.adapter = HttpxAdapter(target)

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
