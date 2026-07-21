# TridentIOS Planner v2

## Status

**Design Phase**

---

# Mission

Transform the TridentIOS Planner from a predefined capability sequence into an observation-driven investigation planner.

Planner v2 examines the current mission intelligence and recommends the most valuable capability to execute next.

The planner does **not** execute tools.

---

# Core Principle

The Planner recommends capabilities.

Execution remains the responsibility of the existing architecture.

```text
Planner
    ↓
Recommendation
    ↓
Capability Router
    ↓
Capability
    ↓
Weapon
    ↓
Sensor
    ↓
Adapter
    ↓
Translator
    ↓
Observation Emitter
```

---

# Inputs

Planner v2 may inspect:

- Mission target
- Mission state
- Existing observations
- Known entities
- Known relationships
- Open ports
- Running services
- Web applications
- Virtual hosts
- Previous capability executions
- Failed recommendations
- Deferred recommendations

---

# Outputs

The planner produces one or more ranked recommendations.

Example:

```yaml
capability_id: virtual-host-discovery

priority: High

confidence: 0.92

reason: >
  HTTP service and hostname redirect observed.
  Virtual host enumeration has not yet been completed.

evidence:
  - HTTP service detected
  - Redirect contains hostname
```

---

# Recommendation Model

Every recommendation should contain:

- capability_id
- priority
- confidence
- reason
- evidence
- scope
- created_at
- status

Recommended statuses:

- pending
- accepted
- running
- completed
- failed
- deferred
- dismissed

---

# Planning Rules

## HTTP Fingerprinting

If an HTTP service exists and fingerprinting has not yet been performed:

```text
Recommend:
http-fingerprinting
```

---

## Virtual Host Discovery

If an HTTP service exists and a hostname or redirect has been observed:

```text
Recommend:
virtual-host-discovery
```

---

## Directory Discovery

If a web application exists and directory discovery has not been completed for that scope:

```text
Recommend:
directory-discovery
```

---

## Header Collection

If HTTP response headers have not yet been preserved:

```text
Recommend:
http-header-collection
```

---

## Artifact Collection

If an interesting endpoint or page is discovered:

```text
Recommend:
http-artifact-collection
```

---

# Scope Awareness

Every recommendation belongs to a specific scope.

Examples:

```text
10.129.36.93

bedside.htb

research.bedside.htb

http://research.bedside.htb/uploads/
```

Capabilities completed against one scope should **not** automatically apply to every other scope.

---

# Duplicate Prevention

Planner v2 should not repeatedly recommend the same capability when:

- already completed
- currently running
- explicitly dismissed
- evidence has not changed

Recommendations may be regenerated when:

- new observations appear
- scope expands
- previous execution failed
- mission intelligence changes

---

# Stopping Conditions

The planner stops recommending work when:

- no remaining recommendations exceed the confidence threshold
- every applicable capability has completed
- operator approval is required
- mission has completed

Stopping does **not** imply the investigation is finished.

It only means there is currently insufficient evidence to justify another automated action.

---

# Confidence

Suggested confidence levels:

| Confidence | Meaning |
|------------|---------|
| 0.90–1.00 | Direct evidence |
| 0.70–0.89 | Strong evidence |
| 0.50–0.69 | Moderate evidence |
| Below 0.50 | Do not automatically recommend |

---

# Priority

Recommended priorities:

- Critical
- High
- Medium
- Low

Priority represents investigative value.

It does **not** represent vulnerability severity.

---

# Planning Loop

```text
Load Mission
      ↓
Review Observations
      ↓
Identify Missing Intelligence
      ↓
Match Intelligence Gaps
to Capabilities
      ↓
Remove Duplicate Work
      ↓
Rank Recommendations
      ↓
Return Recommendations
      ↓
Capability Executes
      ↓
New Observations Created
      ↓
Repeat
```

---

# Bedside Example

Current observations:

- Port 80 open
- Apache detected
- Redirect to bedside.htb
- bedside.htb discovered
- research.bedside.htb discovered

Planner output:

```text
HTTP Service
      ↓
HTTP Fingerprinting

Hostname Found
      ↓
Virtual Host Discovery

New VHost
      ↓
HTTP Fingerprinting

Fingerprint Complete
      ↓
Directory Discovery

Interesting Surface
      ↓
Artifact Collection
```

---

# Non-Goals

Planner v2 does **not**:

- generate shell commands
- invoke tools directly
- bypass the Capability Router
- modify observations
- rewrite historical evidence
- convert hypotheses into facts
- perform unrestricted autonomous execution

---

# Implementation Roadmap

## Phase 1

- Recommendation model
- Recommendation statuses
- Scope awareness
- Duplicate prevention

---

## Phase 2

- Deterministic planning rules
- Ranked recommendations
- Confidence scoring
- Human-readable reasoning

---

## Phase 3

- Recursive planning
- Recommendation history
- Stopping conditions
- Planner memory

---

## Phase 4

- Observation weighting
- Operator feedback
- Mission learning
- Adaptive recommendation scoring

---

# Success Criteria

Planner v2 is complete when:

- Recommendations are generated from observations.
- Recommendations reference capability IDs only.
- Every recommendation explains *why* it exists.
- Duplicate work is prevented.
- Recommendations are scoped correctly.
- New observations automatically generate new investigative opportunities.
- Existing execution architecture remains unchanged.

---

# Vision

Planner v1 answered:

> "What capability comes next?"

Planner v2 answers:

> "Given everything we currently know, what is the most valuable question to answer next, and which capability can answer it?"

That shift transforms TridentIOS from a capability runner into an investigation engine.