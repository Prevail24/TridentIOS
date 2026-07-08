# Technique Specification

## Purpose

A Technique is a reusable investigative method.

Unlike an Observation, which records what happened during a specific investigation, a Technique captures a repeatable approach that can be applied across many investigations.

Techniques are intended to evolve as they are tested and refined.

---

## Technique ID Format

```text
TECH-0001
```

Rules:

- IDs are permanent.
- Techniques are never deleted; they are archived when obsolete.
- Revisions preserve history rather than replacing it.

---

## Required Metadata

Every Technique should include:

```text
Technique ID
Title
Status
Category
Difficulty
Created
Updated
Reliability
Related Tools
Related Observations
Related Playbooks
Tags
```

---

## Reliability

Reliability reflects real-world experience gathered from Observations.

Track:

- Times Used
- Successful Uses
- Partial Successes
- Failed Uses

Reliability should improve through evidence, not opinion.

---

## Core Sections

### Purpose

What problem does this technique solve?

### When to Use

Describe the situations where this technique is appropriate.

### Prerequisites

List the information or artifacts needed before applying the technique.

### Procedure

Document the repeatable workflow step by step.

### Expected Outcomes

Describe what success looks like.

### Strengths

Where this technique performs well.

### Weaknesses

Known limitations.

### Common Mistakes

Frequent investigator errors when applying this technique.

### Success Indicators

Observable signs that the technique is producing useful results.

### Related Knowledge

Reference:

- Related Observations
- Related Tools
- Related Playbooks

---

## Evolution Rule

A Technique should become better over time as new Observations validate, refine, or challenge it.

Every meaningful improvement should be recorded in its revision history.

---

## Design Principle

A Technique represents institutional knowledge.

It should answer:

> 'If another Observer faced the same problem tomorrow, what repeatable method would give them the best chance of success?'
