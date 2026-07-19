"""
═══════════════════════════════════════════════════════

                      MEDUSA

                Chief of Operations
                   Trident IOS

The Observer commands.
Medusa coordinates.
The Council reasons.
The Serpents explore.
The Loom remembers.

═══════════════════════════════════════════════════════
"""

from core.briefings.mission_brief import MissionBrief
from core.council.council import Council
from core.kernel.mission_context import MissionContext
from core.serpents.reporter import Reporter

from core.command.medusa import Medusa

__all__ = ["Medusa"]
