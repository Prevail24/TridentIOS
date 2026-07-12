from core.services.mission_report_service import MissionReportService


def show_report(host: str):
    service = MissionReportService()

    report = service.build(host)

    if report is None:
        print("No report generated.")
        return

    print()
    print(report)