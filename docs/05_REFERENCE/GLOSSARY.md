# 📚 Trident Glossary

> **The canonical vocabulary of the Trident Intelligence Operating System.**

---

# Purpose

This glossary defines the official terminology used throughout Trident.

Every architectural document, API, extension, and contribution should use these definitions consistently.

When multiple terms could describe the same concept, this glossary establishes the preferred language.

---

# A

## Artifact

A piece of evidence collected during a Mission.

Examples include:

- Files

- Screenshots

- Network captures

- Certificates

- Documents

- Logs

Artifacts are immutable once recorded.

---

# C

## Capability

A specific piece of functionality that can be executed within Trident.

Examples:

- DNS Lookup

- WHOIS

- HTTP Scan

- AI Summarization

- Malware Analysis

Capabilities are requested by responsibility rather than implementation.

---

## Capability Registry

The platform component responsible for discovering, validating, registering, and resolving Capabilities.

Consumers request capabilities.

The Registry selects implementations.

---

## Council

A collection of reasoning specialists that interpret Mission intelligence from different perspectives.

Council Members gather no intelligence themselves.

---

## Council Member

A reasoning specialist with a defined analytical perspective.

Examples:

- Threat Analyst

- Risk Analyst

- OSINT Analyst

- Devil's Advocate

---

# E

## Entity

A meaningful object identified during a Mission.

Examples:

- Person

- Organization

- Domain

- IP Address

- Host

- Email Address

Entities may be connected through Relationships.

---

## Event

An immutable record describing something that occurred within the platform.

Events communicate operational activity.

They are distinct from Mission Updates.

---

## Evidence

Information supporting a Finding or Hypothesis.

Evidence increases confidence in Mission intelligence.

---

## Extension

A modular component that extends Trident without modifying the core platform.

Examples include:

- Serpents

- Providers

- Council Members

- Reporters

---

# F

## Finding

A validated conclusion derived from Mission intelligence.

Findings are stronger than Observations and may support Recommendations.

---

# H

## Hypothesis

A possible explanation supported by available evidence but not yet confirmed.

Hypotheses evolve as additional intelligence is collected.

---

# I

## Intelligence

Structured knowledge accumulated during a Mission.

Intelligence consists of:

- Observations

- Entities

- Relationships

- Findings

- Evidence

- Hypotheses

- Recommendations

---

# L

## Loom

Trident's institutional knowledge system.

Loom stores validated knowledge that can assist future Missions.

Unlike Missions, Loom persists across investigations.

---

# M

## Medusa

The orchestration engine of Trident.

Medusa plans investigations, coordinates execution, and delegates work to Capabilities.

Medusa does not perform intelligence gathering directly.

---

## Mission

The central object within Trident.

A Mission represents a single investigation.

All intelligence belongs to exactly one Mission.

The Mission is the operational source of truth.

---

## Mission Context

The scoped information provided to a component while executing within a Mission.

Mission Context ensures components only access information relevant to their responsibilities.

---

## Mission Update

An immutable contribution to Mission intelligence.

Mission Updates are the only mechanism through which Mission intelligence changes.

---

# O

## Observation

A recorded fact collected during an investigation.

Observations are raw intelligence.

They may later support Findings or Hypotheses.

---

## Observer

The human directing a Mission.

The Observer defines objectives, reviews intelligence, and remains the final decision-maker.

---

# P

## Package

A distributable unit containing one or more Extensions.

Packages may include manifests, configuration, documentation, and signatures.

---

## Provider

An integration layer connecting Trident to external systems.

Providers handle authentication, communication, normalization, retries, and security.

Providers do not generate intelligence.

---

# R

## Recommendation

A suggested course of action derived from Mission intelligence.

Recommendations assist the Observer but do not make decisions.

---

## Relationship

A structured connection between two or more Entities.

Examples:

- Owns

- Hosts

- Resolves To

- Communicates With

- Registered By

---

## Reporter

A presentation specialist responsible for transforming Mission intelligence into human-readable outputs.

Reporters do not perform investigations.

---

# S

## Serpent

A specialist responsible for gathering intelligence.

Serpents execute Capabilities and contribute Mission Updates.

Each Serpent should own a single responsibility.

---

# T

## Trust Level

A classification indicating the level of confidence placed in an Extension.

Example levels include:

- Core

- Trusted

- Verified

- Community

- Untrusted

---

# V

## Validation

The process of verifying that data, packages, Mission Updates, or Extensions conform to platform contracts.

Validation protects platform integrity.

---

# Canonical Principles

Throughout Trident, remember these distinctions:

Mission ≠ Event

Mission Update ≠ Event

Capability ≠ Provider

Provider ≠ Serpent

Council ≠ AI Model

Reporter ≠ Intelligence

Loom ≠ Mission

Observer ≠ Automation

Understanding these boundaries is essential to understanding Trident.

---

# Summary

Trident uses precise terminology to maintain architectural clarity.

A shared vocabulary reduces ambiguity, improves communication, and preserves the consistency of the platform as it grows.

---

> **Architecture begins with language.**

> **Shared language creates shared understanding.**

🔱