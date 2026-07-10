TRIDENT IOS
Version 0.3 Architecture

               User
                 │
                 ▼
             CLI Router
                 │
        ┌────────┴────────┐
        ▼                 ▼
     Sensors         Commands
        │
        ▼
     Adapters
        │
        ▼
     Parsers
        │
        ▼
 Native Observations
        │
   ┌────┴─────────┐
   ▼              ▼
Observation   The Loom
 Engine        (Memory)
   │              │
   ▼              ▼
Repositories  Knowledge
                  │
                  ▼
          Intelligence Engine
                  │
                  ▼
             Renderers/UI

# Trident IOS Architecture Bible

## Prime Directive

Trident IOS is an intelligence operating system.

Every capability must support one or more of the core actions:

- Observe
- Remember
- Reason

## Development Doctrine

Before writing code:

1. Identify the capability.
2. Identify the owning layer.
3. Check for existing systems.
4. Extend before creating new components.
5. Smoke test.
6. Commit one clean milestone.

## Layer Responsibilities

### CLI

Routes commands only.

Must not:
- Parse tool output
- Build graphs
- Save domain objects directly
- Contain business logic

### Sensors

Start collection.

Owns:
- Sensor identity
- Sensor metadata
- Sensor execution entry point

### Adapters

Run tools and bridge external output into Trident.

Owns:
- External command execution
- Evidence file creation
- Native parser invocation
- ToolRun creation

### Parsers

Convert raw data into structured objects.

Owns:
- XML parsing
- JSON parsing
- Text parsing
- Native observation construction

### Models

Define domain objects.

Owns:
- Mission
- Observation
- Evidence
- Entity
- Relationship
- ToolRun

### Services

Orchestrate business logic.

Owns:
- Creating missions
- Emitting observations
- Resolving entities
- Building reports
- Managing timelines

### Repositories

Persist and retrieve data.

Owns:
- File storage
- JSON storage
- Markdown storage
- Future database storage

### The Loom

Canonical location:

`core/graph/`

Owns:
- Knowledge nodes
- Knowledge edges
- Graph building
- Loom persistence
- Connected memory

### Renderers

Display information.

Must not:
- Save data
- Parse data
- Mutate domain objects
- Run tools

## Architecture Rule

If a feature feels hard to place, stop coding and audit the architecture first.

## Canonical Flow

```text
CLI
 ↓
Sensor
 ↓
Adapter
 ↓
Parser
 ↓
Native Observations
 ├── Observation Engine
 └── The Loom

 Current Canonical Decisions

* core/graph/ is the canonical Loom system.
* core/adapters/nmap_adapter.py is the canonical Nmap adapter.
* ToolRun.observations stores observation IDs, not structured observation objects.
* Graph construction belongs where native observations still exist.
* CLI should remain thin.