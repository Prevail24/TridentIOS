from core.sensors.nmap.sensor import NmapSensor


def medusa_strike(target: str):
    print()
    print("🐍 Medusa")
    print("Council assembling...")
    print()
    print("👁 Sentinel  : Monitoring reality")
    print("🎯 Hunter    : Preparing investigation")
    print("📢 Reporter  : Standing by")
    print()
    print("Strike authorized.")
    print()

    recon_nmap(target)


def recon_nmap(target: str):
    sensor = NmapSensor(target)
    run = sensor.collect()

    print()
    print("═══════════════════════════════")
    print("      NMAP COMPLETE")
    print("═══════════════════════════════")
    print()
    print(f"Run ID : {run.id}")
    print(f"Target : {target}")