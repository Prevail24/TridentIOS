# 🔱 TRIDENT SECRET HUNTER SKILL

## Skill Name

`trident-secret-hunter`

## Purpose

Identify, classify, validate, document, and responsibly report exposed secrets during authorized missions.

## Mission Phase

Primary phase:

- Discover
- Analyze
- Act

## Responsibilities

This skill is responsible for:

- secret discovery planning
- GitHub and public-code secret hunting
- JavaScript and sourcemap review
- public workspace review
- secret classification
- safe validation guidance
- exposure severity assessment
- disclosure preparation

This skill is not responsible for:

- abusing credentials
- persistence
- privilege escalation
- data theft
- destructive cloud actions
- using secrets outside authorized validation

## Inputs

Expected inputs:

- mission context
- target organization
- authorized scope
- rules of engagement
- discovered secret candidate
- source URL or artifact path
- provider type
- validation permission status

## Outputs

Expected outputs:

- secret classification
- confidence level
- validation plan
- evidence record
- severity assessment
- remediation guidance
- disclosure-ready finding

## Routing Rules

Use this skill when the operator asks about:

- leaked credentials
- API keys
- GitHub dorks
- secret scanning
- exposed tokens
- AWS keys
- GitHub PATs
- `.env` leaks
- JavaScript secrets
- sourcemap secrets
- Postman workspace leaks

Do not use this skill when:

- the request is to abuse credentials
- the request is credential theft
- the request is unrelated to exposed secrets
- the task is general recon without secret context

## ScopeGuard Requirements

Before validation, confirm:

- the target is authorized
- the asset is in scope
- read-only validation is permitted
- provider rules allow validation
- no destructive or write actions will be performed

If validation is not explicitly permitted, classify and report without using the secret.

Never expose full secret values in client-facing reports.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/secrets/04-secret-hunting.md`
- `playbooks/bug-bounty/02-bug-bounty-workflow.md`

## Libraries

Relevant libraries:

- `libraries/regex/`
- `libraries/dorks/`
- `libraries/tools/`
- `libraries/cloud/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- secret candidate records
- classification notes
- validation logs
- source artifacts
- hashes
- redacted screenshots
- severity notes
- disclosure drafts

## Mission Handoff

This skill may hand off to:

- `trident-cloud`
- `trident-bugbounty`
- `trident-reporting`
- `trident-evidence`
- `trident-recon`

## Limitations

This skill must not:

- use secrets for access beyond read-only validation
- dump data
- modify cloud resources
- bypass controls
- expose secret values in reports
- encourage unauthorized credential use

## Doctrine

Find carefully.

Validate safely.

Redact aggressively.

Disclose responsibly.

Evidence before conclusions.

Discover.

Analyze.

Act.