# 🔱 TRIDENT EVIDENCE SYSTEM

Evidence is the foundation of every Trident mission.

No evidence.

No finding.

---

# Purpose

The Evidence System ensures that every claim, finding, recommendation, and report can be traced back to supporting artifacts.

Evidence may include:

- commands
- outputs
- screenshots
- logs
- HTTP requests
- HTTP responses
- timestamps
- notes
- URLs
- files
- hashes
- tool results

---

# Evidence Philosophy

Evidence outweighs assumption.

A weak artifact produces a weak conclusion.

A strong artifact produces a strong conclusion.

Trident must never present speculation as fact.

---

# Evidence Standards

Each artifact should record:

- mission name
- target
- timestamp
- source
- command or method
- raw output
- operator notes
- confidence level
- relevance
- file path
- hash when appropriate

---

# Evidence Confidence

Use these confidence levels:

## Confirmed

Direct evidence proves the claim.

## Likely

Evidence strongly supports the claim but is not complete.

## Possible

Evidence suggests the claim but requires validation.

## Unknown

Insufficient evidence exists.

---

# Evidence Index

Every mission should maintain an evidence index.

Example:

```yaml
evidence:
  - id: EVID-001
    type: command_output
    source: subfinder
    target: acme.example
    path: evidence/subdomains.txt
    confidence: confirmed
    notes: passive subdomain enumeration

```


Artifact Naming

Use clear, consistent names.

Examples:

    evidence/
├── recon/
│   ├── subdomains.txt
│   ├── dns-records.txt
│   └── internetdb.jsonl
│
├── web/
│   ├── api-users-request.txt
│   ├── api-users-response.txt
│   └── screenshot-user-created.png
│
└── reports/
    └── evidence-index.md


    Evidence Rules

Preserve raw output.

Do not overwrite important artifacts.

Redact secrets in reports.

Keep sensitive evidence in private annexes.

Record uncertainty.

Separate facts from analysis.

⸻

Doctrine

Every finding needs evidence.

Every artifact needs context.

Every report needs traceability.

Evidence before conclusions.

Discover.

Analyze.

Act.