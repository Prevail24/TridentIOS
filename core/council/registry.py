from core.serpents.hunter import Hunter

class CouncilRegistry:
    """
    Registry of available Council members.

    Eventually this becomes the discovery mechanism for the
    entire Council.
    """

    def __init__(self):
        self._members = {
            "hunter": Hunter(),
        }

    def get(self, name: str):
        return self._members[name.lower()]

    def members(self):
        return self._members