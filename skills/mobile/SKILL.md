# 🔱 TRIDENT MOBILE SKILL

## Skill Name

`trident-mobile`

## Purpose

Guide authorized mobile application security review for Android and iOS using scoped, evidence-driven methodology.

## Mission Phase

Primary phase:

- Discover
- Analyze

## Responsibilities

This skill is responsible for:

- mobile app triage
- APK/IPA static review planning
- package metadata review
- endpoint discovery
- embedded secret identification
- permission review
- insecure storage analysis
- mobile API handoff
- evidence capture

This skill is not responsible for:

- malware deployment
- device compromise
- unauthorized app tampering
- bypassing protections on third-party systems
- credential theft
- final report writing

## Inputs

Expected inputs:

- mission context
- app name
- platform
- package name or bundle ID
- authorization status
- app binary path or store URL
- scope rules
- existing evidence

## Outputs

Expected outputs:

- mobile review plan
- app metadata summary
- endpoint list
- permission notes
- secret candidates
- API handoff notes
- vulnerability candidates
- evidence records

## Routing Rules

Use this skill when the operator asks about:

- Android
- iOS
- APK
- IPA
- mobile app testing
- package names
- app permissions
- mobile secrets
- mobile API endpoints
- app store recon

Do not use this skill when:

- the request is purely web testing
- the task is cloud-only
- the target is not authorized
- the request asks for malware, spyware, or unauthorized device access

## ScopeGuard Requirements

Before mobile testing, confirm:

- the app is in scope
- static analysis is permitted
- dynamic testing is permitted if requested
- test accounts are authorized
- third-party systems are not targeted without scope

If scope is unknown, provide safe static-review guidance only.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/mobile/`
- `playbooks/bug-bounty/02-bug-bounty-workflow.md`
- `playbooks/secrets/04-secret-hunting.md`

## Libraries

Relevant libraries:

- `libraries/mobile/android/`
- `libraries/mobile/ios/`
- `libraries/tools/`
- `libraries/owasp/mobile/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- package metadata notes
- permission summaries
- endpoint lists
- secret candidates
- screenshots
- static analysis outputs
- vulnerability candidates

## Mission Handoff

This skill may hand off to:

- `trident-api`
- `trident-secret-hunter`
- `trident-bugbounty`
- `trident-reporting`
- `trident-evidence`

## Limitations

This skill must not:

- guide spyware creation
- bypass user consent
- attack third-party services outside scope
- extract private user data unnecessarily
- overstate static findings without validation

## Doctrine

Understand the app.

Map the endpoints.

Protect user data.

Validate safely.

Document evidence.

Discover.

Analyze.

Act.