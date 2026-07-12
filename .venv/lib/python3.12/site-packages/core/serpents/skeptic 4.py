from core.serpents.oracle import Oracle


class Skeptic:
    """
    Keeper of Verification.

    Reviews Oracle's hypotheses and assigns an
    initial verification status.
    """

    def __init__(self):
        self.oracle = Oracle()

    def verify(self, host: str) -> list[dict]:

        hypotheses = self.oracle.hypothesize(host)

        results = []

        for hypothesis in hypotheses:

            confidence = hypothesis["confidence"]

            if confidence == "high":
                status = "verified"
            elif confidence == "medium":
                status = "plausible"
            else:
                status = "unverified"

            results.append(
                {
                    "hypothesis": hypothesis["hypothesis"],
                    "confidence": confidence,
                    "status": status,
                }
            )

        return results