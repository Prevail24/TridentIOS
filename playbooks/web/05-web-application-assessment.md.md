# 🔱 TRD-PB-005

# Web Application Assessment

Version:
1.0

Department:
Application Security

Primary Skill:
trident-web

Mission Phase:
Discover → Analyze → Act

Estimated Duration:
2–8 Hours

Difficulty:
Intermediate → Advanced

---

# Purpose

Modern web applications are ecosystems.

Every application consists of interconnected systems including identities, APIs, databases, cloud services, third-party integrations, business logic, and infrastructure.

The objective is not to discover isolated vulnerabilities.

The objective is to understand the application's trust model, attack surface, and security posture.

A complete assessment identifies technical weaknesses while preserving context, evidence, and relationships.

---

# Mission Objectives

By the end of this assessment the operator should understand:

• Application architecture

• Authentication model

• Authorization model

• Session management

• Technology stack

• API exposure

• Third-party dependencies

• Business logic

• Sensitive data flows

• Trust boundaries

• Validated findings

---

# Prerequisites

Before beginning verify:

☐ Mission created

☐ Scope confirmed

☐ Rules of Engagement reviewed

☐ Recon complete

☐ Identity mapping completed (recommended)

☐ Evidence repository prepared

---

# Mission Inputs

Mission Context

Target URL

Scope

Recon Package

Identity Graph

Existing Evidence

---

# Assessment Workflow

## Phase 1 — Application Discovery

Understand the application before interacting with it.

Identify:

• Entry points

• Technologies

• Frameworks

• Authentication methods

• Third-party services

• Public resources

Deliverable:

Application Overview

---

## Phase 2 — Surface Mapping

Map every accessible component.

Examples:

Pages

Authentication

Administration

User Features

APIs

File Uploads

Search

Notifications

Exports

WebSockets

Document every endpoint.

---

## Phase 3 — Trust Analysis

Determine:

Who trusts whom?

Examples:

Browser → Application

Application → API

API → Database

Application → Cloud

Application → Identity Provider

Third-Party Services

Draw trust boundaries.

---

## Phase 4 — Authentication Review

Review:

Registration

Login

Password Reset

MFA

Session Creation

Logout

Account Recovery

Identity Federation

Deliverable:

Authentication Assessment

---

## Phase 5 — Authorization Review

Validate:

Horizontal access

Vertical access

Role separation

Administrative functions

Resource ownership

Object references

Deliverable:

Authorization Assessment

---

## Phase 6 — Session Security

Review:

Cookies

Session IDs

Token lifetime

Token invalidation

Remember Me

Logout behavior

Session fixation

Deliverable:

Session Assessment

---

## Phase 7 — Input Validation

Review every major input.

Examples:

Forms

Headers

Parameters

Uploads

Search

JSON

XML

Multipart Data

Document observed behavior.

---

## Phase 8 — Business Logic

Ask:

What assumptions does the application make?

Can those assumptions fail?

Business logic flaws often create the highest-impact findings.

---

## Phase 9 — Data Flow Analysis

Track:

Sensitive Data

Credentials

PII

Financial Data

Files

Secrets

Cloud Resources

Observe where data travels.

---

## Phase 10 — Validation

Every finding must be:

Reproducible

Evidence-backed

Within scope

Risk understood

False positives removed

---

# Evidence Requirements

Capture:

☐ Requests

☐ Responses

☐ Screenshots

☐ Session Details

☐ Timeline

☐ Relevant Headers

☐ Proof of Concept

☐ Related Entities

☐ Related Observations

☐ Related Evidence

---

# Success Criteria

The operator understands:

How the application works.

Where trust exists.

Where trust breaks.

What risks matter most.

---

# Common Mistakes

Testing before understanding.

Ignoring business logic.

Tunnel vision.

Skipping authentication review.

Skipping authorization review.

Failing to document evidence.

Reporting assumptions.

---

# Mission Handoff

Primary

→ trident-reporting

Possible

→ trident-api

→ trident-identity

→ trident-secret-hunter

→ trident-cloud

→ trident-remediation

---

# Knowledge Graph Updates

Possible outputs:

Application Entity

Technology Entity

Identity Relationship

Trust Relationship

API Relationship

Infrastructure Relationship

Evidence Link

Validated Finding

---

# Lessons Learned

Record:

Unexpected behavior

Interesting architecture

New attack paths

Workflow improvements

Knowledge improvements

---

# Operator Mindset

Every application tells a story.

Read the story before testing it.

Understand trust.

Question assumptions.

Think in systems.

Observe before acting.

---

# Doctrine

Applications are ecosystems.

Trust is the true attack surface.

Evidence creates confidence.

Knowledge compounds.

The best operators understand systems before they test them.

Discover.

Analyze.

Act.

🔱