class NmapAdapter:
    """
    Adapter for the Nmap sensor.

    This adapter is intentionally thin for now. It gives the NmapSensor
    a stable interface while we migrate the existing Nmap recon pipeline
    into the sensor architecture.
    """

    def __init__(self, target: str):
        self.target = target

    def execute(self):
        return {
            "sensor": "nmap",
            "target": self.target,
            "raw": None,
        }
