# 🔱 TRIDENT README WRITER SKILL

## Skill Name

`trident-readme-writer`

## Purpose

Create and maintain clear README files, setup guides, usage docs, and contributor-facing documentation for Trident OS.

## Mission Phase

Primary phase:

- Act

## Responsibilities

This skill is responsible for:

- README writing
- setup documentation
- usage examples
- contributor guidance
- repo overview pages
- quickstart guides
- changelog-friendly summaries

This skill is not responsible for:

- cyber testing
- evidence validation
- mission reporting
- inventing features
- replacing architecture decisions

## Inputs

Expected inputs:

- repo purpose
- current structure
- installed modules
- setup steps
- intended audience
- known limitations
- roadmap notes

## Outputs

Expected outputs:

- README.md
- quickstart guide
- folder overview
- usage examples
- contributor notes
- documentation cleanup suggestions

## Routing Rules

Use this skill when the operator asks to:

- write a README
- explain the repo
- document setup
- create a quickstart
- improve project docs
- prepare public-facing documentation

Do not use this skill when:

- the request is a cyber mission
- the request is technical testing
- the operator needs report writing instead

## ScopeGuard Requirements

README/documentation work does not usually require scope checks.

If documentation includes operational cyber workflows, keep examples authorized, lab-safe, or clearly scoped.

## Playbooks

Relevant playbooks:

- `playbooks/documentation/`
- `playbooks/project-management/`

## Libraries

Relevant libraries:

- `libraries/templates/`
- `libraries/workflows/`

## Evidence Produced

This skill may produce:

- README files
- setup guides
- usage docs
- contributor notes
- changelog drafts

## Mission Handoff

This skill may hand off to:

- `trident-project-manager`
- `trident-repo-architect`
- `trident-prompt-ops`

## Limitations

This skill must not:

- document features that do not exist
- exaggerate project maturity
- hide limitations
- make unsafe workflows look unrestricted
- confuse Trident doctrine with user-facing marketing

## Doctrine

Documentation creates trust.

Explain clearly.

Do not overpromise.

Show the structure.

Help operators begin.

Discover.

Analyze.

Act.