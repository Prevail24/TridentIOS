# 🐍 Building Serpents

> **Designing specialized intelligence capabilities for the Trident Intelligence Operating System.**

---

# Purpose

Serpents are Trident's specialists.

Each Serpent performs a focused intelligence responsibility.

Examples include:

- Network Enumeration
- DNS Analysis
- WHOIS Collection
- Certificate Inspection
- Malware Classification
- OSINT Collection
- HTTP Fingerprinting
- Port Scanning

A Serpent should solve one problem exceptionally well.

---

# Philosophy

Serpents do not investigate.

Serpents do not orchestrate.

Serpents do not reason.

Serpents perform one specialized task and report what they discover.

Think of a Serpent as a highly trained investigator with a single area of expertise.

---

# Responsibilities

A Serpent should:

- Receive scoped Mission Context
- Execute a capability
- Validate collected information
- Produce Mission Updates
- Publish operational Events
- Return control to Medusa

A Serpent should never:

- Modify Mission state directly
- Schedule work
- Choose the next capability
- Promote knowledge into Loom
- Generate final reports

---

# The Serpent Lifecycle

```text
Mission Assigned

↓

Mission Context Received

↓

Capability Executed

↓

Mission Updates Produced

↓

Events Published

↓

Execution Completed
```

Every Serpent follows the same lifecycle.

---

# Design Principles

Every Serpent should be:

- Focused
- Deterministic where possible
- Explainable
- Testable
- Replaceable
- Provider-independent
- Stateless whenever practical

---

# One Responsibility

Good:

```text
DNS Enumeration
```

Bad:

```text
DNS + HTTP + AI Analysis + Reporting
```

Large responsibilities should be divided into multiple Serpents.

---

# Mission Context

Serpents receive only the information required for execution.

Example:

```python
def execute(context):
    ...
```

Context may include:

- Mission ID
- Current objective
- Target scope
- Configuration
- Providers
- Logger
- Permissions

Context should never expose unnecessary Mission intelligence.

---

# Provider Usage

Serpents interact with external systems through Providers.

Example:

```python
shodan = providers.get("shodan")
```

Never call external APIs directly.

The Provider Layer isolates vendor-specific logic.

---

# Producing Mission Updates

Mission intelligence is communicated through Mission Updates.

Example:

```python
MissionUpdate(
    type="Observation",
    summary="SSH service detected",
    confidence="High",
    payload={}
)
```

Mission Updates are the only mechanism for contributing intelligence.

---

# Publishing Events

Operational state should be communicated through Events.

Example:

```python
events.publish(
    "Capability.Execution.Completed"
)
```

Events describe execution.

Mission Updates describe intelligence.

---

# Error Handling

Recoverable failures should produce operational Events.

Example:

```text
ProviderUnavailable

↓

RetryScheduled
```

Do not silently ignore failures.

---

# Logging

Log meaningful operational information.

Good:

```text
Beginning DNS enumeration.
```

Bad:

```text
Running...
```

Logs should help operators understand execution.

---

# Configuration

Configuration should be injected.

Example:

```python
context.config.timeout
```

Do not read configuration files directly.

---

# Permissions

Only request permissions required for execution.

Good:

```yaml
permissions:
  - network.http
```

Bad:

```yaml
permissions:
  - *
```

Least privilege improves security.

---

# Testing

Every Serpent should support:

- Unit Tests
- Mock Providers
- Mock Mission Context
- Contract Validation
- Replay Testing

A Serpent should be testable without running the full platform.

---

# Performance

Prefer:

- Predictable runtime
- Bounded resource usage
- Configurable concurrency

Avoid:

- Infinite retries
- Blocking operations
- Unbounded memory usage

---

# AI Usage

If a Serpent uses AI:

Treat AI output as observations.

Never assume AI is correct.

AI should assist investigation.

It should not define truth.

---

# Good Serpent Example

```text
TLS Certificate Inspector

Responsibility:

Retrieve certificates

Extract metadata

Produce observations

Return
```

---

# Poor Serpent Example

```text
Network Analyzer

Runs Nmap

Calls OpenAI

Writes Reports

Stores Knowledge

Schedules Tasks

Emails Results
```

This combines multiple architectural responsibilities.

---

# Naming

Serpent names should describe responsibilities.

Good:

- DNS Enumerator
- HTTP Fingerprinter
- ASN Resolver
- WHOIS Collector
- TLS Inspector

Avoid vague names.

---

# Mission Boundaries

Remember:

Serpents contribute intelligence.

They do not own intelligence.

The Mission owns intelligence.

---

# Common Mistakes

Avoid:

- Direct Mission modification
- Calling external APIs directly
- Hidden configuration
- Global state
- Multiple unrelated responsibilities
- Vendor-specific assumptions

---

# Best Practices

Keep Serpents:

- Small
- Focused
- Explainable
- Easy to replace
- Easy to test

Prefer multiple simple Serpents over one complex Serpent.

---

# Example Execution

```text
Mission

↓

Medusa

↓

Capability Registry

↓

DNS Enumeration Serpent

↓

Mission Update

↓

Mission
```

The Serpent executes only its assigned responsibility.

---

# Summary

Serpents are Trident's specialists.

Each Serpent performs one focused intelligence capability.

Serpents receive scoped context, execute their capability, produce Mission Updates, publish operational Events, and return control to the platform.

Well-designed Serpents are simple, testable, reusable, and provider-independent.

---

> **One Serpent.**

> **One Responsibility.**

> **One Contribution to the Mission.**

🔱