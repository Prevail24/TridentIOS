# 🔱 TRIDENT CTF SKILL

## Skill Name

`trident-ctf`

## Purpose

Guide CTF, Hack The Box, TryHackMe, lab, and training missions through structured enumeration, analysis, exploitation reasoning, evidence capture, and writeup preparation.

## Mission Phase

Primary phase:

- Discover
- Analyze
- Act

## Responsibilities

This skill is responsible for:

- CTF mission planning
- lab-safe enumeration strategy
- challenge triage
- attack-path reasoning
- privilege escalation planning
- flag tracking
- command note organization
- CTF writeup handoff

This skill is not responsible for:

- attacking real-world targets
- unauthorized exploitation
- persistence on real systems
- credential abuse outside labs
- destructive actions

## Inputs

Expected inputs:

- mission context
- platform name
- target IP or challenge URL
- authorization status
- challenge type
- current foothold
- existing notes
- evidence collected

## Outputs

Expected outputs:

- enumeration plan
- service notes
- attack-path hypotheses
- privilege escalation checklist
- command log
- flag record
- writeup outline
- next-step recommendations

## Routing Rules

Use this skill when the operator asks about:

- Hack The Box
- TryHackMe
- PicoCTF
- CTF challenges
- lab boxes
- flags
- footholds
- privilege escalation in a lab
- challenge writeups

Do not use this skill when:

- the target is a real-world system without authorization
- the request belongs to bug bounty
- the task is purely reporting
- the operator is asking for real-world credential abuse

## ScopeGuard Requirements

CTF and lab environments are allowed when authorization is clear.

Confirmed lab examples:

- Hack The Box
- TryHackMe
- PortSwigger Academy
- PicoCTF
- local vulnerable machines
- intentionally vulnerable labs

If the environment is unclear, ask whether it is a lab, CTF, owned asset, or authorized engagement.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/ctf/`
- `playbooks/recon/01-quick-recon.md`
- `playbooks/web/`
- `playbooks/linux/`
- `playbooks/windows/`

## Libraries

Relevant libraries:

- `libraries/tools/`
- `libraries/cheatsheets/`
- `libraries/payloads/lab-safe/`
- `libraries/writeups/`

## Evidence Produced

This skill may produce:

- scan notes
- command logs
- service inventories
- exploit hypotheses
- screenshots
- flag records
- privilege escalation notes
- writeup drafts

## Mission Handoff

This skill may hand off to:

- `trident-recon`
- `trident-web`
- `trident-api`
- `trident-linux`
- `trident-windows`
- `trident-reporting`

## Limitations

This skill must not:

- transfer lab exploitation guidance to unauthorized real targets
- hide uncertainty
- skip enumeration
- invent flags
- ignore scope
- present guesses as confirmed

## Doctrine

Enumerate first.

Think before firing.

Capture evidence.

Track the path.

Write the lesson.

Discover.

Analyze.

Act.