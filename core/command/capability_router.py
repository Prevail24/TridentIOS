from core.planner.recommendation import Recommendation
from core.serpents.serpent import Serpent


class CapabilityNotFoundError(LookupError):
    """
    Raised when no registered Serpent owns the requested Capability.
    """


class CapabilityExecutionError(RuntimeError):
    """
    Raised when a Capability cannot be executed safely.
    """


class CapabilityRouter:
    """
    Resolves Capability IDs through registered Serpents and dispatches
    execution to the Weapons owned by the selected Capability.
    """

    def __init__(self, serpents: list[Serpent]):
        self._serpents = list(serpents)

    def resolve(self, capability_id: str):
        """
        Return the Capability matching the supplied stable ID.
        """
        for serpent in self._serpents:
            for capability in serpent.capabilities():
                if capability.id == capability_id:
                    return capability

        raise CapabilityNotFoundError(
            f"No capability registered with ID: {capability_id}"
        )

    def execute(self, capability_id: str, context) -> list:
        """
        Execute every Weapon owned by a Capability.

        Each Weapon receives the current MissionContext. Results are
        returned in Weapon order.
        """
        capability = self.resolve(capability_id)
        weapons = capability.weapons()

        if not weapons:
            raise CapabilityExecutionError(
                f"Capability '{capability_id}' has no available weapons."
            )

        results = []

        for weapon in weapons:
            results.append(weapon.execute(context))

        return results

    def execute_recommendation(
    self,
    recommendation: Recommendation,
    context,
) -> list:
        """
        Execute a Planner recommendation when it is immediately
        executable.
        """
        if not recommendation.available:
            raise CapabilityExecutionError(
                f"Capability '{recommendation.capability_id}' "
                "is currently unavailable."
            )

        if recommendation.required_inputs:
            required = ", ".join(recommendation.required_inputs)

            raise CapabilityExecutionError(
                f"Capability '{recommendation.capability_id}' requires "
                f"additional input: {required}"
            )

        if not recommendation.executable:
            raise CapabilityExecutionError(
                f"Recommendation for "
                f"'{recommendation.capability_id}' is not executable "
                f"while its status is "
                f"'{recommendation.status.value}'."
            )

        return self.execute(
            capability_id=recommendation.capability_id,
            context=context,
        )