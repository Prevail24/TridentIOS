# 🔱 TRD-PB-008

# Linux Enumeration

Version:
1.0

Department:
Infrastructure

Primary Skill:
trident-linux

Mission Phase:
Discover → Analyze

Estimated Duration:
1–4 Hours

Difficulty:
Intermediate

Dependencies

Required

✓ TRD-PB-001 Quick Recon

Recommended

✓ TRD-PB-007 Cloud Security Assessment

---

# Purpose

Linux systems frequently host critical infrastructure including web servers, APIs, databases, containers, CI/CD systems, and cloud workloads.

The objective is to understand the operating environment, identify valuable information, and document the system while respecting scope and authorization.

Enumeration is observation.

Not exploitation.

---

# Mission Objectives

By completion the operator should understand:

• Operating system version

• Installed services

• Running processes

• User accounts

• Network configuration

• File system layout

• Scheduled tasks

• Logging

• Authentication mechanisms

• Security controls

---

# Assessment Workflow

## Phase 1 — System Identification

Identify:

• Distribution

• Kernel

• Hostname

• Time

• Architecture

Deliverable

System Profile

---

## Phase 2 — User Enumeration

Review:

Users

Groups

Privileges

Login methods

Authentication

Service accounts

Deliverable

Identity Profile

---

## Phase 3 — Service Enumeration

Identify:

Running services

Listening ports

Web servers

Databases

Containers

Virtualization

Deliverable

Service Inventory

---

## Phase 4 — File System Review

Review:

Configuration

Logs

Backups

Scripts

Secrets

Keys

Interesting files

Deliverable

Filesystem Assessment

---

## Phase 5 — Network Review

Review:

Interfaces

Routing

DNS

Connections

Firewall

VPN

Deliverable

Network Assessment

---

## Phase 6 — Security Review

Observe:

Permissions

Sudo configuration

Scheduled tasks

Logging

Monitoring

Security tooling

Deliverable

Security Posture

---

# Evidence Requirements

Capture:

☐ System profile

☐ Users

☐ Services

☐ Configuration

☐ Interesting files

☐ Network information

☐ Timeline

☐ Evidence references

---

# Mission Handoff

Primary

→ trident-analysis

Possible

→ trident-reporting

→ trident-remediation

→ trident-risk

---

# Operator Mindset

Learn the system before judging it.

Understand purpose before searching for weakness.

Context matters.

---

# Doctrine

Linux is an ecosystem.

Understand the ecosystem.

Evidence before conclusions.

Discover.

Analyze.

Act.

🔱