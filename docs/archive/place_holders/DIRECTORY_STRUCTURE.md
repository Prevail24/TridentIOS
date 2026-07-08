# TridentIOS Directory Structure

This document defines the purpose of every directory in the project.

As the project grows, new files should be placed according to these guidelines to keep the repository organized.

---

# Root

```
README.md
```

Project overview.

```
ROADMAP.md
```

Development milestones.

```
ARCHITECTURE.md
```

System design.

```
CHANGELOG.md
```

Release history.

```
LICENSE
```

Project license.

---

# skills/

Contains reusable ChatGPT Skills.

Examples:

- osint-methodology
- offensive-osint
- trident-methodology
- trident-osint-ctf

Each skill should be self-contained.

---

# playbooks/

Step-by-step investigation guides.

Examples:

- Username Investigation
- Image Geolocation
- Domain Enumeration
- Metadata Analysis
- Timeline Building
- Archive Investigation

Playbooks explain *how* to investigate.

---

# templates/

Reusable investigation documents.

Examples:

- Challenge Intake
- Evidence Log
- Pivot Log
- Timeline
- Observation Report
- Final Report

Templates reduce repetitive work.

---

# docs/

Long-form documentation.

Examples:

- Methodology
- Tool Guides
- Best Practices
- Ethics
- Investigation Techniques

---

# scripts/

Automation.

Examples:

- Metadata extractors
- Regex parsers
- Evidence generators
- Report builders
- Helper utilities

Scripts should automate repetitive investigator tasks.

---

# examples/

Completed investigations.

These serve as reference material.

Each example should include:

- Original challenge
- Investigation process
- Evidence
- Pivots
- Final solution
- Lessons learned

---

# assets/

Images, logos, diagrams, icons, branding.

---

# Future

Potential additions:

```
plugins/
```

External integrations.

```
agents/
```

Specialized investigation agents.

```
datasets/
```

Known OSINT datasets.

```
knowledge/
```

Curated references and research.

---

# Repository Rule

Every file should have a clear home.

If a new feature doesn't obviously belong somewhere, create a proposal before creating a new top-level directory.