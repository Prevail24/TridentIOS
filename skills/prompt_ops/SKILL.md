# 🔱 TRIDENT PROMPT OPS SKILL

## Skill Name

`trident-prompt-ops`

## Purpose

Design, refine, and standardize prompts that help operators use Trident skills, playbooks, and mission workflows effectively.

## Mission Phase

Primary phase:

- Discover
- Analyze
- Act

## Responsibilities

This skill is responsible for:

- prompt design
- mission prompt templates
- skill invocation prompts
- playbook execution prompts
- report generation prompts
- reusable operator commands
- prompt quality review

This skill is not responsible for:

- replacing skills
- inventing evidence
- bypassing ScopeGuard
- producing unsafe operational prompts

## Inputs

Expected inputs:

- mission context
- operator goal
- target skill
- target playbook
- desired output
- scope status
- existing evidence

## Outputs

Expected outputs:

- reusable prompts
- command templates
- workflow prompts
- mission starters
- report prompts
- quality-improved prompt variants

## Routing Rules

Use this skill when the operator asks to:

- write a better prompt
- create reusable commands
- design mission prompts
- standardize Trident usage
- improve skill interaction
- convert rough intent into precise instructions

Do not use this skill when:

- the request belongs fully to a technical specialist skill
- evidence needs to be collected first
- the request bypasses safety or scope

## ScopeGuard Requirements

Prompts must respect mission scope.

Do not create prompts that encourage unauthorized testing, credential abuse, evasion, persistence, or destructive actions.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/prompt-ops/`
- `playbooks/training/`
- `playbooks/mission-control/`

## Libraries

Relevant libraries:

- `libraries/templates/`
- `libraries/prompts/`
- `libraries/workflows/`

## Evidence Produced

This skill may produce:

- prompt templates
- mission command examples
- workflow commands
- operator macros
- prompt review notes

## Mission Handoff

This skill may hand off to:

- `trident-mission-control`
- `trident-training`
- `trident-reporting`
- `trident-research`

## Limitations

This skill must not:

- generate unsafe operational prompts
- bypass ScopeGuard
- invent context
- replace evidence
- encourage reckless automation

## Doctrine

Clear prompts create clear missions.

Reusable commands reduce friction.

Precision improves outcomes.

Scope still applies.

Discover.

Analyze.

Act.