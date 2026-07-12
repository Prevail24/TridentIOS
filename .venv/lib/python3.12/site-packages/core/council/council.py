from cli.commands import host
from core.serpents.hunter import Hunter
from core.serpents.oracle import Oracle
from core.serpents.skeptic import Skeptic
from core.serpents.reporter import Reporter


class Council:
    """
    Coordinates TridentIOS Council deliberation.

    Serpents remain independent specialists.
    The Council invokes their public interfaces and
    assembles their separate intelligence artifacts.
    """

    def __init__(self) -> None:
        self.hunter = Hunter()
        self.oracle = Oracle()
        self.skeptic = Skeptic()
        self.reporter = Reporter()

    def deliberate(self, host: str) -> dict:
        """
        Convene the available Council members for a host.

        Returns:
            A structured collection containing Hunter
            recommendations, Oracle theories, and Skeptic reviews.
        """
        recommendations = self.hunter.hunt(host)
        theories = self.oracle.hypothesize(host)
        reviews = self.skeptic.review(theories)

    
        briefing = {
            "host": host,
            "recommendations": recommendations,
            "theories": theories,
            "reviews": reviews,
        }

        self.reporter.brief(briefing)

        return briefing