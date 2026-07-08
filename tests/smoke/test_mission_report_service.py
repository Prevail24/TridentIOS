from core.services.mission_report_service import MissionReportService


service = MissionReportService()

report = service.build("45.33.32.156")

if report is None:
    print("No report generated")
    raise SystemExit(1)

print()
print(report)