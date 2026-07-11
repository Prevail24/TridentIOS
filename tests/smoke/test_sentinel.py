from core.serpents.sentinel import Sentinel

sentinel = Sentinel()

report = sentinel.detect(
    "RUN-2026-0030",
    "RUN-2026-0031",
)

print()
print("SENTINEL")
print("---------")
print("Watching:", report["target"])

changes = report["changes"]

empty = True

for category, diff in changes.items():

    if diff["added"] or diff["removed"]:

        empty = False

        print()
        print(category.upper())

        for item in diff["added"]:
            print(f"+ {item}")

        for item in diff["removed"]:
            print(f"- {item}")

if empty:
    print()
    print("No changes detected.")