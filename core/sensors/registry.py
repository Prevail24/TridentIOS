class SensorRegistry:

    def __init__(self):
        self._sensors = []

    def register(self, sensor):
        self._sensors.append(sensor)

    def all(self):
        return self._sensors