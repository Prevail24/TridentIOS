from core.services.diff_service import DiffService
from core.services.tool_run_snapshot_service import ToolRunSnapshotService

snapshots = ToolRunSnapshotService()

old = snapshots.build("RUN-2026-0030")
new = snapshots.build("RUN-2026-0031")



diff = DiffService.compare(old, new)

print()
print("SNAPSHOT DIFFERENTIAL")
print("---------------------")

for section, changes in diff.items():

    if not changes["added"] and not changes["removed"]:
        continue

    print()
    print(section.upper())

    for item in changes["added"]:
        print(f"+ {item}")

    for item in changes["removed"]:
        print(f"- {item}")

print()
print("Done.")