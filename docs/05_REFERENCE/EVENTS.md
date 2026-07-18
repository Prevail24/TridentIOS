# 📡 Events Reference

> **The canonical catalog of operational events within the Trident Intelligence Operating System.**

---

# Purpose

Events communicate operational activity occurring within Trident.

They allow components to observe platform behavior without creating tight coupling.

Events describe **what happened**.

They do not represent Mission intelligence.

---

# Philosophy

Events answer questions such as:

- What just started?
- What completed?
- What failed?
- What changed operationally?

Mission Updates answer:

- What was learned?

The distinction is fundamental.

---

# Event Characteristics

Every Event is:

- Immutable
- Timestamped
- Versioned
- Replayable
- Observable
- Traceable

Events are part of operational history.

---

# Event Schema

```yaml
event:

  event_version:

  event_id:

  event_type:

  timestamp:

  source:

  subject:

  mission_id:

  correlation_id:

  causation_id:

  severity:

  payload:

  metadata:
```

---

# Core Fields

| Field | Description |
|--------|-------------|
| event_id | Globally unique identifier |
| event_type | Canonical event name |
| timestamp | UTC creation time |
| source | Component producing the event |
| mission_id | Associated Mission (optional) |
| correlation_id | Links related operations |
| causation_id | References triggering event |
| payload | Event-specific data |

---

# Event Categories

```text
Mission
Medusa
Capability Registry
Serpent
Provider
Council
Reporter
Loom
Extension
Package
Security
Observer
System
```

Each category owns its own event namespace.

---

# Mission Events

Examples:

```text
Mission.Created

Mission.Started

Mission.Planning

Mission.Executing

Mission.Reasoning

Mission.Reporting

Mission.Completed

Mission.Archived

Mission.Cancelled

Mission.Failed
```

Mission lifecycle only.

No intelligence.

---

# Medusa Events

```text
Medusa.Planning.Started

Medusa.Planning.Completed

Medusa.Capability.Selected

Medusa.Execution.Started

Medusa.Execution.Completed
```

These describe orchestration.

---

# Capability Registry Events

```text
Capability.Registered

Capability.Unregistered

Capability.Discovered

Capability.Validated

Capability.Resolved
```

Registry behavior only.

---

# Serpent Events

```text
Serpent.Started

Serpent.Completed

Serpent.Failed

Serpent.Timeout

Serpent.PermissionDenied
```

Operational execution.

Not findings.

---

# Provider Events

```text
Provider.Initialized

Provider.Authenticated

Provider.Request.Started

Provider.Request.Completed

Provider.Request.Failed

Provider.RateLimited

Provider.Unavailable
```

These monitor integrations.

---

# Council Events

```text
Council.Started

Council.Member.Started

Council.Member.Completed

Council.Member.Failed

Council.Completed
```

Reasoning execution only.

---

# Reporter Events

```text
Reporter.Started

Reporter.Report.Generated

Reporter.Report.Delivered

Reporter.Completed

Reporter.Failed
```

Presentation events.

---

# Loom Events

```text
Loom.Candidate.Created

Loom.Knowledge.Validated

Loom.Knowledge.Promoted

Loom.Knowledge.Rejected
```

Knowledge lifecycle.

---

# Extension Events

```text
Extension.Loaded

Extension.Enabled

Extension.Disabled

Extension.Unloaded

Extension.Upgraded
```

Extension management.

---

# Package Events

```text
Package.Downloaded

Package.Verified

Package.Installed

Package.Upgraded

Package.Removed
```

Package lifecycle.

---

# Security Events

```text
Security.AuthenticationFailed

Security.AuthorizationDenied

Security.PermissionViolation

Security.SignatureFailed

Security.SecretAccessed

Security.Quarantined
```

Critical security activity.

---

# Observer Events

```text
Observer.Login

Observer.Logout

Observer.MissionCreated

Observer.Approved

Observer.Rejected
```

Human interaction.

---

# System Events

```text
System.Startup

System.Shutdown

System.Backup

System.Restore

System.ConfigurationChanged
```

Platform lifecycle.

---

# Event Flow

```text
Observer

↓

Mission.Created

↓

Medusa.Planning.Started

↓

Capability.Selected

↓

Serpent.Started

↓

Provider.Request.Started

↓

Provider.Request.Completed

↓

Serpent.Completed

↓

Council.Started

↓

Reporter.Generated

↓

Mission.Completed
```

Notice that no Mission Updates appear here.

Those belong to Mission intelligence.

---

# Correlation IDs

Every investigation should maintain a correlation ID.

Example:

```text
Mission

↓

Medusa

↓

Serpent

↓

Provider

↓

Reporter
```

Every Event can be linked together.

---

# Severity Levels

Suggested values:

```text
Debug

Info

Notice

Warning

Error

Critical
```

Severity reflects operational importance.

---

# Delivery

Events may be published through:

- Internal Event Bus
- Message Queue
- WebSocket
- REST Webhooks
- Logging
- Streaming Infrastructure

The transport is independent of the Event contract.

---

# Ordering

Ordering should be preserved whenever possible.

If ordering cannot be guaranteed, Events must include sufficient timestamps and correlation information to reconstruct execution.

---

# Replay

Events should support replay for:

- Debugging
- Auditing
- Analytics
- Monitoring
- Performance analysis

Replaying Events must never modify Mission intelligence.

---

# Versioning

Events are versioned independently.

Breaking schema changes require a new event version.

Consumers should validate supported versions.

---

# Best Practices

Events should be:

- Small
- Immutable
- Self-describing
- Versioned
- Observable

An Event should communicate one meaningful occurrence.

---

# Anti-Patterns

Avoid:

- Embedding large datasets
- Business logic
- Mission intelligence
- Sensitive secrets
- Provider-specific objects

Events should remain operational.

---

# Events vs Mission Updates

| Mission Updates | Events |
|-----------------|--------|
| Intelligence | Operations |
| Change Mission state | Never change Mission state |
| Permanent investigation record | Operational history |
| Used for reasoning | Used for monitoring |
| Consumed by Mission | Consumed by infrastructure |

Understanding this distinction is essential to understanding Trident.

---

# Summary

Events describe everything the platform does while remaining separate from the intelligence it produces.

They provide observability, traceability, replayability, and loose coupling across the Trident ecosystem.

Mission Updates preserve what was learned.

Events preserve how the platform behaved.

---

> **Mission Updates tell the story of the investigation.**

> **Events tell the story of the platform.**

🔱