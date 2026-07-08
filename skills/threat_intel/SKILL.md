# 🔱 TRIDENT THREAT INTEL SKILL

## Skill Name

`trident-threat-intel`

## Purpose

Analyze adversary behavior, indicators, TTPs, campaigns, malware families, and threat reports to support defensive and investigative missions.

## Mission Phase

Primary phase:

- Analyze

## Responsibilities

This skill is responsible for:

- indicator analysis
- TTP mapping
- campaign notes
- MITRE ATT&CK alignment
- threat report summarization
- actor behavior comparison
- defensive recommendation support
- intelligence briefing preparation

This skill is not responsible for:

- malware deployment
- unauthorized access
- offensive campaign execution
- phishing execution
- evasion guidance
- persistence guidance

## Inputs

Expected inputs:

- mission context
- indicators
- suspicious domains
- IPs
- hashes
- logs
- threat reports
- observed behavior
- existing evidence

## Outputs

Expected outputs:

- threat summary
- indicator table
- TTP map
- confidence rating
- source notes
- defensive recommendations
- intelligence brief

## Routing Rules

Use this skill when the operator asks about:

- threat intelligence
- IOCs
- MITRE ATT&CK
- threat actors
- malware families
- campaign analysis
- suspicious infrastructure
- defensive briefings

Do not use this skill when:

- the request asks to weaponize malware
- the task is purely recon
- the task is final reporting only
- the request lacks evidence or indicators

## ScopeGuard Requirements

Threat intelligence is usually analysis-focused.

If the operator asks for active probing or interaction with suspicious infrastructure, confirm authorization and safety boundaries first.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/threat-intel/`
- `playbooks/recon/01-quick-recon.md`

## Libraries

Relevant libraries:

- `libraries/mitre/`
- `libraries/threat-intel/`
- `libraries/iocs/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- IOC notes
- TTP mappings
- confidence labels
- source summaries
- timeline notes
- defensive recommendations

## Mission Handoff

This skill may hand off to:

- `trident-dfir`
- `trident-reporting`
- `trident-evidence`
- `trident-analysis`

## Limitations

This skill must not:

- invent attribution
- overstate confidence
- provide malware deployment guidance
- encourage unauthorized interaction
- treat weak indicators as confirmed compromise

## Doctrine

Correlate carefully.

Attribute cautiously.

Map behavior.

Defend clearly.

Confidence must match evidence.

Discover.

Analyze.

Act.