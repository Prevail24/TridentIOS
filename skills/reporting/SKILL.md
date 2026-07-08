# 🔱 TRIDENT REPORTING SKILL

## Skill Name

`trident-reporting`

## Purpose

Transform mission evidence, findings, and analysis into clear professional reports.

## Mission Phase

Primary phase:

- Act

## Responsibilities

This skill is responsible for:

- executive summaries
- technical findings
- bug bounty reports
- CTF writeups
- evidence annexes
- recommendations
- lessons learned

This skill is not responsible for:

- discovering new assets
- performing tests
- validating exploits
- inventing missing evidence
- exaggerating severity

## Inputs

Expected inputs:

- mission context
- scope
- evidence index
- findings
- confidence levels
- severity notes
- screenshots or artifact paths
- audience type

## Outputs

Expected outputs:

- executive summary
- technical report
- finding cards
- bug bounty submission
- CTF writeup
- evidence appendix
- remediation plan
- lessons learned

## Routing Rules

Use this skill when the operator asks to:

- write a report
- summarize findings
- create an executive summary
- draft a HackerOne report
- document evidence
- prepare disclosure
- turn notes into a deliverable

Do not use this skill when:

- evidence is not yet collected
- the request is mainly recon
- the request is active testing
- the request is tool setup

## ScopeGuard Requirements

Reports must clearly state:

- engagement type
- authorization context
- in-scope assets
- out-of-scope assets
- limitations
- testing restrictions

Never include secret values in client-facing reports.

Redact sensitive data when appropriate.

## Playbooks

Relevant playbooks:

- `playbooks/bug-bounty/02-bug-bounty-workflow.md`
- `playbooks/recon/01-quick-recon.md`

## Libraries

Relevant libraries:

- `libraries/report-templates/`
- `libraries/cvss/`
- `libraries/owasp/`
- `libraries/mitre/`

## Evidence Produced

This skill may produce:

- report drafts
- executive summaries
- finding cards
- evidence indexes
- disclosure messages
- remediation plans
- lessons learned

## Mission Handoff

This skill may hand off to:

- `trident-bugbounty`
- `trident-recon`
- `trident-web`
- `trident-api`
- `trident-cloud`

## Limitations

This skill must not:

- invent evidence
- hide uncertainty
- inflate severity
- expose secrets unnecessarily
- present speculation as fact
- submit anything without operator approval

## Doctrine

Evidence becomes intelligence.

Findings become action.

Reports create trust.

Operator remains in command.

Discover.

Analyze.

Act.