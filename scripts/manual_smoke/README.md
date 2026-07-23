# Trident Manual Smoke Scripts

These files are operator-run diagnostic workflows.

They are not automated pytest tests and may intentionally create or
modify Trident operational data, including missions, cases, entities,
observations, relationships, evidence, and runtime state.

Run a script from the repository root:

    PYTHONPATH="$PWD" python scripts/manual_smoke/<script>.py

Do not execute these scripts through pytest.

Automated tests belong under `tests/` and run inside isolated temporary
storage.
