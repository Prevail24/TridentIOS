from core.services.active_mission_service import ActiveMissionService

service = ActiveMissionService()

print()
print("ACTIVE MISSION")
print("--------------")

print(service.current())

print()
print("ACTIVATING...")

service.activate("MIS-2026-0001")

print(service.current())

print()
print("HAS ACTIVE")

print(service.has_active())

print()
print("CLEARING...")

service.clear()

print(service.current())