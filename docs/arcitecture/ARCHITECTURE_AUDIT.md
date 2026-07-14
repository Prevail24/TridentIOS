# Trident IOS Architecture Audit

## Purpose

This document tracks Trident IOS architecture decisions as we grow so we avoid duplicate systems, misplaced logic, and unnecessary rewrites.

## Current Rule

Before adding a new feature:

1. Identify the capability.
2. Ask which layer owns it.
3. Check whether a system already exists.
4. Extend before creating new files.
5. Smoke test.
6. Commit one clean milestone.

## Canonical Systems

### Mission Context

Canonical location:

- `core/kernel/mission_context.py`

Responsibility:

- Provide mission-scoped access to persisted intelligence.
- Expose observations, tool runs, ports, services, and web surfaces.
- Serve as the intelligence API for the Observer and Council.
- Prevent higher layers from reading repositories directly.

Rule:

- Current-operation reasoning should use `MissionContext`.
- Historical cross-mission reasoning may use the Loom and history services.

### Observer Console

Canonical locations:

- `cli/observer_shell.py`
- `cli/observer_dashboard.py`

Responsibility:

- Accept operator commands.
- Route commands to Mission Context and Council systems.
- Render investigation views.
- Contain no scanning, persistence, or intelligence logic.

Current commands:

- `status`
- `all`
- `ports`
- `services`
- `web`
- `observations`
- `runs`
- `hunter`
- `clear`
- `help`
- `exit`

### The Council

Canonical location:

- `core/council/`

Current files:

- `core/council/council.py`
- `core/council/assessment.py`
- `core/council/member.py`
- `core/council/registry.py`

Specialists:

- `core/serpents/sentinel.py`
- `core/serpents/hunter.py`
- `core/serpents/historian.py`
- `core/serpents/skeptic.py`
- `core/serpents/reporter.py`
- `core/serpents/oracle.py`

Responsibility:

- Interpret mission intelligence.
- Produce assessments, recommendations, comparisons, warnings, summaries, and hypotheses.
- Never create canonical facts.
- Never execute tools directly.

Rule:

- Observations are facts.
- Council assessments are interpretations.
- Recommendations are never evidence.

### Medusa

Role:

- Chief of Operations.

Responsibility:

- Coordinate strikes.
- Dispatch sensors.
- Convene Council members.
- Maintain operational flow.
- Present mission briefings.
- Return control to the Observer.

Rule:

- Medusa coordinates.
- The Council reasons.
- The Serpents explore.
- The Loom remembers.
- The Observer commands.

### Council Events

Canonical location:

- `core/events/council_event.py`

Responsibility:

- Represent immutable announcements emitted by Council members.
- Carry actor, event type, mission identity, tool-run identity, message, and structured data.

Distinction:

- `CouncilEvent` represents something announced during operations.
- `CouncilAssessment` represents the structured result of deliberate analysis.

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

### Active mission state

Review:

- `core/services/active_mission_service.py`
- `core/services/state_service.py`

Current direction:

- `StateService` is canonical for active mission runtime state.
- `ActiveMissionService` may be legacy and should be removed only after all callers migrate.

### Council presentation and orchestration

Review:

- `cli/commands/council.py`
- `core/council/council.py`
- `core/renderers/strike_renderer.py`

Decision direction:

- CLI and renderers own presentation.
- `core/council/council.py` owns orchestration.
- `core/events/council_event.py` owns the event contract.
- Presentation code must not contain Council reasoning.

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

### 2026-07-14

`MissionContext` is the canonical API for active-mission intelligence.

Hunter recommendations must use active-mission observations rather than accumulated historical host state.

`HostProfileService` remains suitable for historical host knowledge and future Historian analysis.

The Observer Shell routes commands and renders results but performs no intelligence.

Medusa is the Chief of Operations, not a Council member.

The Council never creates facts. It creates perspective from canonical observations.

Core modules must not import from `cli`.

## Next Refactor Targets

1. Confirm `StateService` as the only active-mission state system.
2. Migrate remaining `ActiveMissionService` callers.
3. Remove core-to-CLI imports.
4. Finish the `CouncilAssessment` and `CouncilMember` contracts.
5. Introduce the Council registry without replacing existing serpent logic.
6. Adapt Hunter as the first registered Council member.
7. Separate Council orchestration from Council presentation.
8. Confirm canonical graph renderer and retire unused graph renderers.
9. Confirm canonical Nmap adapter and remove the placeholder adapter.
10. Correct ToolRun start and finish lifecycle timestamps.