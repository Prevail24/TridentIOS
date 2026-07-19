# ADR-001 — The Birth of Species

Date:
2026-07-18

Decision:

Trident introduces the Species architecture.

A Species represents an investigative domain.

Species own Serpents.

Serpents own Capabilities.

Capabilities select Weapons.

Rationale:

This separates domain knowledge from execution,
allowing Trident to evolve naturally as an
Intelligence Operating System rather than a
collection of tools.