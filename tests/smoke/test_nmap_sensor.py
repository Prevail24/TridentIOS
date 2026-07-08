from core.sensors.nmap.sensor import NmapSensor

sensor = NmapSensor("scanme.nmap.org")

print()
print("NMAP SENSOR")
print("-----------")
print(f"name: {sensor.name}")
print(f"version: {sensor.version}")
print(f"produces: {sensor.produces}")