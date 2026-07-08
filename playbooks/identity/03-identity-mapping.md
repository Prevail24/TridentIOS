# 🔱 PLAYBOOK-003

# Identity Fabric Mapping

Version:
1.0

Department:
Intelligence

Primary Skill:
trident-identity

Mission Phase:
Discover → Analyze

Estimated Duration:
30–120 Minutes

Difficulty:
Intermediate

---

# Purpose

Identity is one of the strongest indicators available during any cyber investigation.

Organizations, individuals, infrastructure, domains, cloud resources, source code, email addresses, usernames, social profiles, certificates, and repositories rarely exist in isolation.

The objective of Identity Fabric Mapping is to discover, correlate, and visualize these relationships.

The goal is not to collect identities.

The goal is to understand how identities connect.

---

# Mission Objectives

By the end of this playbook the operator should understand:

• Primary entities

• Identity relationships

• Organizational structure

• Infrastructure ownership

• Shared identifiers

• Trust relationships

• High-value identity targets

• Confidence of discovered relationships

---

# Prerequisites

Before beginning verify:

☐ Mission created

☐ Scope reviewed

☐ Authorization confirmed

☐ Initial target identified

☐ Knowledge graph available

☐ Evidence repository prepared

---

# Mission Inputs

Mission Context

Primary Target

Known Domains

Known Organizations

Known Identities

Existing Knowledge

Evidence

---

# Identity Layers

Every investigation should consider multiple identity layers.

Examples include:

People

Organizations

Email Addresses

Domains

Subdomains

Cloud Accounts

GitHub Organizations

GitHub Users

Source Repositories

Certificates

Social Profiles

Phone Numbers

Infrastructure

Applications

API Keys

Cloud Resources

ASN Ownership

Physical Locations

Each layer strengthens the overall Identity Fabric.

---

# Workflow

## Phase 1 — Identify Primary Entities

Begin with known entities.

Examples:

Organization

Domain

Employee

Repository

Email Address

Document each entity.

Assign an Entity ID.

---

## Phase 2 — Expand Relationships

For every entity ask:

What else is connected?

Examples:

Email → GitHub

GitHub → Repository

Repository → Domain

Domain → Certificate

Certificate → Organization

Organization → ASN

ASN → Infrastructure

Infrastructure → Cloud Provider

Every relationship should be evidence-backed.

---

## Phase 3 — Validate Relationships

Confirm:

Observed

Evidence exists

Confidence level

Relationship direction

False relationships removed

Deliverable:

Validated Identity Graph

---

## Phase 4 — Confidence Scoring

Assign confidence.

Example:

High

Multiple evidence sources.

Medium

Single trusted source.

Low

Hypothesis requiring validation.

Unknown

Relationship suspected.

Do not overstate confidence.

---

## Phase 5 — Intelligence Correlation

Compare discoveries against existing knowledge.

Questions:

Have we seen this before?

Existing Entity?

Existing Relationship?

New Observation?

New Organization?

Existing Infrastructure?

Mission overlap?

Knowledge compounds.

---

# Evidence Requirements

Capture:

☐ Screenshots

☐ URLs

☐ Repository Links

☐ Certificate Details

☐ WHOIS

☐ DNS

☐ Metadata

☐ Archived Sources

☐ Timeline

☐ Confidence Notes

---

# Success Criteria

The operator understands:

Who exists.

What exists.

How everything connects.

What deserves additional investigation.

---

# Common Mistakes

Collecting identities without relationships.

Assuming ownership.

Ignoring confidence.

Duplicating entities.

Treating observations as facts.

Skipping evidence.

---

# Mission Handoff

Primary

→ trident-analysis

Possible

→ trident-osint

→ trident-threat-intel

→ trident-recon

→ trident-secret-hunter

→ trident-reporting

---

# Knowledge Graph Updates

Possible outputs:

New Entity

New Relationship

Updated Confidence

New Observation

New Technique

New Organization

Updated Infrastructure

Identity Merge

Relationship Merge

Every mission should improve the graph.

---

# Lessons Learned

Record:

Unexpected relationships

False assumptions

Useful correlation techniques

Knowledge improvements

Future investigation ideas

---

# Operator Mindset

Everything is connected.

Assume nothing.

Verify everything.

Relationships matter more than isolated facts.

Think like an intelligence analyst.

---

# Doctrine

Identity is infrastructure.

Relationships create intelligence.

Evidence creates confidence.

Knowledge compounds.

The strongest investigations are built from connected observations.

Discover.

Analyze.

Act.

🔱