# 🔱 TRD-PB-007

# Cloud Security Assessment

Version:
1.0

Department:
Infrastructure

Primary Skill:
trident-cloud

Mission Phase:
Discover → Analyze → Act

Estimated Duration:
2–8 Hours

Difficulty:
Intermediate → Advanced

Dependencies

Required

✓ TRD-PB-001 Quick Recon

Recommended

✓ TRD-PB-003 Identity Fabric Mapping

✓ TRD-PB-004 Secret Hunting

✓ TRD-PB-006 API Security Assessment

---

# Purpose

Modern organizations operate on cloud infrastructure.

Applications, APIs, storage, identity providers, serverless functions, containers, and CI/CD pipelines are frequently interconnected across multiple cloud platforms.

The objective is not to enumerate cloud assets.

The objective is to understand the organization's cloud architecture, trust relationships, exposure, and operational security.

Cloud security is the study of distributed trust.

---

# Mission Objectives

By completion the operator should understand:

• Cloud providers

• Identity architecture

• Storage exposure

• Compute resources

• Networking

• IAM configuration

• Secrets management

• Third-party integrations

• Operational risk

• Validated findings

---

# Prerequisites

Before beginning verify:

☐ Mission created

☐ Scope confirmed

☐ Authorization verified

☐ Recon complete

☐ Evidence repository prepared

---

# Mission Inputs

Mission Context

Target Organization

Known Domains

Known Cloud Resources

Identity Graph

Recon Package

Existing Evidence

---

# Assessment Workflow

## Phase 1 — Cloud Discovery

Identify:

Cloud Providers

Storage

CDNs

Serverless Functions

Load Balancers

Managed Services

Container Platforms

Registries

Deliverable

Cloud Inventory

---

## Phase 2 — Identity Architecture

Understand:

IAM

Roles

Policies

Federation

Service Accounts

Managed Identities

Trust Relationships

Deliverable

Identity Architecture

---

## Phase 3 — Storage Review

Review:

Object Storage

Blob Storage

Buckets

Snapshots

Backups

Public Exposure

Permissions

Encryption

Deliverable

Storage Assessment

---

## Phase 4 — Compute Review

Review:

Virtual Machines

Containers

Functions

Clusters

Managed Services

Autoscaling

Metadata Services

Deliverable

Compute Assessment

---

## Phase 5 — Network Analysis

Evaluate:

Public Services

Private Networks

Security Groups

Firewalls

Ingress

Egress

VPN

Peering

Deliverable

Network Assessment

---

## Phase 6 — Operational Security

Review:

Logging

Monitoring

Alerting

Secrets Management

Key Management

Backups

Disaster Recovery

Configuration Management

Deliverable

Operational Assessment

---

## Phase 7 — Validation

Every finding must be:

Evidence-backed

Reproducible

Within scope

Technically verified

Business impact understood

---

# Evidence Requirements

Capture

☐ Cloud Inventory

☐ Identity Relationships

☐ Network Diagrams

☐ Screenshots

☐ Configuration Evidence

☐ Timeline

☐ Related Entities

☐ Related Observations

☐ Validation Notes

---

# Success Criteria

The operator understands:

How cloud resources are organized.

How trust is established.

Where sensitive resources exist.

What operational risks matter.

---

# Common Mistakes

Focusing only on storage.

Ignoring IAM.

Ignoring trust relationships.

Treating cloud services as isolated systems.

Skipping evidence.

Failing to understand provider-specific architecture.

---

# Mission Handoff

Primary

→ trident-reporting

Possible

→ trident-identity

→ trident-secret-hunter

→ trident-remediation

→ trident-risk

---

# Knowledge Graph Updates

Possible outputs

Cloud Provider

Cloud Resource

Identity Relationship

Storage Relationship

Network Relationship

Infrastructure Relationship

Validated Finding

Evidence Link

---

# Lessons Learned

Record

Architecture observations

Identity discoveries

Operational improvements

Interesting configurations

Workflow improvements

Knowledge graph additions

---

# Operator Mindset

Cloud is infrastructure built on trust.

Understand identity before infrastructure.

Map relationships before evaluating risk.

Observe systems, not individual resources.

---

# Doctrine

Cloud security is identity security at scale.

Trust creates infrastructure.

Evidence creates confidence.

Knowledge compounds.

Discover.

Analyze.

Act.

🔱