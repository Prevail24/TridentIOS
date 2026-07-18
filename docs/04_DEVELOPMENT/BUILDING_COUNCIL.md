# 🧠 Building Council Members

> **Designing reasoning specialists for the Trident Intelligence Operating System.**

---

# Purpose

Council Members provide structured reasoning over Mission intelligence.

Unlike Serpents, which gather intelligence, Council Members interpret, evaluate, challenge, and synthesize intelligence.

A Council Member represents a particular way of thinking.

It does not represent a particular AI model.

---

# Philosophy

The Council exists because difficult investigations rarely have one correct perspective.

Different experts ask different questions.

Different experts notice different patterns.

Different experts reach different conclusions.

Rather than relying upon one reasoning process, Trident allows multiple reasoning specialists to examine the same Mission intelligence.

---

# Responsibilities

A Council Member should:

- Analyze Mission intelligence
- Evaluate evidence
- Identify gaps
- Challenge assumptions
- Produce hypotheses
- Assess confidence
- Recommend next actions
- Produce Mission Updates when appropriate

A Council Member should never:

- Gather intelligence
- Execute tools
- Call external providers directly
- Modify Mission state
- Schedule capabilities
- Generate final reports

---

# Council Is Not AI

A Council Member is a reasoning strategy.

Examples:

- Threat Analyst
- OSINT Analyst
- Malware Analyst
- Intelligence Reviewer
- Risk Assessor
- Attribution Analyst
- Devil's Advocate
- Skeptic
- Strategic Advisor

Each represents expertise.

Not technology.

---

# The Council Lifecycle

```text
Mission Intelligence Ready

↓

Council Member Invoked

↓

Reasoning Performed

↓

Mission Update Produced

↓

Execution Complete
```

Every Council Member follows the same lifecycle.

---

# Inputs

Council Members receive scoped Mission intelligence.

Examples include:

- Observations
- Findings
- Evidence
- Entities
- Relationships
- Previous hypotheses
- Mission objectives

Council Members never access unrelated Mission data.

---

# Outputs

Council Members contribute:

- Hypotheses
- Findings
- Confidence assessments
- Recommendations
- Alternative explanations
- Intelligence gaps

Every contribution becomes a Mission Update.

---

# Multiple Perspectives

A Mission may invoke multiple Council Members.

Example:

```text
Threat Analyst

↓

Risk Analyst

↓

Infrastructure Analyst

↓

Devil's Advocate

↓

Consensus
```

Different perspectives improve investigative quality.

---

# Consensus

Consensus is optional.

Council Members may disagree.

Disagreement is valuable intelligence.

The platform should preserve minority opinions whenever appropriate.

---

# Reasoning Style

Each Council Member should have a clearly defined reasoning style.

Examples:

Threat Analyst

Focus:

- Tactics
- Techniques
- Procedures

Risk Analyst

Focus:

- Business impact
- Likelihood
- Severity

Devil's Advocate

Focus:

- Alternative explanations
- Contradictory evidence
- Missing assumptions

Every reasoning style should be explicit.

---

# AI Independence

Council Members should request reasoning services through Providers.

Example:

```python
reasoner = providers.get("ai.chat")
```

Never instantiate vendor SDKs directly.

Changing AI providers should not require rewriting reasoning logic.

---

# Explainability

Every conclusion should include supporting evidence whenever possible.

Good:

```text
Confidence: High

Evidence:

- Observation 12
- Observation 18
- Finding 7
```

Poor:

```text
I think this is malware.
```

Reasoning should be inspectable.

---

# Confidence

Council Members should communicate confidence explicitly.

Suggested values:

- Unknown
- Low
- Medium
- High
- Confirmed

Confidence reflects evidence quality.

Not model confidence.

---

# Challenge Assumptions

Good Council Members ask:

- What evidence is missing?
- What assumptions exist?
- Could another explanation fit?
- What would disprove this conclusion?
- What additional intelligence is needed?

Reasoning should reduce uncertainty.

---

# Human Authority

Council recommendations remain recommendations.

The Observer retains authority.

Council Members advise.

They do not decide.

---

# Mission Updates

Reasoning results become Mission Updates.

Examples:

- Hypothesis
- Recommendation
- Finding
- Confidence Adjustment

Reasoning never modifies Mission state directly.

---

# Events

Operational Events describe Council execution.

Examples:

```text
Council.Member.Started

Council.Member.Completed

Council.Member.Failed
```

Events communicate execution.

Mission Updates communicate reasoning.

---

# Testing

Council Members should support:

- Mock Mission Context
- Mock Providers
- Replay testing
- Contract validation
- Deterministic prompt tests where possible

Reasoning should be reproducible whenever practical.

---

# Prompt Design

If AI is used, prompts should be:

- Structured
- Explicit
- Role-specific
- Versioned
- Reviewed

Prompt engineering is part of the implementation, not the architecture.

---

# Best Practices

Council Members should:

- Stay focused
- Avoid unsupported conclusions
- Cite evidence
- Preserve uncertainty
- Encourage additional investigation when needed

---

# Anti-Patterns

Avoid:

- Acting as a Serpent
- Calling external APIs directly
- Scheduling capabilities
- Producing reports
- Assuming AI is always correct
- Hiding uncertainty

Reasoning should remain transparent.

---

# Example

```text
Mission Intelligence

↓

Threat Analyst

↓

Hypothesis

↓

Mission Update
```

The Council interprets intelligence.

It does not collect it.

---

# Summary

Council Members are reasoning specialists.

They examine Mission intelligence from defined perspectives, challenge assumptions, generate hypotheses, assess confidence, and recommend future action.

They gather no intelligence themselves.

They transform intelligence into understanding.

---

> **Serpents discover.**

> **Council Members reason.**

> **The Observer decides.**

🔱