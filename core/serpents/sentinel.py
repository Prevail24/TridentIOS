from core.services.diff_service import DiffService
from core.services.tool_run_snapshot_service import ToolRunSnapshotService


class Sentinel:
    """
    Keeper of Change.

    Watches for differences between two moments in time.
    """

    def __init__(self):
        self.snapshots = ToolRunSnapshotService()
        self.diff = DiffService()

    def detect(
        self,
        previous_run: str,
        current_run: str,
    ):

        old = self.snapshots.build(previous_run)
        new = self.snapshots.build(current_run)

        return {
            "previous_run": previous_run,
            "current_run": current_run,
            "target": new["target"],
            "changes": self.diff.compare(old, new),
        }