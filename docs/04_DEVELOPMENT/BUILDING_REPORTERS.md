# 📢 Building Reporters

> **Designing communication specialists for the Trident Intelligence Operating System.**

---

# Purpose

Reporters transform Mission intelligence into human-readable outputs.

A Reporter is responsible for communicating intelligence.

It never creates intelligence.

It never modifies intelligence.

Its responsibility is presentation.

---

# Philosophy

A Mission may contain thousands of observations.

Humans should not have to read thousands of observations.

Reporters transform structured intelligence into clear communication.

Good reporting increases understanding.

It should never distort truth.

---

# Responsibilities

A Reporter should:

- Read Mission intelligence
- Organize information
- Summarize findings
- Generate visualizations
- Produce reports
- Produce briefings
- Format outputs

A Reporter should never:

- Execute capabilities
- Gather intelligence
- Reason about evidence
- Modify Mission state
- Promote knowledge into Loom

---

# Reporter Is Presentation

Reporter answers:

> "How should this intelligence be communicated?"

It does not answer:

> "Is this intelligence correct?"

Truth belongs to the Mission.

Presentation belongs to Reporter.

---

# Reporter Lifecycle

```text
Mission Complete

↓

Mission Intelligence Retrieved

↓

Content Organized

↓

Output Generated

↓

Report Delivered
```

---

# Inputs

Reporters consume structured Mission intelligence.

Examples include:

- Observations
- Findings
- Evidence
- Entities
- Relationships
- Recommendations
- Timelines
- Confidence Levels

They never consume raw provider responses directly.

---

# Outputs

Possible outputs include:

- Markdown
- HTML
- PDF
- DOCX
- JSON
- Executive Briefing
- Technical Report
- Timeline
- IOC List
- Threat Summary
- Intelligence Bulletin

Every output represents the same intelligence.

Only the presentation changes.

---

# Separation of Concerns

Mission owns intelligence.

Reporter owns presentation.

This separation allows:

```text
One Mission

↓

Executive Report

Technical Report

Timeline

Incident Summary

IOC Export

Dashboard
```

Multiple audiences.

One source of truth.

---

# Audience-Aware Reporting

Different audiences require different communication.

Examples:

Executive

Focus:

- Risk
- Impact
- Recommendations

Technical Analyst

Focus:

- Evidence
- Timeline
- Indicators
- Commands

Incident Response

Focus:

- Immediate actions
- Containment
- Recovery

Reporter adapts communication.

It does not change intelligence.

---

# Templates

Reporters should support reusable templates.

Examples:

- Executive Summary
- Incident Report
- Threat Intelligence Report
- OSINT Report
- Malware Analysis
- HTB Walkthrough

Templates standardize communication.

---

# Visualizations

Reporters may generate:

- Timelines
- Graphs
- Relationship Maps
- Tables
- Statistics
- Charts
- Network Diagrams

Visuals should clarify intelligence.

Not decorate it.

---

# Confidence

Confidence should always be preserved.

Example:

```text
Finding

Confidence: High
```

Reporters should never hide uncertainty.

---

# Evidence

Every significant conclusion should reference supporting evidence.

Good:

```text
Finding:

SMB Signing Disabled

Evidence:

Observation 14

Observation 22
```

Readers should be able to verify conclusions.

---

# Traceability

Every statement should be traceable to Mission intelligence.

Reporter should never invent information.

---

# Mission Updates

Reporters generally do not create Mission Updates.

Their responsibility begins after intelligence has already been produced.

The report itself is an output artifact.

Not new intelligence.

---

# Events

Reporter publishes operational Events.

Examples:

```text
Reporter.Started

Reporter.Completed

Report.Generated

Report.Delivered

Reporter.Failed
```

Events describe communication.

Not intelligence.

---

# Styling

Report styling should remain independent from content.

Example:

```text
Markdown

↓

HTML Theme

↓

PDF Theme

↓

Dark Theme

↓

Corporate Theme
```

Presentation should be replaceable.

---

# Localization

Future Reporters may support:

- Multiple languages
- Regional formats
- Accessibility standards
- Localization

The underlying intelligence remains unchanged.

---

# Delivery

Reporters may deliver outputs through:

- Files
- Email
- Web UI
- APIs
- Dashboards
- Messaging Platforms
- Knowledge Systems

Delivery mechanisms are separate from report generation.

---

# Security

Reports should respect Mission permissions.

Sensitive information may require:

- Redaction
- Classification labels
- Audience filtering
- Approval workflows

Communication should never violate Mission security.

---

# Testing

Reporters should support:

- Template validation
- Rendering tests
- Snapshot tests
- Accessibility checks
- Output consistency tests

Presentation should be predictable.

---

# Best Practices

Good Reporters:

- Preserve traceability
- Preserve confidence
- Preserve evidence
- Use clear language
- Respect audience needs
- Remain deterministic where practical

---

# Anti-Patterns

Avoid:

- Inventing conclusions
- Changing confidence
- Omitting evidence
- Performing analysis
- Calling Providers
- Executing capabilities

Reporter communicates.

It does not investigate.

---

# Example

```text
Mission Intelligence

↓

Executive Reporter

↓

Executive Briefing
```

or

```text
Mission Intelligence

↓

Timeline Reporter

↓

Chronological Investigation Timeline
```

Different Reporters.

Same intelligence.

---

# Future Vision

Future Reporter capabilities may include:

- Interactive dashboards
- Live Mission briefings
- AI-assisted summaries
- Collaborative reports
- Streaming reports
- Voice briefings
- Video generation
- Executive presentation decks

As communication evolves, the underlying Mission remains the single source of truth.

---

# Summary

Reporters transform structured Mission intelligence into clear communication.

They organize information for different audiences without changing the intelligence itself.

By separating presentation from investigation, Trident allows one Mission to produce many forms of communication while preserving consistency, traceability, and explainability.

---

> **The Mission discovers.**

> **The Council understands.**

> **Reporter communicates.**

🔱