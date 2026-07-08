# 🔱 TRIDENT CLOUD SKILL

## Skill Name

`trident-cloud`

## Purpose

Guide authorized cloud security review across AWS, Azure, and GCP using scoped, evidence-driven methodology.

## Mission Phase

Primary phase:

- Discover
- Analyze

## Responsibilities

This skill is responsible for:

- cloud asset identification
- exposed storage review
- IAM posture analysis
- public cloud misconfiguration review
- cloud secret exposure triage
- read-only validation planning
- cloud risk assessment
- cloud finding preparation

This skill is not responsible for:

- destructive actions
- unauthorized cloud access
- persistence
- privilege escalation without authorization
- data exfiltration
- modifying cloud resources

## Inputs

Expected inputs:

- mission context
- cloud provider
- authorized scope
- rules of engagement
- account IDs or tenant IDs
- discovered cloud assets
- existing evidence
- validation permissions

## Outputs

Expected outputs:

- cloud asset summary
- exposure notes
- IAM observations
- misconfiguration candidates
- validation checklist
- cloud findings
- remediation guidance

## Routing Rules

Use this skill when the operator asks about:

- AWS
- Azure
- GCP
- S3 buckets
- IAM users
- access keys
- cloud storage exposure
- cloud misconfigurations
- cloud account ownership
- cloud posture review

Do not use this skill when:

- the request is unrelated to cloud
- the target is not authorized
- the task is purely web or API testing
- the request asks to abuse cloud access

## ScopeGuard Requirements

Before cloud validation, confirm:

- cloud assets are in scope
- account or tenant ownership is established
- read-only validation is permitted
- no write actions will be performed
- sensitive data will not be accessed unnecessarily

If scope is unclear, classify and document only.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/secrets/04-secret-hunting.md`
- `playbooks/identity/03-identity-fabric-mapping.md`
- `playbooks/bug-bounty/02-bug-bounty-workflow.md`

## Libraries

Relevant libraries:

- `libraries/cloud/aws/`
- `libraries/cloud/azure/`
- `libraries/cloud/gcp/`
- `libraries/iam/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- account ownership notes
- bucket exposure records
- IAM read-only outputs
- cloud service inventories
- configuration observations
- validation logs
- remediation notes

## Mission Handoff

This skill may hand off to:

- `trident-secret-hunter`
- `trident-identity`
- `trident-bugbounty`
- `trident-reporting`
- `trident-evidence`

## Limitations

This skill must not:

- modify cloud resources
- access data beyond validation need
- use credentials outside ROE
- escalate privileges without authorization
- dump secrets or production data
- present cloud ownership as confirmed without evidence

## Doctrine

Cloud scope matters.

Validate ownership.

Prefer read-only.

Protect data.

Document evidence.

Discover.

Analyze.

Act.