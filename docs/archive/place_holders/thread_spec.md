# Thread Specification

## Purpose

A **Thread** is the fundamental knowledge object within **The Loom**.

Every permanent piece of knowledge stored by The Watchers is represented as a Thread.

Applications such as TridentIOS, SignalFlare, CertQuest, and future Watchers services do not own knowledge—they create, update, and link Threads.

---

# Philosophy

> Knowledge is woven, not stored.
>
> Every Thread strengthens The Loom.

A Thread should represent one meaningful piece of knowledge that can evolve over time and connect to other Threads.

---

# Thread Types

Supported thread types include:

- Observation
- Technique
- Tool
- Playbook
- Discovery
- Pattern
- Theory
- Lesson
- Journal
- Strategy
- Reference
- Experiment

New thread types may be introduced without changing the core architecture.

---

# Required Metadata

Every Thread must contain YAML frontmatter with at least:

```yaml
id:
type:
title:
author:
created:
updated:
status:
confidence:
tags: []
links: []
```

---

# Provenance

Every Thread must preserve its lineage.

Knowledge without provenance cannot be fully trusted.

The provenance section records where a Thread originated, how it evolved, and who validated it.

Example:

```yaml
provenance:
  created_by: TridentIOS
  source_application: TridentIOS
  source_platform: Hack The Box
  source_case: "Sherlock - The Last Broadcast"

  derived_from:
    - OBS-2026-0007

  reviewed_by:
    - Scribe

  approved_by:
    - Observer

  woven_by:
    - Weaver
```

Questions provenance should answer:

- Where did this knowledge originate?
- Which Observation first discovered it?
- Has it been independently verified?
- Which Threads contributed to it?
- Has it been revised?
- Who approved it for The Loom?

---

# Identity

Every Thread has:

- A permanent ID.
- A single primary purpose.
- Revision history.
- Relationships to other Threads.

Thread IDs are immutable.

---

# Relationships

Threads are connected through explicit links.

Examples:

- Observation → Technique
- Technique → Tool
- Observation → Playbook
- Discovery → Pattern
- Lesson → Observation

The Loom should be able to navigate these relationships in any direction.

---

# Knowledge Graph

The Loom is a graph of interconnected Threads.

Each Thread may reference any number of other Threads.

Relationship types include:

- derived_from
- supports
- contradicts
- expands
- supersedes
- references
- related_to
- discovered_by
- validated_by

These relationships allow the Observatory, Archivist, and future AI systems to navigate knowledge rather than simply search documents.

---

# Lifecycle

1. Created by a Watchers application.
2. Reviewed by The Scribe.
3. Approved by the Observer.
4. Woven into The Loom by the Weaver.
5. Indexed by the Archivist.
6. Referenced by future investigations.

---

# Design Principles

- One Thread represents one idea.
- Threads should link rather than duplicate information.
- Preserve history through revisions.
- Facts, hypotheses, and opinions must remain clearly separated.
- Every Thread should increase the usefulness of The Loom.

---

# Long-Term Vision

The Thread model is domain-agnostic.

It is intended to support every Watchers application, including:

- TridentIOS
- SignalFlare
- CertQuest
- Future Watchers projects

Applications create Threads.

The Loom preserves Threads.

The Observatory visualizes Threads.

Together they form the intelligence architecture of The Watchers Platform.

---

# The Watchers Principle

> Threads are the fabric of memory.
>
> The Loom is only as strong as the quality of the Threads woven into it.