from core.services.host_profile_service import HostProfileService

service = HostProfileService()

profile = service.build("45.33.32.156")

print()
print("HOST PROFILE")
print("------------")

for key, value in profile.items():
    print(f"{key}: {value}")