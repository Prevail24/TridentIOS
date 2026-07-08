from core.services.diff_service import DiffService

old = {
    "ports": ["tcp/22", "tcp/80"],
    "services": ["ssh", "http"],
    "products": ["OpenSSH"],
    "versions": ["6.6"],
}

new = {
    "ports": ["tcp/22", "tcp/80", "tcp/443"],
    "services": ["ssh", "http", "https"],
    "products": ["OpenSSH", "Apache"],
    "versions": ["6.6", "2.4.7"],
}

diff = DiffService.compare(old, new)

print()
print("DIFFERENTIAL INTELLIGENCE")
print("-------------------------")

for section, changes in diff.items():
    print()
    print(section.upper())

    print("Added")
    for item in changes["added"]:
        print(f"  + {item}")

    print("Removed")
    for item in changes["removed"]:
        print(f"  - {item}")