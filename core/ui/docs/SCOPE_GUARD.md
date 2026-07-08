# 🔱 TRIDENT SCOPEGUARD

ScopeGuard keeps Trident OS aligned with authorization, rules of engagement, and mission boundaries.

ScopeGuard is not a cage.

ScopeGuard is a targeting system.

---

# Core Rule

No scope.

No strike.

---

# Purpose

ScopeGuard determines whether a requested action is:

- authorized
- unknown
- out of scope
- unsafe
- prohibited

Its job is to warn, guide, or block depending on the action and mission context.

---

# ScopeGuard Modes

## Off

Use only for general learning, note-taking, theory, documentation, or non-operational research.

Behavior:

- no scope warnings for normal educational discussion
- no active-target guidance unless authorization is later established

## Advisory

Default mode.

Behavior:

- warn when scope is unclear
- continue with passive, educational, or non-invasive help
- require caution before active testing

## Confirm

Behavior:

- require operator confirmation before active testing guidance
- ask for scope, authorization, or rules of engagement when unclear

## Enforce

Behavior:

- block destructive, unauthorized, credential-abuse, persistence, evasion, or harmful requests
- redirect to legal alternatives, lab setup, defensive validation, or reporting guidance

---

When a request may be outside confirmed scope, display:

⚠️ ATTENTION: Target may be outside confirmed scope.
Proceed only if you have authorization.

For red-team or active testing requests:

⚠️ ATTENTION: This action requires confirmed authorization and scope.
Confirm the target, scope, and rules of engagement before proceeding.git add 

# Recommended Default

```yaml
scopeguard:
  enabled: true
  mode: advisory
  authorization_status: unknown
  engagement_type: unknown
  allowed_assets: []
  excluded_assets: []
  allowed_actions: []
  prohibited_actions: []
  notes: []