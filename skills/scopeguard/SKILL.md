# 🔱 TRIDENT SCOPEGUARD SKILL

## Skill Name

`trident-scopeguard`

## Purpose

Evaluate authorization, scope, engagement boundaries, and rules of engagement before Trident provides operational security guidance.

## Mission Phase

Primary phase:

- Discover
- Analyze
- Act

## Responsibilities

This skill is responsible for:

- scope review
- authorization checks
- engagement classification
- allowed asset tracking
- excluded asset tracking
- prohibited action tracking
- warning generation
- safe redirection

This skill is not responsible for:

- performing recon
- running tests
- writing final reports
- bypassing safety boundaries
- approving illegal activity

## Inputs

Expected inputs:

- mission context
- target
- engagement type
- authorization status
- allowed assets
- excluded assets
- rules of engagement
- requested action

## Outputs

Expected outputs:

- scope status
- warning message
- allowed action summary
- prohibited action summary
- next safe step
- handoff recommendation

## Routing Rules

Use this skill when:

- scope is unclear
- authorization is unclear
- the operator requests active testing
- the target may be out of scope
- ROE needs review
- prohibited actions may be involved

Do not use this skill when:

- the request is purely general education
- the mission scope is already clear and passive
- another skill only needs normal documentation help

## ScopeGuard Requirements

Scope states:

- confirmed
- unknown
- out_of_scope
- prohibited

Modes:

- off
- advisory
- confirm
- enforce

Default:

```yaml
scopeguard:
  enabled: true
  mode: advisory

  # 🔱 TRIDENT SCOPEGUARD SKILL

## Skill Name

`trident-scopeguard`

## Purpose

Evaluate authorization, scope, engagement boundaries, and rules of engagement before Trident provides operational security guidance.

## Mission Phase

Primary phase:

- Discover
- Analyze
- Act

## Responsibilities

This skill is responsible for:

- scope review
- authorization checks
- engagement classification
- allowed asset tracking
- excluded asset tracking
- prohibited action tracking
- warning generation
- safe redirection

This skill is not responsible for:

- performing recon
- running tests
- writing final reports
- bypassing safety boundaries
- approving illegal activity

## Inputs

Expected inputs:

- mission context
- target
- engagement type
- authorization status
- allowed assets
- excluded assets
- rules of engagement
- requested action

## Outputs

Expected outputs:

- scope status
- warning message
- allowed action summary
- prohibited action summary
- next safe step
- handoff recommendation

## Routing Rules

Use this skill when:

- scope is unclear
- authorization is unclear
- the operator requests active testing
- the target may be out of scope
- ROE needs review
- prohibited actions may be involved

Do not use this skill when:

- the request is purely general education
- the mission scope is already clear and passive
- another skill only needs normal documentation help

## ScopeGuard Requirements

Scope states:

- confirmed
- unknown
- out_of_scope
- prohibited

Modes:

- off
- advisory
- confirm
- enforce

Default:

```yaml
scopeguard:
  enabled: true
  mode: advisory

  # 🔱 TRIDENT SCOPEGUARD SKILL

## Skill Name

`trident-scopeguard`

## Purpose

Evaluate authorization, scope, engagement boundaries, and rules of engagement before Trident provides operational security guidance.

## Mission Phase

Primary phase:

- Discover
- Analyze
- Act

## Responsibilities

This skill is responsible for:

- scope review
- authorization checks
- engagement classification
- allowed asset tracking
- excluded asset tracking
- prohibited action tracking
- warning generation
- safe redirection

This skill is not responsible for:

- performing recon
- running tests
- writing final reports
- bypassing safety boundaries
- approving illegal activity

## Inputs

Expected inputs:

- mission context
- target
- engagement type
- authorization status
- allowed assets
- excluded assets
- rules of engagement
- requested action

## Outputs

Expected outputs:

- scope status
- warning message
- allowed action summary
- prohibited action summary
- next safe step
- handoff recommendation

## Routing Rules

Use this skill when:

- scope is unclear
- authorization is unclear
- the operator requests active testing
- the target may be out of scope
- ROE needs review
- prohibited actions may be involved

Do not use this skill when:

- the request is purely general education
- the mission scope is already clear and passive
- another skill only needs normal documentation help

## ScopeGuard Requirements

Scope states:

- confirmed
- unknown
- out_of_scope
- prohibited

Modes:

- off
- advisory
- confirm
- enforce

Default:

```yaml
scopeguard:
  enabled: true
  mode: advisory
```


  Warning:
  ⚠️ ATTENTION: Target may be outside confirmed scope.
Proceed only if you have authorization.

Hard rule:

No scope. No strike.

Playbooks

Relevant playbooks:

* playbooks/scopeguard/
* playbooks/bug-bounty/02-bug-bounty-workflow.md
* playbooks/pentesting/

Libraries

Relevant libraries:

* libraries/templates/
* libraries/legal/
* libraries/roe/

Evidence Produced

This skill may produce:

* scope summaries
* ROE notes
* allowed asset lists
* excluded asset lists
* authorization notes
* safety warnings

Mission Handoff

This skill may hand off to:

* trident-mission-control
* trident-recon
* trident-bugbounty
* trident-pentesting
* trident-reporting

Limitations

This skill must not:

* invent authorization
* approve prohibited activity
* ignore out-of-scope assets
* replace legal review
* block safe education unnecessarily

Doctrine

Scope defines the mission.

Warnings protect the operator.

Authorization enables action.

Out of scope means redirect.

No scope. No strike.

Discover.

Analyze.

Act.