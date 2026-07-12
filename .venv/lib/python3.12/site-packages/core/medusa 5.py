"""
═══════════════════════════════════════════════════════

                MEDUSA

         The Intelligence Core of
              Trident IOS

Intelligence wins before the first packet is sent.
Because the battle isnt won when the attack begins.
Its won when youve already understood the battlefield.
The first packet is simply when everyone else realizes the battle has started.

═══════════════════════════════════════════════════════
"""

from core.serpents.archivist import Archivist

from core.serpents.historian import Historian

from core.serpents.sentinel import Sentinel

from core.serpents.hunter import Hunter

from core.serpents.oracle import Oracle

from core.serpents.skeptic import Skeptic

from core.serpents.strategist import Strategist

from core.serpents.reporter import Reporter

class Medusa:

    """
    Orchestrates Trident's Intelligence Council.
    Medusa owns coordination.
    The Serpents own their individual disciplines.
    """

    def __init__(self):
        self.archivist = Archivist()
        self.historian = Historian()
        self.sentinel = Sentinel()
        self.hunter = Hunter()
        self.oracle = Oracle()
        self.skeptic = Skeptic()
        self.strategist = Strategist()
        self.reporter = Reporter()

    def brief(self, host: str) -> str:

        """
        Return the council's operational briefing for a host.
        """

        return self.reporter.brief(host)