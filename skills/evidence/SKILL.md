# 🔱 TRIDENT EVIDENCE SKILL

## Skill Name

`trident-evidence`

## Purpose

Organize, index, preserve, and prepare mission evidence so every finding remains traceable.

## Mission Phase

Primary phase:

- Analyze
- Act

## Responsibilities

This skill is responsible for:

- evidence organization
- artifact naming
- evidence indexing
- screenshot tracking
- command/output tracking
- hash recording
- confidence labeling
- redaction guidance
- evidence handoff to reporting

This skill is not responsible for:

- discovering new targets
- performing exploitation
- writing final reports alone
- inventing missing artifacts
- hiding uncertainty

## Inputs

Expected inputs:

- mission context
- artifact paths
- commands run
- screenshots
- notes
- findings
- timestamps
- confidence levels

## Outputs

Expected outputs:

- evidence index
- artifact summary
- finding-to-evidence map
- redaction notes
- report-ready evidence package
- missing-evidence checklist

## Routing Rules

Use this skill when the operator asks to:

- organize evidence
- index artifacts
- prepare screenshots
- map evidence to findings
- clean mission notes
- verify report support
- identify missing proof

Do not use this skill when:

- the request is primarily recon
- the request is active testing
- the request is tool installation
- the request is unrelated to mission artifacts

## ScopeGuard Requirements

Evidence may contain sensitive data.

Before sharing or reporting:

- identify secrets
- redact sensitive values
- separate private annexes from client-facing reports
- preserve raw evidence securely
- avoid exposing third-party data unnecessarily

## Playbooks

Relevant playbooks:

- `playbooks/recon/01-quick-recon.md`
- `playbooks/bug-bounty/02-bug-bounty-workflow.md`
- `playbooks/secrets/04-secret-hunting.md`

## Libraries

Relevant libraries:

- `libraries/report-templates/`
- `libraries/redaction/`
- `libraries/evidence/`

## Evidence Produced

This skill may produce:

- evidence indexes
- artifact manifests
- redaction logs
- confidence labels
- timeline notes
- finding support matrices

## Mission Handoff

This skill may hand off to:

- `trident-reporting`
- `trident-bugbounty`
- `trident-recon`
- `trident-secret-hunter`

## Limitations

This skill must not:

- invent missing evidence
- alter raw artifacts
- remove uncertainty
- expose secrets unnecessarily
- treat weak evidence as confirmed

## Doctrine

Preserve raw evidence.

Index everything important.

Redact carefully.

Trace every finding.

Evidence before conclusions.

Discover.

Analyze.

Act.