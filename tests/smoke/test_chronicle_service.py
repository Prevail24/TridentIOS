from core.services.chronicle_service import ChronicleService

service = ChronicleService()

entries = service.build("45.33.32.156")

print()
print("MISSION CHRONICLE")
print("-----------------")

for entry in entries:

    print()
    print(entry["timestamp"])

    print(f"Observations : {entry['count']}")

    if entry["services"]:
        print("Services")
        for service in entry["services"]:
            print(f"  • {service}")

    if entry["products"]:
        print("Products")
        for product in entry["products"]:
            print(f"  • {product}")

    if entry["versions"]:
        print("Versions")
        for version in entry["versions"]:
            print(f"  • {version}")