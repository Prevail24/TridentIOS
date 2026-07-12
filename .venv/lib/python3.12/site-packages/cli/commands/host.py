from core.services.host_profile_service import HostProfileService


def show_host(host: str):
    service = HostProfileService()

    profile = service.build(host)

    if profile is None:
        print("Host not found.")
        return

    print()
    print("═══════════════════════════════")
    print("        HOST PROFILE")
    print("═══════════════════════════════")
    print()

    print(f"Host: {profile['host']}")
    print()

    print("History")
    print("-------")
    print(f"First Seen  : {profile['first_seen']}")
    print(f"Last Seen   : {profile['last_seen']}")
    print(f"Observations: {profile['observation_count']}")
    print()

    print("Ports")
    print("-----")
    for port in sorted(profile["ports"]):
        print(f"• {port}")

    print()
    print("Services")
    print("--------")
    for service_name in sorted(profile["services"]):
        print(f"• {service_name}")

    print()
    print("Products")
    print("--------")
    for product in sorted(profile["products"]):
        print(f"• {product}")

    print()
    print("Versions")
    print("--------")
    for version in sorted(profile["versions"]):
        print(f"• {version}")