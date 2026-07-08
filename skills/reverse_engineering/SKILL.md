# 🔱 TRIDENT REVERSE ENGINEERING SKILL

## Skill Name

`trident-reverse-engineering`

## Purpose

Support authorized reverse engineering, binary analysis, firmware review, malware triage, and lab-safe technical investigation.

## Mission Phase

Primary phase:

- Discover
- Analyze

## Responsibilities

This skill is responsible for:

- static analysis planning
- binary metadata review
- string and symbol analysis
- file format identification
- firmware extraction guidance
- malware triage at a defensive level
- behavior hypothesis development
- evidence capture

This skill is not responsible for:

- malware deployment
- weaponization
- stealth
- evasion
- unauthorized exploitation
- persistence development

## Inputs

Expected inputs:

- mission context
- file type
- hash
- sample origin
- authorization status
- analysis goal
- tool outputs
- existing evidence

## Outputs

Expected outputs:

- analysis plan
- file metadata summary
- string observations
- behavior hypotheses
- suspicious capability notes
- IOC candidates
- evidence records
- reporting handoff

## Routing Rules

Use this skill when the operator asks about:

- reverse engineering
- binaries
- firmware
- strings
- Ghidra
- IDA
- radare2
- malware triage
- file hashes
- suspicious samples

Do not use this skill when:

- the request asks to build malware
- the request asks for evasion
- the request asks for weaponization
- the task is purely web/API/cloud

## ScopeGuard Requirements

Before analysis, confirm:

- sample handling is authorized
- environment is controlled
- no live deployment is requested
- no weaponization is requested
- evidence is preserved

Unknown or suspicious samples should be handled in isolated lab environments.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/reverse-engineering/`
- `playbooks/malware-analysis/`
- `playbooks/dfir/`

## Libraries

Relevant libraries:

- `libraries/reverse-engineering/`
- `libraries/malware-analysis/`
- `libraries/tools/ghidra/`
- `libraries/tools/radare2/`
- `libraries/iocs/`

## Evidence Produced

This skill may produce:

- hashes
- metadata notes
- strings output
- symbol notes
- capability hypotheses
- IOC candidates
- screenshots
- triage summaries

## Mission Handoff

This skill may hand off to:

- `trident-dfir`
- `trident-threat-intel`
- `trident-evidence`
- `trident-reporting`

## Limitations

This skill must not:

- help create malware
- help evade detection
- help deploy payloads
- provide persistence logic
- overstate behavior without evidence
- skip safe handling guidance

## Doctrine

Handle samples carefully.

Analyze before concluding.

Separate capability from intent.

Preserve evidence.

Report defensively.

Discover.

Analyze.

Act.