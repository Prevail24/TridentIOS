from core.planner.capabilities import get_display_name


class PlannerRenderer:

    def render(self, recommendations):
        print()
        print("MISSION PLAN")
        print("─" * 40)

        if not recommendations:
            print("No recommendations.")
            return

        for index, recommendation in enumerate(
            recommendations,
            start=1,
        ):
            capability_name = get_display_name(
                recommendation.capability_id
            )

            print(
                f"{index}. [{recommendation.confidence.upper()}]"
            )
            print(capability_name)
            print()

            print(f"Reason: {recommendation.reason}")

            if recommendation.inputs:
                print("Known Inputs:")

                for name, value in recommendation.inputs:
                    print(f"  {name}: {value}")

            if recommendation.required_inputs:
                required = ", ".join(
                    recommendation.required_inputs
                )
                print(f"Requires: {required}")
                
            elif recommendation.executable:
                print("Status: Ready")
            else:
                print(
                    f"Status: {recommendation.status.value}"
                )

            if recommendation.rule:
                print(f"Rule: {recommendation.rule}")

            print()