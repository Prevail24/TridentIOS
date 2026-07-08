# 🔱 TRIDENT OSINT SKILL

## Skill Name

`trident-osint`

## Purpose

Guide authorized open-source intelligence missions through structured discovery, source evaluation, correlation, and evidence-based reporting.

## Mission Phase

Primary phase:

- Discover
- Analyze

## Responsibilities

This skill is responsible for:

- public source research
- domain and organization profiling
- username and identity correlation
- public document review
- metadata awareness
- source reliability assessment
- OSINT evidence organization

This skill is not responsible for:

- doxxing
- harassment
- stalking
- credential theft
- social engineering execution
- illegal access

## Inputs

Expected inputs:

- mission context
- target entity
- authorization status
- research objective
- allowed sources
- excluded sources
- existing evidence

## Outputs

Expected outputs:

- OSINT plan
- source list
- entity map
- confidence-rated findings
- evidence notes
- unanswered questions
- reporting handoff

## Routing Rules

Use this skill when the operator asks about:

- OSINT
- public research
- usernames
- companies
- domains
- leaked documents
- public exposure
- entity mapping
- source correlation

Do not use this skill when:

- the request is harassment
- the request targets private individuals without legitimate purpose
- the task is active exploitation
- the task belongs fully to recon, identity, or reporting

## ScopeGuard Requirements

OSINT may be passive, but it still requires discipline.

Confirm:

- mission purpose
- target type
- allowed sources
- privacy boundaries
- reporting intent

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/recon/01-quick-recon.md`
- `playbooks/bug-bounty/02-bug-bounty-workflow.md`

## Libraries

Relevant libraries:

- `libraries/osint/`
- `libraries/dorks/`
- `libraries/tools/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- source notes
- entity maps
- public exposure findings
- screenshots
- archive links
- confidence ratings
- research timelines

## Mission Handoff

This skill may hand off to:

- `trident-recon`
- `trident-identity`
- `trident-secret-hunter`
- `trident-reporting`

## Limitations

This skill must not:

- facilitate harassment
- expose private personal data unnecessarily
- invent identity links
- overstate weak correlations
- bypass access controls
- encourage social engineering

## Doctrine

Public does not mean careless.

Correlate carefully.

Respect privacy.

Label confidence.

Preserve evidence.

Discover.

Analyze.

Act.