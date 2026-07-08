# 🔱 TRIDENT IDENTITY SKILL

## Skill Name

`trident-identity`

## Purpose

Map and analyze identity infrastructure during authorized missions, with emphasis on Microsoft 365, Entra ID, SSO, federation, and identity exposure.

## Mission Phase

Primary phase:

- Discover
- Analyze

## Responsibilities

This skill is responsible for:

- identity surface mapping
- Microsoft 365 tenant discovery
- Entra ID fingerprinting
- federation posture review
- SSO exposure analysis
- Teams federation review
- SharePoint and OneDrive presence mapping
- OAuth client discovery
- breach-to-identity correlation
- identity finding preparation

This skill is not responsible for:

- credential abuse
- phishing execution
- tenant compromise
- bypassing MFA
- persistence
- destructive testing

## Inputs

Expected inputs:

- mission context
- target domain
- authorization status
- known emails
- known tenant identifiers
- existing recon evidence
- rules of engagement

## Outputs

Expected outputs:

- identity surface summary
- tenant discovery notes
- federation status
- SSO exposure findings
- Teams federation notes
- OAuth client observations
- identity risk assessment
- recommended next steps

## Routing Rules

Use this skill when the operator asks about:

- Microsoft 365
- Entra ID
- Azure AD
- SSO
- identity fabric
- tenant GUIDs
- federation
- Teams federation
- SharePoint
- OneDrive
- OAuth client IDs
- breached employee identity risk

Do not use this skill when:

- the task is purely web app testing
- the task is unrelated to identity
- the request seeks credential abuse
- the request asks for phishing execution

## ScopeGuard Requirements

Identity mapping can expose sensitive organizational posture.

Before active validation, confirm:

- target domain is in scope
- identity infrastructure is allowed
- ROE permits identity enumeration
- no phishing or credential use is involved

If scope is unclear, provide passive guidance only.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/identity/03-identity-fabric-mapping.md`
- `playbooks/recon/01-quick-recon.md`
- `playbooks/secrets/04-secret-hunting.md`

## Libraries

Relevant libraries:

- `libraries/cloud/azure/`
- `libraries/identity/`
- `libraries/tools/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- tenant GUID notes
- federation status output
- DNS identity records
- SharePoint presence checks
- Teams federation notes
- OAuth client ID findings
- breach correlation summaries
- identity risk findings

## Mission Handoff

This skill may hand off to:

- `trident-recon`
- `trident-bugbounty`
- `trident-secret-hunter`
- `trident-cloud`
- `trident-reporting`

## Limitations

This skill must not:

- guide phishing execution
- abuse discovered credentials
- bypass MFA
- attempt unauthorized login
- overstate risk without evidence
- treat presence indicators as compromise

## Doctrine

Identity is the trust anchor.

Map carefully.

Validate safely.

Correlate evidence.

Report clearly.

Discover.

Analyze.

Act.