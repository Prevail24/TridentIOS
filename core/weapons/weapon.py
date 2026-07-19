from abc import ABC


class Weapon(ABC):
    """
    A Weapon executes work.

    Weapons produce Observations.
    """

    name = ""

    def execute(self, context):
        raise NotImplementedError