# 🔱 TRIDENT SOCIAL ENGINEERING AWARENESS SKILL

## Skill Name

`trident-social-engineering-awareness`

## Purpose

Support defensive awareness, training, risk review, and reporting around social engineering threats without enabling real-world manipulation or phishing execution.

## Mission Phase

Primary phase:

- Analyze
- Act

## Responsibilities

This skill is responsible for:

- awareness training
- pretext risk analysis
- phishing-resilience guidance
- defensive scenario review
- reporting social-engineering exposure
- safe tabletop exercises
- employee education support

This skill is not responsible for:

- phishing execution
- impersonation
- credential harvesting
- manipulation scripts
- bypassing human trust
- real-world targeting

## Inputs

Expected inputs:

- mission context
- organization type
- threat scenario
- training objective
- authorization status
- audience
- evidence or observations

## Outputs

Expected outputs:

- awareness brief
- safe training scenario
- defensive checklist
- risk summary
- detection recommendations
- reporting handoff

## Routing Rules

Use this skill when the operator asks about:

- phishing awareness
- vishing risk
- smishing risk
- Teams/social pretext risk
- employee training
- social engineering defense
- tabletop exercises

Do not use this skill when:

- the request asks to trick real people
- the request asks for phishing templates
- the request asks to harvest credentials
- the request asks for impersonation scripts

## ScopeGuard Requirements

Social engineering requires explicit written authorization.

Default to defensive education unless ROE clearly permits controlled awareness exercises.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/social-engineering-awareness/`
- `playbooks/identity/03-identity-fabric-mapping.md`
- `playbooks/reporting/`

## Libraries

Relevant libraries:

- `libraries/awareness/`
- `libraries/policies/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- awareness notes
- risk summaries
- training outlines
- tabletop scenarios
- defensive recommendations

## Mission Handoff

This skill may hand off to:

- `trident-identity`
- `trident-reporting`
- `trident-compliance`
- `trident-privacy`

## Limitations

This skill must not:

- create real phishing campaigns
- write deceptive messages for real targets
- collect credentials
- enable impersonation
- encourage harassment

## Doctrine

Defend people.

Train safely.

Reduce risk.

Respect consent.

Protect trust.

Discover.

Analyze.

Act.