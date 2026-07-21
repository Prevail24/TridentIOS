# TridentIOS Planner Architecture

## Status

**Proposed Architecture — Planner v1**

---

# Purpose

The Planner is TridentIOS's deterministic investigation guidance layer.

Its responsibility is to examine the current mission state and recommend the next appropriate investigative capabilities.

The Planner does **not** execute tools.

The Planner does **not** parse tool output.

The Planner does **not** inspect runtime files.

The Planner does **not** directly access repositories.

The Planner reasons only through the operational intelligence exposed by `MissionContext`.

---

# Core Principle

> The Planner recommends **what Trident should do next**, not **how a tool should do it.**

The Planner recommends **Capabilities**.

Species, Serpents, Weapons, Sensors, and Adapters determine how those Capabilities are executed.

---

# Architectural Position

```text
Sensors
    ↓
Adapters
    ↓
Parsers
    ↓
Canonical Observations
    ↓
Observation Engine
    ↓
Entities & Relationships
    ↓
MissionContext
    ↓
Planner
    ↓
Capability Recommendations
    ↓
Observer Decision
```

The Planner sits above mission intelligence and below the Observer.

It never bypasses existing architectural boundaries.

---

# Operational Contract

The Planner receives a `MissionContext`.

```python
recommendations = planner.plan(context)
```

The Planner queries mission intelligence through methods such as:

```python
context.open_ports()
context.services()
context.web_surfaces()
context.web_vhosts()
```

Future MissionContext methods may include:

```python
context.artifacts()
context.technologies()
context.credentials()
context.users()
context.files()
context.processes()
context.sockets()
context.certificates()
context.dns_records()
context.relationships()
```

The Planner must **never** access:

```python
ObservationRepository
ToolRunRepository
StateService
runtime JSON files
raw tool output
adapter results
sensor internals
```

Those implementation details remain behind `MissionContext`.

---

# Responsibilities

The Planner is responsible for:

1. Evaluating the active mission's intelligence.
2. Matching mission conditions against Planner Rules.
3. Producing deterministic Capability Recommendations.
4. Explaining why each recommendation exists.
5. Identifying the intelligence that triggered each recommendation.
6. Reporting whether the Capability currently exists.
7. Avoiding duplicate recommendations.
8. Returning recommendations without automatically executing them.

---

# Non-Responsibilities

The Planner is **not** responsible for:

- Running tools.
- Selecting command-line arguments.
- Parsing output.
- Creating observations.
- Writing repositories.
- Managing evidence.
- Creating entities.
- Creating relationships.
- Making autonomous decisions.
- Replacing the Observer.

---

# Planner Rule

A Planner Rule represents one proven investigative lesson.

Each rule answers one question:

> "Given these mission conditions, what capability should be recommended?"

Rules should remain extremely small.

Example:

```text
Condition

HTTP Redirect Detected

↓

Recommend

Virtual Host Discovery
```

Another example:

```text
Condition

Downloaded Archive

↓

Recommend

Archive Inspection
```

Rules should contain no tool-specific logic.

They recommend Capabilities, never Weapons.

---

# Recommendation

A Recommendation contains:

- Capability
- Confidence
- Reason
- Triggering Evidence
- Availability

Example:

```text
Capability

Virtual Host Discovery

Reason

HTTP redirect indicates a canonical hostname.

Confidence

High

Status

Available
```

If the Capability has not yet been implemented:

```text
Capability

Archive Inspection

Status

Missing Capability

Reason

Planner rule exists.
Capability not yet implemented.
```

The Planner should still recommend it.

---

# Mission Intelligence

The Planner reasons from Mission Intelligence rather than raw observations.

MissionContext converts thousands of individual observations into operational facts.

Examples include:

- Open Services
- Web Surfaces
- Virtual Hosts
- Technologies
- Artifacts
- Credentials
- Files
- Relationships

The Planner consumes these facts instead of individual tool output.

---

# Design Philosophy

Every completed mission should improve Trident.

A mission produces:

- New observations
- New entities
- New relationships
- New Planner Rules
- New Capabilities
- Better investigations

The Planner is therefore expected to grow continuously as Trident evolves.

Every Hack The Box machine, assessment, engagement, or investigation should leave the Planner smarter than before.

---

# Long-Term Vision

Today:

```text
Mission
    ↓
Planner
    ↓
Recommendations
```

Future:

```text
Mission
    ↓
Planner Rules
    ↓
Knowledge Graph
    ↓
Council
    ↓
Observer
```

Deterministic rules remain the foundation.

Future AI systems reason on top of that foundation rather than replacing it.

---

# Guiding Principle

> Every mission should leave Trident smarter than it was before the mission began.

The Planner exists to capture those lessons and transform them into repeatable investigation doctrine.