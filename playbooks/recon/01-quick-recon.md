# 🔱 PLAYBOOK-001

# Quick Recon

Mission Phase:
Discover

Skill Owner:
trident-recon

Estimated Time:
15–60 minutes

Difficulty:
Beginner → Intermediate

---

# Objective

Rapidly identify the exposed attack surface of an authorized target.

The purpose is not to find vulnerabilities.

The purpose is to understand the environment.

Recon creates situational awareness.

---

# Prerequisites

Mission created

Scope confirmed

Target identified

Evidence folder created

---

# Inputs

Mission Context

Target Domain

Time Budget

Authorization Status

---

# Outputs

Root Domain

Subdomains

DNS Records

Resolved IPs

Open Ports

Technologies

Interesting Services

Recon Notes

Evidence Package

---

# Workflow

## Phase 1 — Target Validation

Confirm:

- Scope
- Target
- Authorization

Document:

Target Name

Primary Domain

Mission ID

---

## Phase 2 — Passive Recon

Collect:

WHOIS

RDAP

DNS Records

Certificate Transparency

ASN

Historical DNS

Archive.org

Technology Fingerprinting

Record all findings.

---

## Phase 3 — Subdomain Enumeration

Discover subdomains.

Merge results.

Remove duplicates.

Resolve live hosts.

Store evidence.

---

## Phase 4 — Service Discovery

Identify:

HTTP

HTTPS

SSH

VPN

Mail

Remote Access

Development Systems

Management Interfaces

---

## Phase 5 — Technology Identification

Identify:

Frameworks

CMS

Cloud Providers

CDNs

Authentication Providers

Security Headers

Interesting Technologies

---

## Phase 6 — Prioritization

Rank targets:

High

Medium

Low

Document why.

---

# Evidence Checklist

□ WHOIS

□ DNS

□ CT Logs

□ Live Hosts

□ IP List

□ Technologies

□ Screenshots

□ Notes

---

# Deliverables

Recon Summary

Evidence Index

Target Inventory

Priority Targets

Recommendations

---

# Mission Handoff

Primary:

trident-analysis

Possible:

trident-web

trident-api

trident-cloud

trident-identity

trident-secret-hunter

---

# Lessons Learned

Record:

Unexpected findings

Missed opportunities

Useful commands

Workflow improvements

---

# Completion Criteria

Mission understanding achieved.

Evidence preserved.

Targets prioritized.

Operator ready for analysis.

---

# Doctrine

Recon is observation.

Not exploitation.

Map first.

Think second.

Strike last.

Discover.

Analyze.

Act.

🔱