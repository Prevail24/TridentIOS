# 🔱 TRIDENT ANALYSIS SKILL

## Skill Name

`trident-analysis`

## Purpose

Correlate mission evidence into findings, hypotheses, risks, priorities, and recommended next actions.

## Mission Phase

Primary phase:

- Analyze

## Responsibilities

This skill is responsible for:

- evidence review
- hypothesis generation
- vulnerability candidate triage
- confidence labeling
- risk prioritization
- attack-path reasoning
- next-step recommendation
- handoff to reporting

This skill is not responsible for:

- collecting raw recon
- active testing
- final report writing
- inventing missing evidence
- overstating certainty

## Inputs

Expected inputs:

- mission context
- evidence index
- recon results
- tool outputs
- screenshots
- notes
- scope status
- operator objective

## Outputs

Expected outputs:

- finding candidates
- confidence ratings
- severity estimates
- attack-path notes
- evidence gaps
- recommended next steps
- reporting handoff

## Routing Rules

Use this skill when the operator asks to:

- analyze results
- prioritize findings
- understand impact
- connect evidence
- determine what matters
- decide next steps
- review possible vulnerabilities

Do not use this skill when:

- the request is simple recon collection
- the request is final report writing
- evidence does not exist yet
- the task is tool installation

## ScopeGuard Requirements

Analysis can continue with unknown scope, but active next steps require confirmed authorization.

If suggesting active testing, include scope warning when needed.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/bug-bounty/02-bug-bounty-workflow.md`
- `playbooks/recon/01-quick-recon.md`
- `playbooks/secrets/04-secret-hunting.md`
- `playbooks/identity/03-identity-fabric-mapping.md`

## Libraries

Relevant libraries:

- `libraries/owasp/`
- `libraries/mitre/`
- `libraries/cvss/`
- `libraries/attack-paths/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- analysis notes
- finding candidates
- confidence labels
- severity estimates
- evidence-gap lists
- recommended next-action lists

## Mission Handoff

This skill may hand off to:

- `trident-reporting`
- `trident-evidence`
- `trident-web`
- `trident-api`
- `trident-cloud`
- `trident-bugbounty`

## Limitations

This skill must not:

- invent evidence
- convert speculation into fact
- inflate severity
- suggest active testing outside scope
- ignore uncertainty

## Doctrine

Evidence becomes understanding.

Understanding becomes findings.

Findings become action.

Confidence must match evidence.

Discover.

Analyze.

Act.