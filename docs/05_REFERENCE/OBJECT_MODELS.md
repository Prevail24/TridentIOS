# 🧩 Object Models

> **The canonical data models that represent intelligence within the Trident Intelligence Operating System.**

---

# Purpose

Object Models define the building blocks of Mission intelligence.

While the Mission Schema defines **how a Mission is organized**, Object Models define **what the Mission contains**.

Every Observation, Entity, Finding, Hypothesis, and Artifact follows the models described in this document.

---

# Philosophy

Every object should be:

- Immutable where practical
- Versioned
- Traceable
- Explainable
- Replayable
- Extensible

Objects represent intelligence.

Platform behavior is represented separately through Events.

---

# Intelligence Object Hierarchy

```text
Mission
│
├── Observation
├── Entity
├── Relationship
├── Finding
├── Hypothesis
├── Evidence
├── Artifact
├── Recommendation
├── Reference
└── Timeline Event
```

---

# Base Intelligence Object

All intelligence objects share common metadata.

```yaml
id:
created_at:
created_by:
confidence:
labels:
metadata:
references:
provenance:
```

| Field | Description |
|--------|-------------|
| id | Unique object identifier |
| created_at | Creation timestamp |
| created_by | Producing component |
| confidence | Confidence level |
| labels | Optional tags |
| metadata | Extension metadata |
| references | Supporting references |
| provenance | Origin information |

---

# Observation

## Purpose

A raw fact collected during a Mission.

Observations should never contain conclusions.

### Schema

```yaml
observation:

  id:
  timestamp:
  source:
  capability:
  confidence:
  summary:
  data:
  references:
```

### Examples

- Open TCP port
- DNS record
- HTTP response
- SSL certificate
- WHOIS registration

---

# Entity

## Purpose

Represents an identifiable object discovered during a Mission.

### Schema

```yaml
entity:

  id:
  type:
  name:
  aliases:
  attributes:
  confidence:
```

### Examples

- Domain
- IP Address
- Person
- Organization
- Email Address
- Certificate
- Malware Family

---

# Relationship

## Purpose

Represents a connection between two Entities.

### Schema

```yaml
relationship:

  id:
  source_entity:
  target_entity:
  relationship_type:
  confidence:
  evidence:
```

### Example

```text
example.com

↓

RESOLVES_TO

↓

104.26.3.12
```

---

# Finding

## Purpose

A validated conclusion derived from Mission intelligence.

### Schema

```yaml
finding:

  id:
  title:
  description:
  severity:
  confidence:
  supporting_evidence:
```

### Example

```text
SMB Signing Disabled
```

---

# Hypothesis

## Purpose

A possible explanation supported by available evidence.

### Schema

```yaml
hypothesis:

  id:
  statement:
  confidence:
  supporting_evidence:
  contradicting_evidence:
  status:
```

### Status Values

- Proposed
- Supported
- Weak
- Rejected
- Confirmed

---

# Evidence

## Purpose

Supports Findings and Hypotheses.

### Schema

```yaml
evidence:

  id:
  type:
  source:
  observation_ids:
  artifact_ids:
```

---

# Artifact

## Purpose

A collected object produced or acquired during the Mission.

Artifacts are immutable.

### Schema

```yaml
artifact:

  id:
  filename:
  mime_type:
  sha256:
  location:
```

### Examples

- PCAP
- Screenshot
- Document
- Log File
- Certificate
- Binary

---

# Recommendation

## Purpose

A suggested action based on Mission intelligence.

Recommendations assist the Observer but never execute automatically.

### Schema

```yaml
recommendation:

  id:
  priority:
  action:
  justification:
  supporting_findings:
```

---

# Reference

## Purpose

Represents an external or internal source supporting intelligence.

### Schema

```yaml
reference:

  id:
  type:
  uri:
  description:
```

### Examples

- CVE
- MITRE ATT&CK
- RFC
- Intelligence Report
- Internal Ticket

---

# Timeline Event

## Purpose

Represents a chronological event within a Mission.

Unlike platform Events, Timeline Events describe the progression of a specific investigation.

### Schema

```yaml
timeline_event:

  id:
  timestamp:
  actor:
  action:
  related_objects:
```

---

# Object Relationships

Mission intelligence grows through relationships between objects.

```text
Observation

↓

supports

↓

Evidence

↓

supports

↓

Finding

↓

supports

↓

Recommendation
```

Knowledge is also represented through connected entities.

```text
Observation

↓

identifies

↓

Entity

↓

connected by

↓

Relationship

↓

Knowledge Graph
```

---

# Validation Rules

All intelligence objects should:

- Have a unique identifier
- Include provenance information
- Include confidence where applicable
- Reference supporting evidence when making conclusions
- Be immutable after creation unless versioned

---

# Common Confidence Levels

Suggested confidence values:

- Unknown
- Low
- Medium
- High
- Confirmed

Confidence reflects the quality of supporting evidence.

---

# Common Severity Levels

Where applicable:

- Informational
- Low
- Medium
- High
- Critical

Severity represents impact.

Confidence represents certainty.

---

# Intelligence Flow

```text
Observation

↓

Entity

↓

Relationship

↓

Evidence

↓

Hypothesis

↓

Finding

↓

Recommendation
```

As Missions evolve, intelligence becomes more structured and more actionable.

---

# Summary

Object Models define the common language of intelligence within Trident.

By separating raw observations from interpreted findings and supported recommendations, Trident maintains clear boundaries between data collection, analysis, and decision support.

Every Mission is ultimately composed of these reusable intelligence objects.

---

> **Objects describe intelligence.**

> **Missions organize intelligence.**

> **Mission Updates evolve intelligence.**

🔱