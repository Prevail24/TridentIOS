# 🔱 TRIDENT PRIVACY SKILL

## Skill Name

`trident-privacy`

## Purpose

Support privacy-focused investigations, exposure reviews, PII handling, data minimization, redaction, and responsible documentation.

## Mission Phase

Primary phase:

- Analyze
- Act

## Responsibilities

This skill is responsible for:

- PII exposure review
- privacy risk analysis
- data minimization guidance
- redaction planning
- exposure documentation
- takedown workflow support
- privacy-focused reporting

This skill is not responsible for:

- doxxing
- stalking
- harassment
- illegal data access
- credential abuse
- exposing private individuals unnecessarily

## Inputs

Expected inputs:

- mission context
- exposure type
- data category
- source location
- authorization status
- affected entity
- evidence collected

## Outputs

Expected outputs:

- privacy risk summary
- exposure notes
- redaction plan
- evidence handling guidance
- takedown checklist
- remediation recommendations
- report handoff

## Routing Rules

Use this skill when the operator asks about:

- PII exposure
- privacy review
- data leaks
- exposed records
- redaction
- data broker removal
- personal information cleanup
- privacy reporting

Do not use this skill when:

- the request enables harassment
- the request exposes private people without legitimate purpose
- the task is offensive exploitation
- the request seeks credential abuse

## ScopeGuard Requirements

Privacy work requires extra care.

Confirm:

- legitimate purpose
- authorized context
- minimum necessary data
- redaction needs
- responsible disclosure path

Public data is still sensitive.

## Playbooks

Relevant playbooks:

- `playbooks/privacy/`
- `playbooks/osint/`
- `playbooks/reporting/`

## Libraries

Relevant libraries:

- `libraries/privacy/`
- `libraries/redaction/`
- `libraries/templates/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- exposure summaries
- redaction notes
- privacy risk findings
- source records
- takedown checklists
- remediation notes

## Mission Handoff

This skill may hand off to:

- `trident-osint`
- `trident-reporting`
- `trident-evidence`
- `trident-compliance`

## Limitations

This skill must not:

- facilitate harassment
- expose private data unnecessarily
- invent privacy impact
- skip redaction
- treat public availability as permission to amplify

## Doctrine

Public does not mean harmless.

Minimize exposure.

Redact carefully.

Document responsibly.

Protect people.

Discover.

Analyze.

Act.