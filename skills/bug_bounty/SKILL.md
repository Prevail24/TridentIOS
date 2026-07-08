# 🔱 TRIDENT BUG BOUNTY SKILL

## Skill Name

`trident-bugbounty`

## Purpose

Guide authorized bug bounty missions from scope review through recon, validation, evidence capture, and report submission.

## Mission Phase

Primary phase:

- Discover
- Analyze
- Act

## Responsibilities

This skill is responsible for:

- reading program scope
- identifying in-scope and out-of-scope assets
- planning bug bounty recon
- prioritizing high-ROI targets
- guiding safe validation
- preparing bounty-ready findings
- handing off to reporting

This skill is not responsible for:

- unauthorized testing
- destructive testing
- social engineering
- persistence
- stealth
- evasion
- public disclosure without permission

## Inputs

Expected inputs:

- mission context
- bug bounty platform
- program scope
- allowed assets
- excluded assets
- rules of engagement
- severity guidance
- evidence collected

## Outputs

Expected outputs:

- scope summary
- recon plan
- target priority list
- validation checklist
- finding draft
- HackerOne/Bugcrowd-style report
- responsible disclosure notes

## Routing Rules

Use this skill when the operator asks about:

- HackerOne
- Bugcrowd
- Intigriti
- YesWeHack
- responsible disclosure
- bounty report writing
- program scope analysis
- bug bounty recon strategy

Do not use this skill when:

- the target has no authorization context
- the task is purely CTF
- the request is general web security theory
- the request belongs fully to reporting, recon, web, API, or cloud

## ScopeGuard Requirements

Always review scope before testing.

Record:

- in-scope assets
- out-of-scope assets
- prohibited actions
- rate limits
- disclosure rules
- testing restrictions

If scope is unclear, stop active guidance and ask for clarification.

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
- `libraries/cvss/`
- `libraries/tools/`
- `libraries/dorks/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- program scope summary
- target priority list
- validation notes
- proof-of-concept artifacts
- request and response captures
- screenshots
- severity notes
- disclosure drafts

## Mission Handoff

This skill may hand off to:

- `trident-recon`
- `trident-web`
- `trident-api`
- `trident-cloud`
- `trident-identity`
- `trident-secret-hunter`
- `trident-reporting`

## Limitations

This skill must not:

- advise testing excluded assets
- encourage noisy or destructive testing
- inflate severity
- omit uncertainty
- submit reports without evidence
- bypass program rules

## Doctrine

Read scope first.

Test carefully.

Validate safely.

Document everything.

Report professionally.

Discover.

Analyze.

Act.