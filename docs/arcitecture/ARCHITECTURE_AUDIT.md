# Trident IOS Architecture Audit

## Canonical Systems

## Possible Duplicates

## Deprecated / Legacy Candidates

## Decisions

## Next Refactor Targets

# Trident IOS Architecture Audit

## Purpose

This document tracks Trident IOS architecture decisions so we avoid duplicate systems, misplaced logic, and unnecessary rewrites.

## Current Rule

Before adding a new feature:

1. Identify the capability.
2. Ask which layer owns it.
3. Check whether a system already exists.
4. Extend before creating new files.
5. Smoke test.
6. Commit one clean milestone.

## Canonical Systems

### CLI

Location:

- `cli/main.py`
- `cli/commands/`

Responsibility:

- Route commands.
- Call services/sensors.
- Avoid business logic.

### Sensors

Location:

- `core/sensors/`

Responsibility:

- Represent sensor interfaces.
- Trigger collection.

### Adapters

Location:

- `core/adapters/`

Responsibility:

- Run tools.
- Parse native output.
- Produce observations/evidence/tool runs.

Canonical Nmap adapter:

- `core/adapters/nmap_adapter.py`

Possible legacy/placeholder:

- `core/sensors/nmap/adapter.py`

### Parsers

Location:

- `core/parsers/`

Responsibility:

- Convert raw files/output into structured domain objects.

### Models

Location:

- `core/models/`

Responsibility:

- Represent persisted/core domain objects.

### Services

Location:

- `core/services/`

Responsibility:

- Orchestrate business logic.

### Repositories

Location:

- `core/repositories/`
- `core/graph/loom_repository.py`

Responsibility:

- Save/load persistent state.

### The Loom / Knowledge Graph

Canonical location:

- `core/graph/`

Canonical files:

- `knowledge_graph.py`
- `node.py`
- `edge.py`
- `graph_builder.py`
- `loom_repository.py`
- `entity_types.py`
- `relationship_types.py`

Responsibility:

- Store connected knowledge.
- Represent nodes and relationships.
- Persist/load the Loom.

### Renderers

Location:

- `core/renderers/`

Responsibility:

- Display data only.
- No business logic.

Canonical Loom renderer:

- `core/renderers/loom_renderer.py`

## Possible Duplicates

### Graph-related

Review later:

- `core/models/graph.py`
- `core/models/graph_edge.py`
- `core/models/entity_graph.py`
- `core/renderers/graph_renderer.py`
- `core/renderers/knowledge_graph_renderer.py`
- `core/renderers/entity_graph_renderer.py`

Decision pending:

- Keep `core/graph/` as canonical Loom system.
- Mark older graph models/renderers as legacy if unused.

### Nmap adapter locations

Review:

- `core/adapters/nmap_adapter.py`
- `core/sensors/nmap/adapter.py`

Decision pending:

- `core/adapters/nmap_adapter.py` appears canonical.
- `core/sensors/nmap/adapter.py` may be placeholder/legacy.

### Observation manager

Review:

- `core/observation_manager.py`
- `core/services/observation_manager.py`

Decision pending.

## Decisions

### 2026-07-09

The Loom / Knowledge Graph should live in `core/graph/`.

The CLI should not build graphs.

Nmap graph construction belongs near native Nmap observation creation, not inside `ToolRun`.

`ToolRun.observations` stores observation IDs, not structured observation objects.

## Next Refactor Targets

1. Clean `__pycache__` files from Git if tracked.
2. Confirm canonical Nmap adapter.
3. Confirm canonical graph renderer.
4. Identify legacy graph models.
5. Decide whether `LoomRepository` stays in `core/graph/` or moves to `core/repositories/`.
6. Add architecture rule to README or docs.