from core.sensors.nmap.sensor import NmapSensor


def recon_nmap(target: str):
    sensor = NmapSensor(target)

    run = sensor.collect()

    print()
    print("═══════════════════════════════")
    print("      NMAP COMPLETE")
    print("═══════════════════════════════")
    print()
    print(f"Run ID : {run.id}")
    print(f"Target : {run.target}")
    print()