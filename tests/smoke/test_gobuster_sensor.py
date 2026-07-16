from core.armory.gobuster.sensor import GobusterSensor


raw_output = """
index.php   (Status: 200) [Size: 12272]
wp-admin    (Status: 418) [Size: 54217]
""".strip()

sensor = GobusterSensor(
    target="http://orion.htb",
    wordlist="/tmp/not-executed.txt",
)

observations = sensor.normalize(raw_output)
summary = sensor.emit(observations)

assert sensor.name == "gobuster"
assert len(observations) == 2
assert observations[0].path == "index.php"
assert observations[1].status_code == 418
assert summary == {
    "sensor": "gobuster",
    "target": "http://orion.htb",
    "observations": 2,
}

print()
print("Gobuster Sensor")
print("----------------")
print(f"name: {sensor.name}")
print(f"observations: {len(observations)}")
print("PASS")
