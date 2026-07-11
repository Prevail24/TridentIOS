"""
═══════════════════════════════════════════════════════

                    MEDUSA

         Chief Intelligence Officer
              Trident IOS

Precision before Power.

═══════════════════════════════════════════════════════
"""

from core.serpents.archivist import Archivist
from core.serpents.historian import Historian
from core.serpents.sentinel import Sentinel
from core.serpents.hunter import Hunter
from core.serpents.oracle import Oracle


class Medusa:

    def __init__(self):

        # Her Serpents

        self.archivist = Archivist()
        self.historian = Historian()
        self.sentinel = Sentinel()
        self.hunter = Hunter()
        self.oracle = Oracle()
        self.skeptic = Skeptic()
        self.strategist = Strategist()
        self.reporter = Reporter()

    def investigate(self, mission):
        pass