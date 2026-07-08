# 🔱 TRIDENT RISK SKILL

## Skill Name

`trident-risk`

## Purpose

Translate technical findings, evidence, and uncertainty into clear risk language for operators, stakeholders, and reports.

## Mission Phase

Primary phase:

- Analyze
- Act

## Responsibilities

This skill is responsible for:

- risk interpretation
- business impact framing
- likelihood assessment
- impact assessment
- severity calibration
- uncertainty labeling
- executive risk summaries
- decision support

This skill is not responsible for:

- inventing impact
- inflating severity
- replacing evidence
- legal advice
- final approval decisions

## Inputs

Expected inputs:

- mission context
- finding
- evidence
- affected asset
- severity estimate
- confidence level
- business context
- exposure context

## Outputs

Expected outputs:

- risk summary
- impact statement
- likelihood statement
- severity rationale
- uncertainty notes
- stakeholder-ready explanation
- recommended action priority

## Routing Rules

Use this skill when the operator asks to:

- explain risk
- translate technical findings
- justify severity
- write impact
- prioritize business risk
- prepare executive language
- compare findings

Do not use this skill when:

- evidence has not been collected
- the request is pure recon
- the request is active testing
- the task belongs fully to reporting

## ScopeGuard Requirements

Risk statements must be based on authorized evidence.

Do not claim confirmed impact without proof.

Label assumptions clearly.

## Playbooks

Relevant playbooks:

- `playbooks/risk/`
- `playbooks/reporting/`
- `playbooks/vulnerability-management/`

## Libraries

Relevant libraries:

- `libraries/risk/`
- `libraries/cvss/`
- `libraries/owasp/`
- `libraries/cwe/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- risk summaries
- impact statements
- likelihood notes
- severity rationale
- uncertainty labels
- executive summaries

## Mission Handoff

This skill may hand off to:

- `trident-reporting`
- `trident-remediation`
- `trident-vulnerability-management`
- `trident-compliance`

## Limitations

This skill must not:

- exaggerate impact
- hide uncertainty
- claim exploitation without evidence
- ignore business context
- replace operator judgment

## Doctrine

Risk must be understandable.

Severity must be justified.

Uncertainty must be visible.

Evidence before conclusions.

Discover.

Analyze.

Act.