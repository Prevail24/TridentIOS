# 🔱 TRIDENT MISSION CONTROL SKILL

## Skill Name

`trident-mission-control`

## Purpose

Create, organize, track, and update Trident missions from initial objective through completion, archive, and lessons learned.

## Mission Phase

Primary phase:

- Discover
- Analyze
- Act

## Responsibilities

This skill is responsible for:

- mission creation
- mission metadata
- phase tracking
- objective tracking
- scope summaries
- status updates
- task lists
- mission folders
- mission closure

This skill is not responsible for:

- performing specialist testing
- writing final reports alone
- replacing ScopeGuard
- inventing evidence
- bypassing authorization

## Inputs

Expected inputs:

- mission name
- operator
- objective
- engagement type
- authorization status
- scope
- rules of engagement
- time budget
- current phase
- existing evidence

## Outputs

Expected outputs:

- mission file
- mission status
- task list
- phase summary
- scope summary
- progress update
- handoff notes
- closure checklist

## Routing Rules

Use this skill when the operator asks to:

- start a mission
- create a case file
- organize an engagement
- update mission status
- track progress
- summarize what has been done
- close or archive a mission

Do not use this skill when:

- the request belongs fully to a specialist skill
- the operator only needs a technical answer
- the request is final report writing

## ScopeGuard Requirements

Every mission must record authorization context.

Required fields:

- engagement type
- allowed assets
- excluded assets
- allowed actions
- prohibited actions
- notes or ROE source

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/mission-control/`
- `playbooks/recon/01-quick-recon.md`
- `playbooks/bug-bounty/02-bug-bounty-workflow.md`

## Libraries

Relevant libraries:

- `libraries/templates/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- mission.md
- scope.md
- task lists
- phase notes
- status summaries
- closure notes
- lessons learned

## Mission Handoff

This skill may hand off to:

- `trident-scopeguard`
- `trident-recon`
- `trident-bugbounty`
- `trident-ctf`
- `trident-evidence`
- `trident-reporting`

## Limitations

This skill must not:

- invent authorization
- claim work is complete without evidence
- skip scope tracking
- perform technical specialist work alone
- lose mission context

## Doctrine

Every operation is a mission.

Every mission has state.

Every state has evidence.

Every completed mission teaches the operator.

Discover.

Analyze.

Act.