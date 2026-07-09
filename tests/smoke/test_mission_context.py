from core.kernel.mission_context import MissionContext

context = MissionContext()

print()
print("MISSION CONTEXT")
print("---------------")
print(context.current_mission_id())

print()
print("ENRICHED PAYLOAD")
print("----------------")
print(
    context.enrich(
        {
            "sensor": "nmap",
            "host": "45.33.32.156",
        }
    )
)