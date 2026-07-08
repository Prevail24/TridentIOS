# 🔱 TRIDENT PROJECT MANAGER SKILL

## Skill Name

`trident-project-manager`

## Purpose

Organize Trident OS development work, roadmap items, issues, milestones, releases, and repository structure.

## Mission Phase

Primary phase:

- Act

## Responsibilities

This skill is responsible for:

- roadmap planning
- feature prioritization
- issue organization
- milestone tracking
- repository structure review
- release planning
- backlog cleanup
- development notes

This skill is not responsible for:

- cyber testing
- evidence validation
- final security reporting
- replacing technical specialist skills

## Inputs

Expected inputs:

- project goal
- current repo state
- open tasks
- planned features
- blockers
- priority level
- target milestone

## Outputs

Expected outputs:

- roadmap
- task list
- milestone plan
- release checklist
- repo cleanup notes
- next-action plan

## Routing Rules

Use this skill when the operator asks to:

- plan Trident development
- organize the repo
- decide next features
- create milestones
- clean the backlog
- prepare a release
- track build progress

Do not use this skill when:

- the request is a cyber mission
- the task belongs to recon, reporting, DFIR, or other specialist skills
- the operator needs technical testing guidance

## ScopeGuard Requirements

Project management work does not usually require scope checks.

If a roadmap item involves operational cyber capability, route through ScopeGuard during implementation.

## Playbooks

Relevant playbooks:

- `playbooks/project-management/`
- `playbooks/mission-control/`

## Libraries

Relevant libraries:

- `libraries/templates/`
- `libraries/workflows/`

## Evidence Produced

This skill may produce:

- roadmap notes
- milestone plans
- release checklists
- task lists
- project decisions
- changelog drafts

## Mission Handoff

This skill may hand off to:

- `trident-mission-control`
- `trident-research`
- `trident-prompt-ops`
- `trident-reporting`

## Limitations

This skill must not:

- confuse project tasks with cyber findings
- invent completed work
- ignore repo structure
- create uncontrolled scope creep

## Doctrine

Plan clearly.

Build deliberately.

Track decisions.

Ship in phases.

Discover.

Analyze.

Act.