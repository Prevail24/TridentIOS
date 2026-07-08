from core.services.history_service import HistoryService


service = HistoryService()

history = service.build("45.33.32.156")

print()
print("HOST HISTORY")
print("------------")

if history is None:
    print("No history found")
    raise SystemExit(1)

for key, value in history.items():
    print(f"{key}: {value}")