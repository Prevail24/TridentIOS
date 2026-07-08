# 🔱 TRIDENT ASSET INVENTORY SKILL

## Skill Name

`trident-asset-inventory`

## Purpose

Organize discovered assets into a clear, searchable inventory that supports recon, analysis, testing, evidence, and reporting.

## Mission Phase

Primary phase:

- Discover
- Analyze

## Responsibilities

This skill is responsible for:

- asset cataloging
- domain tracking
- subdomain tracking
- IP tracking
- service tracking
- technology tagging
- ownership notes
- scope classification
- priority labeling

This skill is not responsible for:

- active exploitation
- vulnerability validation
- final reporting alone
- inventing asset ownership
- ignoring scope boundaries

## Inputs

Expected inputs:

- mission context
- scope
- discovered domains
- subdomains
- IPs
- URLs
- services
- technologies
- evidence paths

## Outputs

Expected outputs:

- asset inventory
- scoped asset table
- excluded asset table
- priority target list
- unknown ownership list
- analysis handoff
- evidence references

## Routing Rules

Use this skill when the operator asks to:

- organize assets
- build an inventory
- sort recon results
- classify in-scope assets
- prioritize discovered hosts
- identify unknown ownership
- prepare targets for testing

Do not use this skill when:

- the request is active testing
- the request is final report writing
- the request is unrelated to mission assets

## ScopeGuard Requirements

Every asset should be classified as:

- in scope
- out of scope
- unknown
- third party
- duplicate
- retired
- high priority

Unknown assets require caution before active testing.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/recon/01-quick-recon.md`
- `playbooks/bug-bounty/02-bug-bounty-workflow.md`

## Libraries

Relevant libraries:

- `libraries/templates/`
- `libraries/recon/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- asset inventories
- target priority lists
- ownership notes
- scope classification tables
- duplicate asset notes
- unknown asset lists

## Mission Handoff

This skill may hand off to:

- `trident-recon`
- `trident-analysis`
- `trident-web`
- `trident-api`
- `trident-cloud`
- `trident-reporting`

## Limitations

This skill must not:

- assume ownership without evidence
- mark assets in scope without authorization
- ignore excluded assets
- treat discovery as vulnerability
- skip evidence references

## Doctrine

Inventory creates clarity.

Scope classifies targets.

Priority guides effort.

Evidence supports ownership.

Discover.

Analyze.

Act.