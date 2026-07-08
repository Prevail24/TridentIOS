class DiffService:
    """
    Computes differences between two host profiles.
    """

    @staticmethod
    def compare(old_profile, new_profile):

        def diff(field):
            old = set(old_profile.get(field, []))
            new = set(new_profile.get(field, []))

            return {
                "added": sorted(new - old),
                "removed": sorted(old - new),
            }

        return {
            "ports": diff("ports"),
            "services": diff("services"),
            "products": diff("products"),
            "versions": diff("versions"),
        }