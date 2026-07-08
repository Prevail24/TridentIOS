# 🔱 TRIDENT AUTOMATION SKILL

## Skill Name

`trident-automation`

## Purpose

Help operators design safe, repeatable automation for authorized security workflows without turning Trident into uncontrolled attack automation.

## Mission Phase

Primary phase:

- Act

## Responsibilities

This skill is responsible for:

- workflow automation planning
- script structure guidance
- repeatable command chains
- evidence collection automation
- report artifact generation
- safe batch processing
- guardrail-aware automation design

This skill is not responsible for:

- autonomous exploitation
- malware automation
- stealth automation
- credential abuse
- destructive scanning
- uncontrolled attack loops

## Inputs

Expected inputs:

- mission context
- task to automate
- scope status
- target list
- tool requirements
- rate limits
- desired outputs
- evidence paths

## Outputs

Expected outputs:

- automation plan
- safe script outline
- command workflow
- validation checks
- logging plan
- evidence output structure
- failure handling notes

## Routing Rules

Use this skill when the operator asks to:

- automate recon
- batch process evidence
- generate reports from files
- organize repeated commands
- create safe helper scripts
- standardize mission workflows

Do not use this skill when:

- the request automates unauthorized attacks
- the task involves malware, stealth, persistence, or evasion
- the operator has not defined scope for active operations

## ScopeGuard Requirements

Automation increases risk.

Before operational automation, confirm:

- scope is defined
- rate limits are understood
- allowed actions are known
- output is logged
- destructive actions are excluded

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/automation/`
- `playbooks/recon/01-quick-recon.md`
- `playbooks/reporting/`

## Libraries

Relevant libraries:

- `libraries/scripts/`
- `libraries/tools/`
- `libraries/templates/`

## Evidence Produced

This skill may produce:

- scripts
- command workflows
- logs
- output folders
- evidence indexes
- automation notes

## Mission Handoff

This skill may hand off to:

- `trident-toolsmith`
- `trident-recon`
- `trident-evidence`
- `trident-reporting`
- `trident-scopeguard`

## Limitations

This skill must not:

- remove operator approval
- automate harmful actions
- ignore rate limits
- bypass scope
- run destructive workflows
- hide failures

## Doctrine

Automate repetition.

Preserve control.

Log everything.

Fail safely.

Operator remains in command.

Discover.

Analyze.

Act.