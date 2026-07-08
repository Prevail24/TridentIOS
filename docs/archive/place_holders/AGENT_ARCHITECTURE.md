# AGENT_ARCHITECTURE.md

# The Observatory Agent Architecture

> "The Loom remembers what others forget.
> The Agents understand what the Loom remembers."

---

# Philosophy

Agents are autonomous specialists that operate on knowledge stored within The Loom.

They do not own data.

They do not store data.

They do not manipulate files directly.

Instead, Agents reason over knowledge through the Service Layer.

Every Agent has a single responsibility.

---

# Architecture

User

↓

Observatory

↓

Dashboard

↓

Agent

↓

Service

↓

Repository

↓

Parser

↓

The Loom

Agents never communicate directly with repositories.

Repositories never communicate with Agents.

The Service Layer is the only bridge.

---

# Agent Contract

Every Agent follows the same structure.

```python
class Agent:

    def run(self):
        ...

    def collect(self):
        ...

    def analyze(self):
        ...

    def report(self):
        ...
```

Each phase has a single purpose.

---

## Collect

Gather information from one or more Services.

Agents never access markdown or files.

Example:

MissionService()

ObservationService()

EvidenceService()

---

## Analyze

Reason over the collected knowledge.

Analysis may include:

- Counting
- Validation
- Pattern detection
- Correlation
- AI reasoning

No persistence occurs here.

---

## Report

Produce output.

Examples:

- Dashboard widget
- CLI report
- Markdown report
- JSON
- Future API response

Agents do not decide where reports are displayed.

---

# Design Principles

## Single Responsibility

Each Agent performs one task exceptionally well.

Never combine unrelated intelligence.

---

## Read First

Agents observe.

Curator is the only Agent permitted to repair knowledge.

---

## Deterministic First

Prefer deterministic algorithms before AI.

Example:

Duplicate IDs

Broken references

Missing relationships

should always be detected algorithmically.

AI should augment—not replace—structured reasoning.

---

## AI is Optional

An Agent must remain useful even when no AI model is available.

AI enhances reports.

AI never replaces verified knowledge.

---

# Current Agents

---

## Weaver

Purpose

Evaluate the integrity of The Loom.

Responsibilities

- Health checks
- Structural validation
- Knowledge quality
- Missing relationships

Never

- Modify knowledge

Commands

weaver analyze

Dashboard

Weaver Widget

---

## Curator

Purpose

Repair The Loom.

Responsibilities

- Repair links
- Remove duplicates
- Rebuild indexes
- Repair corruption

Never

- Invent information
- Perform intelligence analysis

Commands

curator scan

curator repair

---

## Scribe

Purpose

Transform verified knowledge into human-readable reports.

Responsibilities

- Mission summaries
- Observation summaries
- Daily briefings

Never

- Repair knowledge
- Perform integrity checks

Commands

scribe summarize

---

## Cartographer

Purpose

Visualize knowledge.

Responsibilities

- Relationship graphs
- Timeline graphs
- Mission maps
- Entity maps

Never

- Modify knowledge

Commands

map

---

## Analyst

Purpose

Discover hidden relationships using deterministic analysis and AI.

Responsibilities

- Cross-mission correlation
- Entity clustering
- Pattern detection
- AI-assisted reasoning

Never

- Modify evidence
- Modify observations

Commands

analyze

---

# Future Agents

Archivist

Maintains long-term historical knowledge.

---

Sentinel

Continuous monitoring.

Detects new intelligence requiring attention.

---

Librarian

Knowledge search.

Semantic retrieval.

---

Oracle

Strategic forecasting.

Produces probability assessments using AI.

---

# The Prime Directive

Agents exist to assist the Observer.

Agents never become the Observer.

Human judgment remains the final authority.

The Observatory augments human intelligence.

It never replaces it.