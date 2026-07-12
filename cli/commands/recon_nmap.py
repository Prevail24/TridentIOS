from core.sensors.nmap.sensor import NmapSensor


from core.serpents.hunter import Hunter


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

    hunter = Hunter()
    leads = hunter.hunt(target)

    print()
    print("═══════════════════════════════")
    print("      HUNTER ASSESSMENT")
    print("═══════════════════════════════")
    print()

    if not leads:
        print("No investigative leads identified.")
        return

    for index, lead in enumerate(leads, start=1):
        print(f"{index}. {lead}")

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