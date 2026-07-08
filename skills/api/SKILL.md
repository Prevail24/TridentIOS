# 🔱 TRIDENT API SKILL

## Skill Name

`trident-api`

## Purpose

Guide authorized API security testing through structured endpoint mapping, authentication review, authorization analysis, and evidence-driven validation.

## Mission Phase

Primary phase:

- Discover
- Analyze

## Responsibilities

This skill is responsible for:

- API endpoint mapping
- OpenAPI/Swagger discovery
- GraphQL surface review
- authentication and token flow analysis
- authorization testing strategy
- object-level access control review
- rate-limit review
- schema and parameter analysis
- evidence capture for API findings

This skill is not responsible for:

- destructive testing
- credential theft
- persistence
- stealth
- production data exfiltration
- final report writing

## Inputs

Expected inputs:

- mission context
- base API URL
- authorization status
- scope rules
- existing recon evidence
- API documentation
- captured requests/responses
- test account permissions

## Outputs

Expected outputs:

- API inventory
- endpoint map
- method list
- parameter list
- auth observations
- authorization test plan
- vulnerability candidates
- evidence records
- recommended next steps

## Routing Rules

Use this skill when the operator asks about:

- API testing
- Swagger
- OpenAPI
- GraphQL
- REST endpoints
- JWTs
- API keys
- IDOR/BOLA
- mass assignment
- rate limits
- role-based access control

Do not use this skill when:

- the request is purely browser web testing
- the request is only passive recon
- the target is not authorized
- the task belongs to cloud, identity, or reporting

## ScopeGuard Requirements

Before active API testing, confirm:

- API host is in scope
- endpoints are allowed
- test accounts are authorized
- rate limits are respected
- destructive requests are avoided
- real user data is not accessed

If scope is unknown, provide only safe, high-level, or lab-oriented guidance.

No scope. No strike.

## Playbooks

Relevant playbooks:

- `playbooks/bug-bounty/02-bug-bounty-workflow.md`
- `playbooks/recon/01-quick-recon.md`

## Libraries

Relevant libraries:

- `libraries/owasp/api-security/`
- `libraries/tools/burp/`
- `libraries/tools/postman/`
- `libraries/report-templates/`

## Evidence Produced

This skill may produce:

- endpoint inventories
- request captures
- response captures
- schema notes
- auth flow notes
- authorization test matrices
- rate-limit notes
- vulnerability candidates

## Mission Handoff

This skill may hand off to:

- `trident-web`
- `trident-bugbounty`
- `trident-reporting`
- `trident-secret-hunter`
- `trident-evidence`

## Limitations

This skill must not:

- advise attacking out-of-scope APIs
- dump production data
- bypass controls without authorization
- encourage destructive requests
- treat documentation exposure as vulnerability without context
- inflate severity without evidence

## Doctrine

Map endpoints.

Understand authorization.

Validate safely.

Protect data.

Document everything.

Discover.

Analyze.

Act.