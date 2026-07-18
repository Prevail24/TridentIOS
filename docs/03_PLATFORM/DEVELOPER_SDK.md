# 🧰 Trident SDK

> **The Software Development Kit for building extensions on the Trident Intelligence Operating System.**

---

# Purpose

The Trident SDK provides the libraries, interfaces, tooling, and developer experience required to build extensions for the Trident platform.

It abstracts platform complexity while preserving architectural contracts.

Developers should focus on intelligence, not infrastructure.

---

# Philosophy

Writing a Trident extension should feel simple.

The SDK should handle:

- Registration
- Configuration
- Validation
- Mission communication
- Event publication
- Logging
- Provider interaction
- Error handling

Developers should write capabilities.

The SDK should handle the platform.

---

# Goals

The SDK should provide:

- Simple APIs
- Strong typing
- Stable contracts
- Excellent documentation
- Testing utilities
- Local development tools
- Debugging support
- Package generation

The SDK should make the correct approach the easiest approach.

---

# Responsibilities

The SDK is responsible for:

- Extension development
- Capability registration
- Mission Update creation
- Event publication
- Provider interaction
- Configuration loading
- Permission helpers
- Logging
- Testing
- Packaging support

The SDK is not responsible for platform orchestration.

---

# Supported Extension Types

The SDK supports building:

- Serpents
- Providers
- Council Members
- Reporter Extensions
- Loom Adapters
- Domain Packs

Every extension follows the same architectural principles.

---

# Developer Workflow

A typical development workflow looks like:

```text
Create Project

↓

Implement Extension

↓

Run Tests

↓

Validate Contracts

↓

Package Extension

↓

Install

↓

Execute Mission
```

---

# Project Structure

Example:

```text
my-serpent/

├── manifest.yaml
├── pyproject.toml
├── README.md
├── src/
│   └── my_serpent/
│       ├── __init__.py
│       ├── extension.py
│       └── handlers.py
├── tests/
└── examples/
```

The SDK encourages consistency across projects.

---

# Creating an Extension

Example CLI:

```bash
trident create serpent network-enumeration
```

Result:

```text
network-enumeration/

manifest.yaml

src/

tests/

README.md
```

Developers start with working templates instead of empty folders.

---

# Base Classes

The SDK provides base classes for each extension type.

Examples:

```python
Serpent

Provider

CouncilMember

Reporter

LoomAdapter
```

Base classes implement common platform behavior.

---

# Extension Manifest

Every extension includes:

```yaml
id:
name:
version:
type:
capabilities:
permissions:
```

The SDK validates manifests automatically.

---

# Context Objects

Extensions never access the Mission directly.

Instead they receive scoped context.

Example:

```python
def execute(context):
    ...
```

Context may provide:

- Mission metadata
- Current task
- Configuration
- Providers
- Logger
- Permission information

Context should expose only what the extension requires.

---

# Mission Updates

The SDK provides builders for Mission Updates.

Example:

```python
update = MissionUpdate(
    type="Observation",
    summary="Discovered SSH service",
    confidence="High",
    payload={}
)
```

The SDK validates updates before submission.

---

# Event Publishing

Operational events are published through the SDK.

Example:

```python
events.publish(
    "Capability.Completed"
)
```

Extensions should never communicate directly with the Event Bus.

---

# Provider Access

Extensions request Providers through the SDK.

Example:

```python
vt = providers.get("virustotal")
```

The SDK resolves the implementation.

Extensions remain provider-independent.

---

# Configuration

Configuration is injected automatically.

Example:

```python
config.timeout

config.api_endpoint

config.max_results
```

Extensions should not parse configuration files directly.

---

# Logging

The SDK provides structured logging.

Example:

```python
logger.info("Beginning enumeration")
```

Logs automatically include:

- Mission ID
- Extension ID
- Correlation ID
- Timestamp

---

# Permissions

Extensions may query granted permissions.

Example:

```python
permissions.has("network.http")
```

Permission enforcement remains the responsibility of the platform.

---

# Errors

The SDK provides standard exception types.

Examples:

```python
ProviderError

PermissionError

ValidationError

ConfigurationError
```

Consistent errors improve debugging.

---

# Validation

The SDK validates:

- Manifests
- Mission Updates
- Events
- Package metadata
- Contracts

Validation occurs before runtime whenever possible.

---

# Testing

Testing utilities include:

- Mock Mission Context
- Mock Providers
- Mock Events
- Mock Loom
- Contract Validators

Extensions should be testable without running the entire platform.

---

# Local Development

Example:

```bash
trident dev
```

Starts:

- Local runtime
- Test Mission
- Debug logging
- Hot reload

The SDK should shorten the development cycle.

---

# Packaging

The SDK assists with package creation.

Example:

```bash
trident package build
```

Produces a validated Trident package.

---

# Documentation

The SDK should generate documentation from:

- Extension manifests
- Type annotations
- Capability declarations

Documentation should stay synchronized with implementation.

---

# Versioning

The SDK follows Semantic Versioning.

Breaking changes require major version increments.

Older extensions should continue functioning whenever practical.

---

# Compatibility

The SDK should verify compatibility with:

- Platform version
- Contract versions
- Package requirements

Compatibility should be checked before deployment.

---

# Best Practices

Extensions should:

- Declare minimal permissions
- Publish meaningful Mission Updates
- Emit operational Events
- Remain stateless where possible
- Validate external input
- Avoid direct provider dependencies
- Keep capabilities focused

The SDK should encourage these practices by default.

---

# Example Lifecycle

```text
Developer

↓

SDK Template

↓

Implement Capability

↓

SDK Validation

↓

Package Build

↓

Platform Install

↓

Mission Execution
```

The SDK bridges the gap between developers and the platform.

---

# Future Vision

Future SDK capabilities may include:

- Interactive project generators
- Visual debugging tools
- Mission simulators
- Package publishing
- Contract migration tools
- AI-assisted extension scaffolding
- IDE plugins
- Language support beyond Python

The SDK should evolve while preserving stable architectural contracts.

---

# Summary

The Trident SDK is the primary interface between developers and the Trident Intelligence Operating System.

It simplifies extension development through stable APIs, reusable tooling, validation, testing, and packaging support.

Developers focus on solving intelligence problems.

The SDK handles platform integration.

---

> **Build intelligence.**

> **The SDK handles the platform.**

> **The Platform handles the Mission.**

🔱