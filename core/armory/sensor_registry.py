class SensorRegistry:
    """
    Registry of available Trident IOS sensors.
    """

    def __init__(self):
        self._sensors = {}

    def register(self, sensor):
        self._sensors[sensor.name] = sensor

    def get(self, name):
        return self._sensors.get(name)

    def list(self):
        return sorted(self._sensors.keys())