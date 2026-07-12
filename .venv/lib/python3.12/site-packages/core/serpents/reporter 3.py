from core.serpents.strategist import Strategist


class Reporter:
    """
    Keeper of the Briefing.
    """

    def __init__(self):
        self.strategist = Strategist()

    def brief(self, host: str) -> str:

        plan = self.strategist.plan(host)

        lines = []

        lines.append("Observer...")
        lines.append("")
        lines.append("Mission Briefing")
        lines.append("----------------")

        if not plan:
            lines.append("No operational recommendations.")
        else:
            lines.append("Recommended Course of Action:")
            lines.append("")

            for step in plan:
                lines.append(f"• {step}")

        return "\n".join(lines)