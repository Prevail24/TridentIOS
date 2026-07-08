# 🔱 TRIDENT DFIR SKILL

## Skill Name

`trident-dfir`

## Purpose

Support defensive incident response, forensic triage, log review, timeline construction, and evidence-based investigation.

## Mission Phase

Primary phase:

- Discover
- Analyze
- Act

## Responsibilities

This skill is responsible for:

- incident triage
- log review planning
- timeline construction
- suspicious activity analysis
- artifact interpretation
- containment recommendation support
- evidence preservation guidance
- incident summary preparation

This skill is not responsible for:

- unauthorized access
- attacker emulation without approval
- malware deployment
- evidence destruction
- stealth
- retaliatory activity

## Inputs

Expected inputs:

- mission context
- incident description
- affected systems
- logs
- alerts
- timestamps
- indicators
- evidence artifacts

## Outputs

Expected outputs:

- triage plan
- timeline
- suspicious event summary
- affected asset list
- confidence-rated findings
- containment recommendations
- incident report handoff

## Routing Rules

Use this skill when the operator asks about:

- incident response
- forensics
- log analysis
- suspicious events
- compromise investigation
- timelines
- containment
- eradication
- recovery
- post-incident lessons

Do not use this skill when:

- the request is offensive testing
- the request asks for retaliation
- the request seeks stealth or persistence
- the task is unrelated to incident evidence

## ScopeGuard Requirements

DFIR work should be performed on systems the operator owns, administers, or is authorized to investigate.

If ownership or authorization is unclear, provide general defensive guidance only.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/dfir/`
- `playbooks/threat-intel/`

## Libraries

Relevant libraries:

- `libraries/dfir/`
- `libraries/logs/`
- `libraries/mitre/`
- `libraries/iocs/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- incident timelines
- log summaries
- artifact notes
- IOC tables
- affected asset lists
- containment notes
- lessons learned

## Mission Handoff

This skill may hand off to:

- `trident-threat-intel`
- `trident-evidence`
- `trident-reporting`
- `trident-analysis`

## Limitations

This skill must not:

- destroy evidence
- invent timelines
- overstate compromise
- encourage retaliation
- hide uncertainty
- skip evidence preservation

## Doctrine

Preserve evidence.

Build the timeline.

Correlate events.

Contain carefully.

Report clearly.

Discover.

Analyze.

Act.