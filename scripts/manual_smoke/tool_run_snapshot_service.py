from core.services.tool_run_snapshot_service import ToolRunSnapshotService

service = ToolRunSnapshotService()

snapshot = service.build("RUN-2026-0022")

print()
print("TOOL RUN SNAPSHOT")
print("-----------------")

for key, value in snapshot.items():
    print(f"{key}: {value}")