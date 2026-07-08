# Observation Specification

## Purpose

An Observation is the core knowledge unit of TridentIOS.

Every investigation, CTF challenge, case, or research session should become an Observation.

The goal is not only to solve the challenge.  
The goal is to preserve what was learned.

---

## Observation ID Format

Use this format:

```text
OBS-YYYY-0001
```

Example:

```text
OBS-2026-0001
```

Rules:

- IDs are never reused.
- IDs are never renamed.
- Completed Observations remain in the archive.
- Revisions are appended, not overwritten.

---

## Required Fields

Every Observation must include:

```text
Observation ID
Title
Date Started
Status
Platform
Category
Summary
Scope
Confirmed Evidence
Pivots Attempted
Final Outcome
Lessons Learned
```

---

## Status Values

```text
active
solved
unsolved
paused
archived
```

---

## Core Sections

### 1. Case Information

Basic identifying information.

### 2. Scope

Defines what is authorized and what is out of bounds.

### 3. Initial Clues

Everything visible before research begins.

### 4. Evidence

Only confirmed facts.

### 5. Pivots

Every search path attempted.

### 6. Timeline

Important events, discoveries, and sequence.

### 7. Tools Used

Tools used during the investigation.

### 8. Techniques Used

Methods used during the investigation.

### 9. Dead Ends

Failed searches and false leads.

### 10. Hypotheses

Working theories with confidence levels.

### 11. Final Outcome

Flag, answer, or conclusion.

### 12. Lessons Learned

What should improve future investigations.

### 13. Playbook Updates

Recommended changes to TridentIOS playbooks.

### 14. Observer Journal

Human reflection from the investigation.

---

## Evidence Rules

Evidence must be:

- observable
- reproducible
- sourced
- timestamped when possible

Never mark guesses as evidence.

---

## Confidence Scale

```text
★☆☆☆☆ Very weak
★★☆☆☆ Possible
★★★☆☆ Plausible
★★★★☆ Strong
★★★★★ Confirmed
```

---

## Link Rules

Observations can reference:

```text
TECH-0001
TOOL-0001
PLAYBOOK-image-geolocation
OBS-2026-0002
```

This allows the archive to become searchable and connected over time.

---

## Revision Rule

TridentIOS knowledge is append-only.

Do not erase history.

When something changes, add a revision note:

```text
Revision:
Date:
Changed:
Reason:
Related Observation:
```

---

## Completion Rule

An Observation is not complete when the flag is found.

An Observation is complete when:

- the final answer is recorded
- evidence is preserved
- dead ends are logged
- lessons are captured
- playbook updates are identified
- the next Observer can solve faster