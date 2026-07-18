# 🚀 Quick Start

> **Complete your first Trident Mission in under five minutes.**

---

# Welcome

This guide introduces the core workflow of the Trident Intelligence Operating System.

By the end of this tutorial you will have:

- Created a Mission
- Executed a capability
- Produced Mission Updates
- Viewed structured intelligence
- Generated your first report

No prior knowledge of Trident's architecture is required.

---

# Step 1 — Start Trident

Launch Trident.

```bash
trident
```

or

```bash
python -m trident
```

You should see something similar to:

```text
🔱 Trident Intelligence Operating System

Version: 0.1

Providers Loaded: 3

Capabilities Loaded: 27

Ready.
```

---

# Step 2 — Create Your First Mission

Everything in Trident begins with a Mission.

Create one:

```bash
trident mission create
```

Example:

```text
Mission Created

Mission ID:
mission-001

Status:
Ready
```

---

# Step 3 — Give the Mission an Objective

Every Mission should have a clear objective.

Example:

```text
Investigate:

example.com
```

The Mission now knows what you're trying to accomplish.

---

# Step 4 — Ask Medusa to Plan

Rather than manually selecting tools, allow Medusa to orchestrate the investigation.

```bash
trident mission execute mission-001
```

Medusa evaluates the Mission and selects the appropriate capabilities.

Example:

```text
Planning Investigation...

Selected Capabilities:

✔ DNS Lookup

✔ WHOIS

✔ Certificate Inspection

✔ HTTP Analysis

✔ Technology Detection
```

---

# Step 5 — Watch the Investigation

As capabilities execute, intelligence is added to the Mission.

Example:

```text
DNS Lookup Complete

↓

Observation Added

↓

WHOIS Complete

↓

Entity Added

↓

HTTP Analysis Complete

↓

Finding Added
```

Notice something important.

Capabilities never modify the Mission directly.

They contribute Mission Updates.

---

# Step 6 — View Mission Intelligence

Display everything the Mission has learned.

```bash
trident mission show mission-001
```

Example:

```text
Mission Summary

Target:

example.com

Observations:

12

Entities:

5

Findings:

3

Hypotheses:

1
```

The Mission is now the source of truth.

---

# Step 7 — Ask the Council

Once intelligence has been gathered, reasoning can begin.

```bash
trident council analyze mission-001
```

Example:

```text
Threat Analyst

Complete

Risk Analyst

Complete

Infrastructure Analyst

Complete
```

Council Members contribute additional Mission Updates.

They interpret intelligence.

They do not gather it.

---

# Step 8 — Generate a Report

Produce an executive briefing.

```bash
trident report executive mission-001
```

Example:

```text
Executive Brief Generated

Saved:

reports/example-executive.md
```

The report communicates Mission intelligence without modifying it.

---

# Step 9 — Review the Mission Timeline

Every investigation is replayable.

```bash
trident mission timeline mission-001
```

Example:

```text
Mission Created

↓

Observation Added

↓

Finding Added

↓

Hypothesis Added

↓

Executive Report Generated
```

You can reconstruct the investigation at any point.

---

# What Just Happened?

Let's map the workflow to Trident's architecture.

```text
Observer

↓

Mission Created

↓

Medusa Planned Investigation

↓

Serpents Gathered Intelligence

↓

Mission Updates Added

↓

Council Reasoned

↓

Reporter Generated Briefing
```

Every architectural component performed one responsibility.

---

# Why It Matters

Notice what never happened.

The Mission never:

- Called an API
- Ran a scan
- Generated a report

The Serpents never:

- Scheduled work
- Wrote reports
- Made decisions

The Council never:

- Executed tools
- Gathered intelligence

The Reporter never:

- Changed findings
- Performed analysis

This separation of responsibilities is what makes Trident scalable.

---

# Explore Further

Now that you've completed your first Mission, explore:

- Architecture Roadmap
- Mission Model
- Medusa
- Serpents
- Council
- Reporter
- Loom

Understanding these concepts will help you extend Trident effectively.

---

# Next Tutorial

Continue to:

**First Mission**

There you'll complete a full investigation while learning how every architectural component collaborates to produce trustworthy intelligence.

---

> **One Mission.**

> **Many Specialists.**

> **Shared Intelligence.**

> **Welcome to Trident.**

🔱