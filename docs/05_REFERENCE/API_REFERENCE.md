# 🌐 API Reference

> **The canonical interface specification for interacting with the Trident Intelligence Operating System.**

---

# Purpose

The Trident API provides a stable, versioned interface for interacting with the platform.

Every interface—CLI, Python SDK, REST API, Desktop UI, or future Web UI—ultimately communicates with the same core platform.

The API is the contract between Trident and everything that uses it.

---

# Philosophy

The API should be:

- Stable
- Predictable
- Versioned
- Consistent
- Extensible
- Language Agnostic

Interfaces may change.

The API contract should not.

---

# Supported Interfaces

```text
Observer
│
├── CLI
├── Python SDK
├── REST API
├── Desktop UI
├── Web UI
└── Extensions
        │
        ▼
Core Platform
```

Every interface exposes the same platform capabilities.

---

# API Principles

The API should:

- Be Mission-centric
- Be Capability-driven
- Return structured data
- Never expose internal implementation details
- Remain backwards compatible within a major version

---

# Versioning

The API follows semantic versioning.

```text
v1

v2

v3
```

Breaking changes require a new major version.

---

# Primary Resources

```text
Mission

Mission Updates

Capabilities

Providers

Extensions

Reports

Events

Packages

Configuration
```

Everything revolves around the Mission.

---

# Mission Operations

## Create Mission

```python
mission = trident.create_mission(
    title="Investigate Suspicious Infrastructure",
    domain="OSINT"
)
```

---

## Load Mission

```python
mission = trident.load_mission(
    mission_id="mission_001"
)
```

---

## Save Mission

```python
mission.save()
```

---

## Archive Mission

```python
mission.archive()
```

---

# Mission Updates

Mission intelligence changes through Mission Updates.

```python
mission.add_update(update)
```

Mission Updates are validated before being applied.

---

# Capability Execution

Execute a capability directly.

```python
result = trident.execute(
    capability="dns.lookup",
    target="example.com"
)
```

---

# Medusa

Allow Medusa to plan an investigation.

```python
plan = trident.medusa.plan(
    mission
)
```

Execute the plan.

```python
trident.medusa.execute(plan)
```

---

# Serpents

Run a specific Serpent.

```python
serpent.execute(
    mission
)
```

Serpents contribute Mission Updates.

They do not modify Mission state directly.

---

# Council

Start collaborative reasoning.

```python
council.deliberate(
    mission
)
```

Council Members produce Mission Updates.

---

# Reporter

Generate reports.

```python
report = reporter.generate(
    mission
)
```

Supported formats:

- Markdown
- HTML
- PDF
- DOCX
- JSON

---

# Provider Access

Providers are accessed through the Provider Layer.

```python
provider = providers.get("openai")

response = provider.chat(...)
```

Components should depend on Provider contracts rather than vendor SDKs.

---

# Capability Registry

Discover capabilities.

```python
registry.list()

registry.search("dns")

registry.resolve("dns.lookup")
```

---

# Package Management

Install packages.

```python
packages.install(
    "trident-osint"
)
```

Upgrade packages.

```python
packages.upgrade()
```

Remove packages.

```python
packages.remove()
```

---

# Event Subscription

Subscribe to operational events.

```python
events.subscribe(
    callback
)
```

Example:

```python
def callback(event):
    print(event.event_type)
```

---

# CLI

Example commands.

Create Mission

```bash
trident mission create
```

List Missions

```bash
trident mission list
```

Run Investigation

```bash
trident mission execute
```

Generate Report

```bash
trident report generate
```

Install Package

```bash
trident package install
```

List Capabilities

```bash
trident capability list
```

---

# REST API (Future)

Example endpoints.

```text
POST   /missions

GET    /missions

GET    /missions/{id}

PATCH  /missions/{id}

POST   /missions/{id}/updates

POST   /reports

GET    /capabilities

GET    /providers

GET    /events

POST   /packages/install
```

REST is one interface among many.

---

# Python SDK

Typical workflow.

```python
from trident import Trident

trident = Trident()

mission = trident.create_mission(
    title="Investigate Domain"
)

plan = trident.medusa.plan(mission)

trident.medusa.execute(plan)

report = trident.reporter.generate(mission)
```

---

# Return Types

Operations should return structured objects.

Example:

```python
Mission

MissionUpdate

Report

CapabilityResult

ProviderResponse

Event
```

Avoid returning unstructured dictionaries whenever possible.

---

# Error Handling

Errors should be descriptive.

Example:

```python
MissionNotFound

CapabilityNotFound

ProviderUnavailable

PermissionDenied

ValidationError

PackageSignatureError
```

Errors should communicate both the problem and potential resolution.

---

# Authentication

Future enterprise deployments may support:

- API Keys
- OAuth
- OpenID Connect
- Service Accounts

The core platform remains authentication-agnostic.

---

# Pagination

Collection endpoints should support:

```text
page

page_size

cursor
```

Cursor-based pagination is recommended for large datasets.

---

# Filtering

Resources should support filtering.

Example:

```text
status=completed

domain=osint

priority=high
```

---

# Sorting

Resources should support sorting.

```text
created_at

updated_at

priority

confidence
```

---

# Best Practices

- Interact with Missions rather than internal components.
- Use Mission Updates to change intelligence.
- Prefer Capabilities over direct Provider calls.
- Treat the API as the stable contract.
- Build against interfaces, not implementations.

---

# Summary

The Trident API provides a consistent, versioned interface for every interaction with the Intelligence Operating System.

Whether through the CLI, Python SDK, REST API, or future graphical interfaces, every operation ultimately interacts with the same Mission-centric platform.

---

> **One Platform.**

> **Many Interfaces.**

> **One Contract.**

🔱