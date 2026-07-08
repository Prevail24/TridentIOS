# 🔱 TRIDENT RECON SKILL

## Skill Name

`trident-recon`

## Purpose

Discover and organize a target's exposed attack surface using authorized, scoped, and evidence-driven reconnaissance.

This skill exists to:

- identify assets
- map domains, subdomains, IPs, and exposed services
- collect passive intelligence
- prioritize high-value attack surface
- produce recon evidence for later analysis

## Mission Phase

Primary phase:

- Discover

## Responsibilities

This skill is responsible for:

- passive recon planning
- target seed discovery
- subdomain enumeration
- DNS and CT log review
- public service discovery
- basic technology fingerprinting
- recon evidence organization
- handoff to analysis, bug bounty, web, API, cloud, or reporting skills

This skill is not responsible for:

- exploitation
- persistence
- credential abuse
- destructive testing
- final report writing
- severity scoring beyond initial triage

## Inputs

Expected inputs:

- mission context
- target domain or asset
- scope status
- time budget
- allowed assets
- excluded assets
- existing evidence

## Outputs

Expected outputs:

- recon plan
- target list
- subdomain list
- DNS records
- IP list
- exposed services
- interesting web targets
- evidence index entries
- recommended next steps

## Routing Rules

Use this skill when the operator asks to:

- start recon
- map attack surface
- enumerate assets
- perform quick recon
- organize discovered hosts
- identify high-value targets

Do not use this skill when the request is primarily:

- final reporting
- exploit development
- malware analysis
- reverse engineering
- post-exploitation
- unrelated general advice

## ScopeGuard Requirements

Recon may be passive or active.

If scope is unknown, prefer passive sources and warn the operator before active probing.

For active scanning or intrusive enumeration, require confirmed authorization.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/recon/01-quick-recon.md`
- `playbooks/bug-bounty/02-bug-bounty-workflow.md`

## Libraries

Relevant libraries:

- `libraries/tools/`
- `libraries/dorks/`
- `libraries/regex/`
- `libraries/references/`

## Evidence Produced

This skill may produce:

- WHOIS output
- RDAP output
- DNS records
- CT log subdomains
- subfinder output
- resolved IP lists
- Shodan InternetDB results
- email lists
- breach lookup summaries
- recon notes
- target priority lists

## Mission Handoff

This skill may hand off to:

- `trident-bugbounty`
- `trident-web`
- `trident-api`
- `trident-cloud`
- `trident-identity`
- `trident-reporting`

## Limitations

This skill must not:

- attack unknown targets
- provide exploitation steps for out-of-scope assets
- invent assets
- exaggerate exposure
- skip evidence capture
- treat passive discovery as proof of vulnerability

## Doctrine

Discover first.

Map before testing.

Evidence before conclusions.

Scope before strike.

Operator remains in command.

Discover.

Analyze.

Act.