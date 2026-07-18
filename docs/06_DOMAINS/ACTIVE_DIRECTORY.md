# 🏢 Active Directory

> **Applying the Trident Intelligence Operating System to Active Directory security assessments, enterprise investigations, and identity-centric attack path analysis.**

---

# Purpose

Active Directory (AD) is the identity backbone of many enterprise environments.

Within Trident, Active Directory investigations become structured Missions that document relationships between users, groups, computers, trusts, permissions, and privileges to uncover attack paths, privilege escalation opportunities, and security weaknesses.

Rather than viewing AD as isolated objects, Trident models the enterprise as an interconnected Intelligence Graph.

---

# Philosophy

Traditional workflow:

```text
Connect to Domain

↓

Enumerate Users

↓

Run BloodHound

↓

Escalate Privileges

↓

Write Report
```

Trident workflow:

```text
Active Directory

↓

Mission

↓

Enumeration

↓

Relationship Mapping

↓

Attack Path Analysis

↓

Validation

↓

Reporting

↓

Knowledge Promotion
```

The objective is not simply to become Domain Admin.

The objective is to understand the enterprise identity ecosystem.

---

# Mission Lifecycle

Every Active Directory assessment follows the standard Mission lifecycle.

```text
Create Mission

↓

Define Scope

↓

Medusa Planning

↓

Enumeration

↓

Relationship Analysis

↓

Privilege Analysis

↓

Council Review

↓

Reporting

↓

Knowledge Promotion
```

---

# Mission Example

```yaml
mission:

  title: Corporate Active Directory Assessment

  domain: Active Directory

  objective:

    Identify privilege escalation paths, excessive permissions, and identity-related security weaknesses.

  targets:

    - corp.example.local
```

---

# Common Investigation Types

Examples include:

- Active Directory Security Assessments
- Internal Penetration Tests
- Identity Security Reviews
- Privilege Escalation Analysis
- BloodHound Investigations
- Kerberos Assessments
- Certificate Services Reviews
- Tiering Reviews
- Trust Relationship Analysis
- Delegation Assessments

---

# Recommended Investigation Flow

## 1. Scope Definition

Determine:

- Forests
- Domains
- Organizational Units
- Trusts
- In-scope systems

Produces:

- Mission Scope
- Context

---

## 2. Enumeration

Capabilities:

- User Enumeration
- Group Enumeration
- Computer Enumeration
- Trust Enumeration
- LDAP Queries
- SMB Enumeration
- DNS Enumeration
- Kerberos Enumeration

Produces:

- Observations
- Entities

---

## 3. Relationship Discovery

Capabilities:

- Group Membership Analysis
- ACL Enumeration
- Delegation Discovery
- GPO Analysis
- Session Enumeration
- Trust Mapping
- Certificate Enumeration

Produces:

- Relationships
- Evidence

---

## 4. Attack Path Analysis

Capabilities:

- BloodHound Collection
- Privilege Escalation Analysis
- Lateral Movement Analysis
- Delegation Abuse Detection
- Certificate Attack Path Analysis

Produces:

- Findings
- Evidence
- Attack Paths

---

## 5. Validation

Potential attack paths are verified.

False positives are removed.

Validated attack paths become Findings.

---

## 6. Analysis

Council Members evaluate:

- Privilege escalation opportunities
- Administrative boundaries
- Identity risks
- Trust relationships
- Attack complexity

Produces:

- Findings
- Recommendations

---

## 7. Reporting

Reporter generates:

- Executive Summary
- Identity Architecture
- Attack Paths
- Evidence
- Findings
- Remediation Plan

---

# Intelligence Objects

Active Directory Missions commonly produce:

## Observations

Examples:

- LDAP Objects
- Kerberos Tickets
- GPO Configuration
- Trust Relationships
- ACL Entries
- SMB Shares

---

## Entities

Examples:

- User
- Computer
- Group
- Domain
- Forest
- Organizational Unit
- Trust
- Certificate Authority
- Service Account
- Group Policy Object

---

## Relationships

Examples:

```text
MEMBER_OF

ADMIN_TO

HAS_SESSION

TRUSTS

OWNS

DELEGATES_TO

CONTROLS

CAN_RDP

CAN_PSEXEC

CAN_DCSYNC
```

Relationships become the foundation of the Mission Knowledge Graph.

---

## Findings

Examples:

- Domain Users possess excessive permissions.
- Unconstrained Delegation identified.
- Certificate Services vulnerable to ESC1.
- Service Account has Domain Admin privileges.
- Tier boundaries are improperly enforced.

---

## Hypotheses

Examples:

- Additional privilege escalation paths may exist.
- Administrative accounts may violate tiering policies.
- Trust relationships may permit cross-domain compromise.

Hypotheses require validation before becoming Findings.

---

# Mission Updates

Every discovery enters the Mission through Mission Updates.

Example:

```text
LDAP Enumeration

↓

Observation

↓

Mission Update

↓

Mission Intelligence
```

Mission intelligence grows incrementally throughout the investigation.

---

# Knowledge Graph

Active Directory naturally forms one of the richest Knowledge Graphs within Trident.

```text
User

↓

MEMBER_OF

↓

Group

↓

ADMIN_TO

↓

Server

↓

HAS_SESSION

↓

Domain Admin
```

Graph analysis reveals attack paths that are difficult to identify through isolated observations.

---

# Framework Integration

Findings may be mapped to:

- MITRE ATT&CK
- BloodHound Attack Paths
- Microsoft Security Baselines
- CIS Benchmarks
- SpecterOps Guidance

Mappings enhance context without replacing Mission intelligence.

---

# Council Analysis

Council Members may include:

- Active Directory Analyst
- Identity Security Architect
- BloodHound Specialist
- Kerberos Analyst
- PKI Specialist
- Devil's Advocate

Each independently evaluates the Mission and contributes structured intelligence.

---

# Reporting

Reporter may generate:

- Executive Summary
- Identity Architecture Overview
- Attack Path Analysis
- Privilege Escalation Report
- Trust Relationship Map
- Remediation Roadmap

Reports are generated from Mission intelligence.

The report is never the source of truth.

---

# Loom Integration

Validated knowledge may be promoted into Loom.

Examples:

- Identity attack playbooks
- BloodHound methodologies
- Kerberos attack techniques
- Certificate Services guidance
- Administrative tiering models
- Hardening recommendations

Future assessments benefit from accumulated organizational knowledge.

---

# Benefits

Using Trident for Active Directory provides:

- Structured enterprise assessments
- Identity-centric investigations
- Explainable attack paths
- Evidence-backed privilege analysis
- Professional reporting
- Repeatable methodologies
- Long-term institutional knowledge

Every assessment strengthens the organization's understanding of its identity infrastructure.

---

# Summary

Active Directory security is fundamentally about understanding relationships between identities, permissions, and trust boundaries.

Trident transforms these relationships into an explainable Intelligence Graph, enabling investigators to identify privilege escalation paths, validate attack scenarios, and preserve organizational knowledge through structured Missions.

The objective is not simply to compromise the domain.

The objective is to understand and secure the identity ecosystem.

---

> **Map every identity.**

> **Understand every relationship.**

> **Validate every attack path.**

> **Preserve the knowledge.**

🔱