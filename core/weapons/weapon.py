from abc import ABC, abstractmethod


class Weapon(ABC):
    """
    Base contract for every Trident Weapon.

    Weapons execute a specific task and produce
    Observations for later analysis.

    Weapons should be small, focused, and reusable.
    """

    name: str = ""
    description: str = ""

    @abstractmethod
    def execute(self, context):
        """
        Execute the weapon.

        Parameters
        ----------
        context
            Mission context supplied by Medusa.

        Returns
        -------
        Observation | list[Observation]
        """
        raise NotImplementedError

    def awaken(self):
        print(f"⚔️ {self.name} Weapon awakened.")