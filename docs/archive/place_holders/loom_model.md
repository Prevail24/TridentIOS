

# The Loom Model

Version: 1.0
Status: Foundational
Classification: Canonical

---

# Purpose

The Loom is the permanent knowledge layer of The Watchers Platform.

Its purpose is not to store files.

Its purpose is to preserve, connect, and evolve knowledge.

Applications create knowledge.

The Loom remembers it.

---

# The Four Fundamental Objects

The Loom is composed of four fundamental object types:

1. Thread
2. Entity
3. Relationship
4. Event

Everything in the platform is built from these concepts.

---

# 1. Thread

A Thread is a complete unit of knowledge.

Examples:

- Observation
- Technique
- Tool
- Playbook
- Discovery
- Lesson
- Theory
- Pattern
- Journal

Threads provide context.

Without Threads, knowledge becomes disconnected facts.

---

# 2. Entity

An Entity is a meaningful subject discovered within one or more Threads.

Examples:

- Person
- Username
- Email Address
- Company
- Website
- Domain
- IP Address
- City
- Country
- Cryptocurrency Wallet
- Product
- Organization

Entities are intentionally small.

They represent concepts that may appear repeatedly across many Threads.

Entities gain value through repetition and relationships.

---

# 3. Relationship

A Relationship connects knowledge.

Relationships may connect:

- Thread → Thread
- Thread → Entity
- Entity → Entity

Relationship examples:

- references
- discovered_by
- derived_from
- supports
- contradicts
- expands
- located_in
- owned_by
- uses
- mentions

Relationships transform isolated information into an intelligence network.

---

# 4. Event

An Event records that something changed.

Examples:

- Observation Created
- Observation Completed
- Technique Discovered
- Thread Woven
- Thread Updated
- Playbook Improved
- Tool Evaluated

Events allow The Loom to evolve while preserving history.

---

# Architectural Layers

The Watchers Platform consists of three conceptual layers.

Application Layer

- TridentIOS
- SignalFlare
- CertQuest
- Future applications

Knowledge Layer

- Threads
- Entities
- Relationships
- Events

Storage Layer

- Markdown
- YAML
- Git
- Future databases
- Future graph engines

Applications should depend on the Knowledge Layer rather than the Storage Layer.

---

# Design Principles

- Knowledge outlives applications.
- Relationships are first-class data.
- Context is preserved through Threads.
- Entities should be reusable.
- History should never be destroyed.
- The implementation may change; the model should remain stable.

---

# The Watchers Principle

> Build models that survive changing technology.
>
> The Loom is not a collection of documents.
>
> It is a living network of knowledge.