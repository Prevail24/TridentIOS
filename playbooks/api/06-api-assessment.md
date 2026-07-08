# 🔱 TRD-PB-006

# API Security Assessment

Version:
1.0

Department:
Application Security

Primary Skill:
trident-api

Mission Phase:
Discover → Analyze → Act

Estimated Duration:
2–8 Hours

Difficulty:
Intermediate → Advanced

Dependencies

Required

✓ TRD-PB-001 Quick Recon

✓ TRD-PB-005 Web Application Assessment

Recommended

✓ TRD-PB-003 Identity Fabric Mapping

✓ TRD-PB-004 Secret Hunting

---

# Purpose

Modern applications are API-driven systems.

Mobile applications, web frontends, third-party integrations, automation platforms, and cloud services communicate through APIs.

The objective is not to enumerate endpoints.

The objective is to understand how data, identity, and trust move throughout the system.

An API assessment evaluates architecture, authentication, authorization, business logic, data exposure, and trust relationships.

---

# Mission Objectives

By completion the operator should understand:

• API architecture

• Authentication model

• Authorization model

• Data exposure

• Business logic

• Trust boundaries

• Rate limiting

• Sensitive operations

• Third-party integrations

• Validated findings

---

# Prerequisites

Before beginning verify:

☐ Mission created

☐ Scope confirmed

☐ Recon complete

☐ Web assessment completed

☐ Evidence repository prepared

---

# Mission Inputs

Mission Context

Target APIs

Swagger / OpenAPI

Postman Collections

Recon Package

Identity Graph

Evidence

---

# Assessment Workflow

## Phase 1 — API Discovery

Identify:

REST APIs

GraphQL

SOAP

gRPC

Internal APIs

Partner APIs

Versioning

Documentation

Deliverable

API Inventory

---

## Phase 2 — Surface Mapping

Document:

Endpoints

Methods

Parameters

Headers

Authentication

Response Types

Error Messages

Status Codes

Versioning

Deliverable

API Surface Map

---

## Phase 3 — Authentication Review

Review:

API Keys

OAuth

JWT

Session Tokens

mTLS

HMAC

Service Accounts

Identity Federation

Deliverable

Authentication Assessment

---

## Phase 4 — Authorization Review

Validate:

Object ownership

Horizontal access

Vertical access

Administrative operations

Tenant isolation

Privilege boundaries

Deliverable

Authorization Assessment

---

## Phase 5 — Data Flow Analysis

Track:

Sensitive data

PII

Secrets

Files

Financial data

Identifiers

Metadata

Relationships

Determine where data originates and where it travels.

---

## Phase 6 — Business Logic

Ask:

What assumptions does the API make?

Can workflows be abused?

Can operations occur out of sequence?

Can trust relationships be manipulated?

Deliverable

Business Logic Assessment

---

## Phase 7 — Operational Security

Evaluate:

Rate limiting

Pagination

Caching

Logging

Error handling

Version management

Input validation

Output filtering

Abuse protection

---

## Phase 8 — Validation

Every finding must be:

Evidence-backed

Reproducible

Within scope

Technically verified

Business impact understood

---

# Evidence Requirements

Capture

☐ Endpoint inventory

☐ Requests

☐ Responses

☐ Authentication flow

☐ Authorization evidence

☐ Timeline

☐ Related entities

☐ Related observations

☐ Proof of Concept

☐ Validation notes

---

# Success Criteria

The operator understands:

How the API works.

How identities interact.

How trust is established.

Where risk exists.

What should be remediated.

---

# Common Mistakes

Enumerating without understanding.

Ignoring business logic.

Ignoring authorization.

Testing production carelessly.

Missing undocumented endpoints.

Assuming documentation is complete.

---

# Mission Handoff

Primary

→ trident-reporting

Possible

→ trident-web

→ trident-cloud

→ trident-identity

→ trident-secret-hunter

→ trident-remediation

---

# Knowledge Graph Updates

Possible outputs

API Entity

Endpoint Entity

Authentication Relationship

Identity Relationship

Technology Relationship

Infrastructure Relationship

Validated Finding

Evidence Link

---

# Lessons Learned

Record

Unexpected behaviors

Interesting endpoints

Architecture observations

Business logic discoveries

Workflow improvements

Knowledge graph additions

---

# Operator Mindset

APIs reveal architecture.

Endpoints tell stories.

Trust boundaries deserve attention.

Business logic is often the highest-value target.

Observe before interacting.

Understand before testing.

---

# Doctrine

APIs are conversations between systems.

Understand the conversation before questioning the answers.

Trust is earned.

Evidence proves.

Knowledge compounds.

Discover.

Analyze.

Act.

🔱