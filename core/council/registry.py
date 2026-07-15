class CouncilRegistry:
    """
    Holds the active Council members.

    Medusa convenes the registry.

    The registry owns membership,
    not deliberation.
    """

    def __init__(self):
        self.members = []

    def register(self, member):
        self.members.append(member)

    def all(self):
        return list(self.members)