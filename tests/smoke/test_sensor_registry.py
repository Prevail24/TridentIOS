from core.sensors.sensor_registry import SensorRegistry
from core.sensors.nmap.sensor import NmapSensor


registry = SensorRegistry()
registry.register(NmapSensor("scanme.nmap.org"))

print()
print("SENSOR REGISTRY")
print("---------------")

for sensor_name in registry.list():
    sensor = registry.get(sensor_name)

    print(f"• {sensor.name}")
    print(f"  version : {sensor.version}")
    print(f"  produces: {', '.join(sensor.produces)}")