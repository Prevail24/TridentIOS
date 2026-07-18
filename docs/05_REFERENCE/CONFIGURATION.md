# ⚙️ Configuration

> **The canonical configuration model for the Trident Intelligence Operating System.**

---

# Purpose

Configuration controls how Trident behaves across different environments.

The configuration system is designed to be:

- Explicit
- Secure
- Versioned
- Extensible
- Environment-aware

Configuration should change platform behavior without requiring code changes.

---

# Philosophy

Configuration should define:

- **How** Trident operates.

Configuration should never define:

- Mission intelligence
- Business logic
- Investigation results

Configuration is operational.

Not investigative.

---

# Configuration Hierarchy

When multiple configuration sources exist, Trident resolves them in the following order (highest precedence first):

```text
CLI Arguments

↓

Environment Variables

↓

Mission Configuration

↓

Extension Configuration

↓

Provider Configuration

↓

System Configuration

↓

Built-in Defaults
```

Higher levels override lower levels.

---

# Configuration Sources

Trident supports multiple configuration sources:

- Environment Variables
- `.env` Files
- YAML Configuration
- JSON Configuration
- Command Line Arguments
- Future Secret Managers

---

# Default Configuration File

```text
config/

config.yaml
```

Example:

```yaml
system:

  debug: false

  log_level: INFO

providers:

  openai:

    enabled: true

  anthropic:

    enabled: false

missions:

  auto_save: true

events:

  retention_days: 90
```

---

# Environment Variables

Sensitive values should always be provided through environment variables.

Examples:

```text
OPENAI_API_KEY=

ANTHROPIC_API_KEY=

GEMINI_API_KEY=

TRIDENT_LOG_LEVEL=

TRIDENT_DEBUG=
```

Secrets should never be committed to source control.

---

# System Configuration

Controls global platform behavior.

Examples:

```yaml
system:

  debug:

  log_level:

  timezone:

  workspace:

  temp_directory:
```

---

# Mission Configuration

Mission defaults.

Example:

```yaml
missions:

  auto_save:

  auto_archive:

  default_visibility:

  default_classification:
```

---

# Provider Configuration

Each Provider owns its own configuration namespace.

Example:

```yaml
providers:

  openai:

    enabled: true

    model: gpt-5.5

    timeout: 60

    retries: 3
```

Providers should never read unrelated configuration.

---

# Extension Configuration

Extensions may define additional settings.

Example:

```yaml
extensions:

  dns_lookup:

    timeout: 10

    cache: true
```

Extensions must namespace their configuration to avoid conflicts.

---

# Logging

Logging configuration is centralized.

Example:

```yaml
logging:

  level: INFO

  format: structured

  file: logs/trident.log
```

Supported log levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

---

# Event Configuration

Controls event behavior.

Example:

```yaml
events:

  enabled: true

  retention_days: 90

  replay_enabled: true
```

---

# Security Configuration

Security-related options.

```yaml
security:

  verify_signatures: true

  require_signed_packages: true

  audit_logging: true
```

Security defaults should favor safety over convenience.

---

# AI Configuration

Shared AI defaults.

```yaml
ai:

  default_provider: openai

  temperature: 0.2

  max_tokens: 4096
```

Individual Providers may override these values.

---

# Package Configuration

Package installation behavior.

```yaml
packages:

  auto_update: false

  verify_signatures: true
```

---

# Workspace

Workspace directories.

```yaml
workspace:

  missions: missions/

  reports: reports/

  cache: cache/

  logs: logs/

  packages: packages/
```

---

# Validation

Configuration should be validated during startup.

Invalid configuration should produce clear error messages and prevent startup when critical values are missing.

---

# Best Practices

- Prefer environment variables for secrets.
- Keep configuration under version control when appropriate.
- Document every configuration option.
- Use sensible defaults.
- Validate configuration early.

---

# Anti-Patterns

Avoid:

- Hard-coded API keys
- Platform-specific paths
- Magic values
- Hidden configuration
- Duplicate settings

Configuration should remain explicit and discoverable.

---

# Summary

Trident's configuration system provides a consistent, secure, and extensible way to customize platform behavior across environments while keeping investigative logic separate from operational settings.

---

> **Configure behavior.**

> **Never configure truth.**

🔱