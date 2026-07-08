from core.services.chronicle_service import ChronicleService


def show_chronicle(host: str):
    service = ChronicleService()
    entries = service.build(host)

    print()
    print("═══════════════════════════════")
    print("      MISSION CHRONICLE")
    print("═══════════════════════════════")

    for entry in entries:
        print()
        print(entry["timestamp"])
        print("─" * 31)
        print(f"Observations: {entry['count']}")

        if entry["services"]:
            print()
            print("Services")
            for service_name in entry["services"]:
                print(f"• {service_name}")

        if entry["products"]:
            print()
            print("Products")
            for product in entry["products"]:
                print(f"• {product}")

        if entry["versions"]:
            print()
            print("Versions")
            for version in entry["versions"]:
                print(f"• {version}")