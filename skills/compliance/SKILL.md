# 🔱 TRIDENT COMPLIANCE SKILL

## Skill Name

`trident-compliance`

## Purpose

Support security compliance, policy mapping, control review, audit preparation, and evidence organization for authorized defensive missions.

## Mission Phase

Primary phase:

- Analyze
- Act

## Responsibilities

This skill is responsible for:

- control mapping
- policy review
- audit evidence organization
- gap analysis
- compliance summaries
- remediation tracking
- executive-ready control reporting

This skill is not responsible for:

- legal advice
- replacing auditors
- inventing evidence
- hiding control gaps
- bypassing requirements

## Inputs

Expected inputs:

- mission context
- framework
- policies
- controls
- evidence
- systems in scope
- audit objective
- known gaps

## Outputs

Expected outputs:

- control map
- gap analysis
- evidence checklist
- remediation plan
- compliance summary
- audit-ready notes

## Routing Rules

Use this skill when the operator asks about:

- compliance
- policies
- controls
- SOC 2
- ISO 27001
- NIST
- CIS
- HIPAA
- PCI DSS
- audit evidence
- security governance

Do not use this skill when:

- the request is active offensive testing
- the task is purely technical recon
- the request needs legal interpretation beyond general guidance

## ScopeGuard Requirements

Compliance work should use authorized internal or client-provided evidence.

Do not invent control status.

Label gaps clearly.

## Playbooks

Relevant playbooks:

- `playbooks/compliance/`
- `playbooks/reporting/`

## Libraries

Relevant libraries:

- `libraries/compliance/`
- `libraries/policies/`
- `libraries/templates/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- control matrices
- evidence checklists
- gap registers
- remediation trackers
- audit notes
- executive summaries

## Mission Handoff

This skill may hand off to:

- `trident-reporting`
- `trident-evidence`
- `trident-analysis`
- `trident-dfir`

## Limitations

This skill must not:

- provide formal legal advice
- claim compliance without evidence
- hide failed controls
- invent policy language
- replace qualified auditors

## Doctrine

Controls need evidence.

Gaps need clarity.

Reports need honesty.

Remediation creates progress.

Discover.

Analyze.

Act.