# 🔱 PLAYBOOK-004

# Secret Hunting

Version:
1.0

Department:
Intelligence

Primary Skill:
trident-secret-hunter

Mission Phase:
Discover → Analyze

Estimated Duration:
30–180 Minutes

Difficulty:
Intermediate

---

# Purpose

Secrets are among the highest-value artifacts discovered during security investigations.

A single exposed credential may reveal:

• Infrastructure

• Cloud environments

• APIs

• Source code

• Internal systems

• Third-party services

The objective is not to collect secrets.

The objective is to understand exposure, validate findings responsibly, and improve security.

---

# Mission Objectives

By the end of this playbook the operator should understand:

• What secrets exist

• Where they originated

• Current exposure

• Potential impact

• Recommended remediation

• Relationships to other entities

---

# Prerequisites

Before beginning verify:

☐ Scope confirmed

☐ Authorization verified

☐ Mission created

☐ Evidence repository available

☐ Secret handling procedures reviewed

---

# Mission Inputs

Mission Context

Repositories

Domains

Applications

Cloud Resources

Known Identities

Existing Evidence

---

# Secret Categories

Examples include:

API Keys

Cloud Credentials

Database Credentials

SSH Keys

Private Keys

JWT Secrets

OAuth Tokens

Session Tokens

Service Accounts

Webhook Secrets

Environment Variables

Configuration Files

Certificates

Encryption Keys

---

# Workflow

## Phase 1 — Identify Candidate Sources

Potential locations:

- Source repositories
- Configuration files
- CI/CD pipelines
- Public artifacts
- Documentation
- Containers
- Cloud storage
- Logs

Deliverable:

Candidate Source Inventory

---

## Phase 2 — Discovery

Identify potential secrets.

Record:

Location

Type

Context

Exposure

Confidence

Do not assume validity.

---

## Phase 3 — Validation

Confirm:

Secret format

Likely purpose

Scope relevance

Exposure

Evidence

Never use discovered credentials outside authorized testing.

Never exceed scope.

---

## Phase 4 — Correlation

Determine relationships.

Examples:

Secret → Repository

Repository → Organization

Organization → Cloud Account

Cloud Account → Infrastructure

Developer → Commit History

Relationships improve understanding.

---

## Phase 5 — Risk Assessment

Evaluate:

Exposure

Sensitivity

Business impact

Likelihood

Potential abuse

Prioritize findings.

---

# Evidence Requirements

Capture:

☐ Discovery location

☐ File path

☐ Commit reference (if applicable)

☐ Screenshot (redacted when necessary)

☐ Validation notes

☐ Timeline

☐ Related entities

☐ Confidence level

Sensitive values should be handled responsibly and redacted where appropriate.

---

# Success Criteria

The operator understands:

Where the secret exists.

Why it exists.

How it is connected.

Its potential impact.

Recommended remediation.

---

# Common Mistakes

Assuming every string is a credential.

Using credentials without authorization.

Failing to redact sensitive information.

Ignoring relationships.

Skipping validation.

Collecting secrets without documenting context.

---

# Mission Handoff

Primary

→ trident-analysis

Possible

→ trident-cloud

→ trident-identity

→ trident-reporting

→ trident-remediation

---

# Knowledge Graph Updates

Possible outputs:

New Secret Entity

Repository Relationship

Identity Relationship

Infrastructure Relationship

Cloud Relationship

Updated Confidence

Evidence Link

---

# Lessons Learned

Record:

Discovery techniques

False positives

Validation improvements

Relationship discoveries

Workflow improvements

---

# Operator Mindset

Secrets are evidence.

Context matters more than collection.

Protect sensitive information.

Think beyond the credential.

Understand the system it belongs to.

---

# Doctrine

A secret is rarely the objective.

It is a doorway to understanding.

Handle responsibly.

Validate carefully.

Document thoroughly.

Discover.

Analyze.

Act.

🔱