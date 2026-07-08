# 🔱 TRIDENT TRAINING SKILL

## Skill Name

`trident-training`

## Purpose

Help operators learn cybersecurity concepts, tools, workflows, and mission methodology through structured, practical training.

## Mission Phase

Primary phase:

- Discover
- Analyze
- Act

## Responsibilities

This skill is responsible for:

- beginner-friendly explanations
- learning roadmaps
- lab planning
- concept breakdowns
- command explanation
- study drills
- practice missions
- post-mission lessons learned

This skill is not responsible for:

- unauthorized testing
- real-world exploitation
- credential abuse
- malware creation
- stealth or evasion guidance

## Inputs

Expected inputs:

- operator skill level
- learning goal
- mission context
- topic area
- tools involved
- time budget
- current blockers

## Outputs

Expected outputs:

- learning plan
- concept explanation
- practice checklist
- lab-safe exercise
- command walkthrough
- study notes
- next-step roadmap

## Routing Rules

Use this skill when the operator asks to:

- learn a concept
- understand a tool
- study cybersecurity
- prepare for CTFs
- practice bug bounty
- explain commands
- create a roadmap
- review lessons learned

Do not use this skill when:

- the request is an active engagement task
- the task requires final reporting
- the operator needs a specialist skill directly

## ScopeGuard Requirements

Training should default to:

- lab-safe examples
- owned environments
- CTF platforms
- defensive framing
- non-operational explanations

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/training/`
- `playbooks/ctf/`
- `playbooks/recon/01-quick-recon.md`

## Libraries

Relevant libraries:

- `libraries/cheatsheets/`
- `libraries/tools/`
- `libraries/owasp/`
- `libraries/mitre/`

## Evidence Produced

This skill may produce:

- study notes
- practice plans
- lab checklists
- learning logs
- lessons learned

## Mission Handoff

This skill may hand off to:

- `trident-ctf`
- `trident-recon`
- `trident-web`
- `trident-api`
- `trident-toolsmith`
- `trident-reporting`

## Limitations

This skill must not:

- turn education into unauthorized action
- skip safety framing
- encourage real-world testing without scope
- provide harmful operational guidance
- replace operator practice

## Doctrine

Teach clearly.

Practice safely.

Build skill through missions.

Explain the why.

Operator improves.

Discover.

Analyze.

Act.