# 🤝 Contributing to Trident

> **Build intelligence, not complexity.**

Thank you for contributing to the Trident Intelligence Operating System.

Trident is an open platform designed to help humans investigate complex problems through structured intelligence, specialized capabilities, and explainable AI.

This document explains how to contribute in a way that preserves the architecture, philosophy, and long-term vision of the project.

---

# Before You Write Code

Every contribution should begin with a question:

> **Which architectural responsibility owns this?**

If you cannot answer that question, do not start writing code.

Architecture comes first.

Implementation comes second.

---

# Our Philosophy

Trident is designed around a small set of principles:

- Single Responsibility
- Explicit Contracts
- Loose Coupling
- Explainability
- Replayability
- Human Authority
- Extensibility

Every pull request should reinforce these principles.

---

# The Golden Rule

Do not ask:

> "Where can I put this code?"

Ask:

> "Who should own this responsibility?"

Ownership matters more than location.

---

# The Architecture

Before contributing, read these documents in order:

1. Manifesto
2. Principles
3. Philosophy
4. Architecture Roadmap
5. Architecture
6. Mission Model
7. Intelligence Model

Understanding the architecture is more important than understanding the implementation.

---

# Areas of Contribution

Trident welcomes contributions in many forms.

Examples include:

- Serpents
- Providers
- Council Members
- Reporter Extensions
- Domain Packs
- Documentation
- Testing
- Performance
- Developer Tooling
- SDK Improvements
- Bug Fixes

Every contribution should align with the architecture.

---

# What We Value

We value:

- Clear architecture
- Readable code
- Small focused pull requests
- Good documentation
- Strong testing
- Explainable behavior
- Long-term maintainability

We optimize for clarity over cleverness.

---

# What We Avoid

Avoid introducing:

- Hidden coupling
- Global state
- Platform-specific assumptions
- Undocumented behavior
- Implicit contracts
- Architecture bypasses

Shortcuts become technical debt.

---

# Design Before Code

Large contributions should begin with a design discussion.

Describe:

- The problem
- The proposed responsibility
- The architectural impact
- Alternative approaches
- Trade-offs

Architecture should guide implementation.

---

# Coding Style

Contributors should prefer:

- Small functions
- Clear names
- Explicit types
- Predictable behavior
- Minimal side effects

Code should be understandable six months later.

---

# Mission First

Remember:

Extensions do not modify Mission state directly.

Extensions produce Mission Updates.

The Mission determines what becomes operational truth.

Respect this boundary.

---

# Events

Operational changes should be communicated through Events.

Do not use Events to communicate intelligence.

Use Mission Updates.

---

# Providers

Providers isolate external systems.

Do not embed vendor-specific logic inside Serpents or Council Members.

Keep integrations behind Provider contracts.

---

# Extensions

Extensions should remain:

- Focused
- Independent
- Versioned
- Testable
- Replaceable

One extension should solve one responsibility well.

---

# Security

Every contribution should follow the Security Model.

Prefer:

- Least privilege
- Explicit permissions
- Input validation
- Safe defaults

Security reviews are encouraged.

---

# Documentation

If architecture changes, documentation should change first.

A pull request that changes behavior without updating documentation is incomplete.

Documentation is part of the platform.

---

# Testing

Every contribution should include appropriate tests.

Examples include:

- Unit tests
- Contract tests
- Integration tests
- Replay tests

Reliable intelligence requires reliable software.

---

# Pull Requests

A good pull request should answer:

- What problem does this solve?
- Why is this change needed?
- Which architectural component owns it?
- Does it introduce new contracts?
- Does it preserve existing ones?

Smaller pull requests are easier to review.

---

# Review Philosophy

Reviews focus on:

- Correctness
- Simplicity
- Architectural consistency
- Security
- Maintainability

Feedback improves the platform.

It is never personal.

---

# Breaking Changes

Breaking changes require:

- Clear justification
- Documentation updates
- Migration guidance
- Version changes

Platform stability is a priority.

---

# Commit Messages

Prefer descriptive commits.

Example:

```text
Add DNS enumeration Serpent

Improve Mission Update validation

Refactor Provider registration
```

Avoid generic messages such as:

```text
Fix stuff

Updates

Changes
```

---

# Code of Conduct

Treat everyone with respect.

Assume good intentions.

Be patient.

Teach generously.

Learn continuously.

The community is as important as the code.

---

# The Long View

Trident is designed to grow for years.

Every contribution should make the platform:

- Simpler
- Clearer
- More reliable
- More understandable

We are building an operating system for intelligence, not a collection of scripts.

---

# Summary

Contributing to Trident means contributing to an architecture.

Every new capability should strengthen the platform rather than complicate it.

Think in responsibilities.

Respect contracts.

Keep components loosely coupled.

Preserve the Observer's authority.

Build systems that help humans investigate the unknown.

---

> **Architecture first.**

> **Code second.**

> **Intelligence always.**

🔱