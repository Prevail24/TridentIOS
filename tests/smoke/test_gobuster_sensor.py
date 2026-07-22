from core.armory.gobuster.sensor import GobusterSensor


def test_gobuster_sensor_normalizes_tool_output():
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
    assert sensor.adapter.__class__.__module__ == (
        "core.adapters.gobuster_adapter"
    )
    assert len(observations) == 2
    assert observations[0].path == "index.php"
    assert observations[1].status_code == 418
    assert summary == {
        "sensor": "gobuster",
        "target": "http://orion.htb",
        "observations": 2,
    }
