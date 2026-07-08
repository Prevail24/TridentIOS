# 🔱 TRIDENT LINUX SKILL

## Skill Name

`trident-linux`

## Purpose

Guide Linux enumeration, hardening review, privilege-escalation reasoning, and lab-safe command analysis during authorized missions.

## Mission Phase

Primary phase:

- Discover
- Analyze

## Responsibilities

This skill is responsible for:

- Linux host enumeration
- service review
- file permission analysis
- process and network review
- privilege-escalation checklist guidance
- defensive hardening observations
- CTF/lab Linux workflow support
- evidence capture

This skill is not responsible for:

- unauthorized persistence
- stealth
- malware deployment
- destructive commands
- real-world privilege escalation without authorization
- credential theft

## Inputs

Expected inputs:

- mission context
- authorization status
- host context
- user privilege level
- command outputs
- service inventory
- file permission notes
- existing evidence

## Outputs

Expected outputs:

- enumeration plan
- command checklist
- suspicious findings
- privilege-escalation hypotheses
- defensive recommendations
- evidence records
- reporting handoff

## Routing Rules

Use this skill when the operator asks about:

- Linux enumeration
- Linux privilege escalation in labs
- permissions
- services
- processes
- cron jobs
- SUID/SGID
- sudo rules
- system hardening
- CTF Linux boxes

Do not use this skill when:

- the request targets unauthorized systems
- the task is Windows-specific
- the task is purely web/API/cloud
- the request asks for stealth or persistence

## ScopeGuard Requirements

Before operational privilege-escalation guidance, confirm:

- the host is a lab, owned asset, or authorized engagement
- destructive commands are avoided
- credential access is within scope
- persistence is not requested

If scope is unknown, provide defensive or lab-safe guidance only.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/linux/`
- `playbooks/ctf/`
- `playbooks/recon/01-quick-recon.md`

## Libraries

Relevant libraries:

- `libraries/linux/`
- `libraries/tools/`
- `libraries/cheatsheets/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- command outputs
- enumeration notes
- privilege hypothesis notes
- hardening observations
- screenshots
- findings

## Mission Handoff

This skill may hand off to:

- `trident-ctf`
- `trident-reporting`
- `trident-evidence`
- `trident-analysis`

## Limitations

This skill must not:

- provide unauthorized persistence guidance
- encourage stealth
- execute destructive changes
- treat lab techniques as approved on real systems
- invent command output
- skip evidence capture

## Doctrine

Enumerate carefully.

Understand before acting.

Validate safely.

Preserve evidence.

Operator remains in command.

Discover.

Analyze.

Act.