# 🔱 TRIDENT WEB SKILL

## Skill Name

`trident-web`

## Purpose

Guide authorized web application security testing through structured, scoped, evidence-driven methodology.

## Mission Phase

Primary phase:

- Discover
- Analyze

## Responsibilities

This skill is responsible for:

- web application triage
- endpoint mapping
- authentication review
- authorization flaw analysis
- input validation review
- business logic testing
- safe vulnerability validation
- evidence capture for web findings

This skill is not responsible for:

- persistence
- stealth
- destructive testing
- malware delivery
- credential theft
- final report writing

## Inputs

Expected inputs:

- mission context
- target URL
- authorization status
- scope rules
- existing recon evidence
- application notes
- captured requests/responses

## Outputs

Expected outputs:

- web testing plan
- endpoint inventory
- interesting parameters
- authentication observations
- authorization test notes
- vulnerability candidates
- evidence records
- recommended next steps

## Routing Rules

Use this skill when the operator asks about:

- web app testing
- login flows
- IDOR
- XSS
- SQL injection
- SSRF
- CSRF
- file upload testing
- session handling
- access control
- business logic flaws

Do not use this skill when:

- the request is only passive recon
- the target is not authorized
- the request is primarily API-specific
- the request is cloud infrastructure-specific
- the request belongs to final reporting

## ScopeGuard Requirements

Before active web testing, confirm:

- target is in scope
- testing actions are allowed
- rate limits are understood
- destructive actions are avoided
- account creation rules are understood

If scope is unknown, provide only safe, high-level, or lab-oriented guidance.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/bug-bounty/02-bug-bounty-workflow.md`
- `playbooks/recon/01-quick-recon.md`

## Libraries

Relevant libraries:

- `libraries/owasp/`
- `libraries/tools/burp/`
- `libraries/payloads/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- endpoint notes
- HTTP request captures
- HTTP response captures
- screenshots
- parameter lists
- auth flow notes
- vulnerability candidates
- validation notes

## Mission Handoff

This skill may hand off to:

- `trident-api`
- `trident-bugbounty`
- `trident-reporting`
- `trident-recon`
- `trident-evidence`

## Limitations

This skill must not:

- advise attacking out-of-scope applications
- encourage destructive testing
- exploit real targets without authorization
- inflate severity
- skip evidence capture
- treat scanner output as proof without validation

## Doctrine

Map the app.

Understand trust boundaries.

Validate safely.

Document clearly.

Evidence before conclusions.

Discover.

Analyze.

Act.