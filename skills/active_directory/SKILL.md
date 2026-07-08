# 🔱 TRIDENT ACTIVE DIRECTORY SKILL

## Skill Name

`trident-active-directory`

## Purpose

Guide authorized Active Directory enumeration, analysis, hardening review, and lab-safe attack-path reasoning.

## Mission Phase

Primary phase:

- Discover
- Analyze

## Responsibilities

This skill is responsible for:

- AD environment mapping
- domain/user/group review
- trust relationship analysis
- GPO review
- Kerberos concept support
- BloodHound-style attack-path analysis
- defensive hardening observations
- lab and authorized engagement support
- evidence capture

This skill is not responsible for:

- unauthorized domain compromise
- credential theft
- persistence
- stealth
- destructive actions
- real-world abuse without authorization

## Inputs

Expected inputs:

- mission context
- authorization status
- domain name
- user context
- collected AD data
- BloodHound notes
- command outputs
- existing evidence

## Outputs

Expected outputs:

- AD map
- user/group notes
- privilege relationship notes
- attack-path hypotheses
- hardening recommendations
- evidence records
- reporting handoff

## Routing Rules

Use this skill when the operator asks about:

- Active Directory
- domain enumeration
- Kerberos
- LDAP
- BloodHound
- users and groups
- GPOs
- AD privilege paths
- Windows domain labs

Do not use this skill when:

- the request targets an unauthorized domain
- the task is standalone Windows host review
- the task is cloud identity only
- the request asks for stealth, persistence, or credential abuse

## ScopeGuard Requirements

Before operational AD guidance, confirm:

- the domain is a lab, owned environment, or authorized engagement
- data collection is allowed
- credential use is authorized
- destructive or stealth actions are avoided

If scope is unknown, provide defensive or lab-safe conceptual guidance only.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/active-directory/`
- `playbooks/windows/`
- `playbooks/ctf/`

## Libraries

Relevant libraries:

- `libraries/active-directory/`
- `libraries/windows/`
- `libraries/tools/bloodhound/`
- `libraries/mitre/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- AD relationship notes
- BloodHound observations
- user/group summaries
- privilege path notes
- hardening recommendations
- screenshots
- findings

## Mission Handoff

This skill may hand off to:

- `trident-windows`
- `trident-identity`
- `trident-reporting`
- `trident-evidence`
- `trident-analysis`

## Limitations

This skill must not:

- guide unauthorized domain compromise
- encourage stealth
- provide persistence guidance
- abuse credentials
- invent relationships
- skip evidence capture

## Doctrine

Map relationships.

Understand privilege.

Validate safely.

Defend clearly.

Evidence before conclusions.

Discover.

Analyze.

Act.