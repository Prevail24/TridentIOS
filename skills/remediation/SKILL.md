# 🔱 TRIDENT REMEDIATION SKILL

## Skill Name

`trident-remediation`

## Purpose

Translate findings, risks, and evidence into clear remediation actions that help teams fix security issues effectively.

## Mission Phase

Primary phase:

- Act

## Responsibilities

This skill is responsible for:

- remediation planning
- fix prioritization
- short-term and long-term recommendations
- compensating control suggestions
- validation planning
- stakeholder-ready remediation language
- lessons-learned support

This skill is not responsible for:

- hiding risk
- inventing fixes
- replacing engineering judgment
- claiming remediation without evidence
- performing unauthorized changes

## Inputs

Expected inputs:

- mission context
- finding
- affected asset
- severity
- evidence
- business impact
- technical context
- owner or team context

## Outputs

Expected outputs:

- remediation plan
- immediate actions
- short-term fixes
- long-term improvements
- validation checklist
- compensating controls
- stakeholder summary

## Routing Rules

Use this skill when the operator asks to:

- fix a finding
- write remediation steps
- prioritize fixes
- explain mitigation
- create a remediation roadmap
- validate whether a fix worked
- prepare stakeholder guidance

Do not use this skill when:

- the request is pure recon
- the request is active exploitation
- the request needs evidence collection first
- the request belongs fully to compliance or reporting

## ScopeGuard Requirements

Remediation should be based on authorized findings and verified evidence.

Do not recommend destructive changes without caution, backup guidance, and operator approval.

## Playbooks

Relevant playbooks:

- `playbooks/remediation/`
- `playbooks/reporting/`
- `playbooks/vulnerability-management/`

## Libraries

Relevant libraries:

- `libraries/remediation/`
- `libraries/owasp/`
- `libraries/cis/`
- `libraries/cloud/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- remediation plans
- fix checklists
- validation steps
- compensating control notes
- owner/action trackers
- lessons learned

## Mission Handoff

This skill may hand off to:

- `trident-reporting`
- `trident-vulnerability-management`
- `trident-compliance`
- `trident-evidence`

## Limitations

This skill must not:

- claim a fix is complete without validation
- propose risky changes without warning
- ignore operational impact
- hide unresolved risk
- invent business context

## Doctrine

Findings should lead to action.

Fixes should be practical.

Validation proves closure.

Remediation improves the system.

Discover.

Analyze.

Act.