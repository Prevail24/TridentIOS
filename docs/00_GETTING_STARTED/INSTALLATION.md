# 💻 Installation

> **Setting up the Trident Intelligence Operating System**

---

# Requirements

Before installing Trident, ensure your development environment includes the following.

## Operating Systems

Supported:

- macOS
- Linux
- Windows (WSL2 recommended)

---

## Python

Python 3.12 or newer is required.

Verify your installation:

```bash
python --version
```

Example:

```text
Python 3.12.5
```

---

## Git

Verify Git is installed:

```bash
git --version
```

---

## Virtual Environment

Using a virtual environment is strongly recommended.

---

# Clone the Repository

```bash
git clone https://github.com/<your-org>/trident.git

cd trident
```

---

# Create a Virtual Environment

macOS / Linux

```bash
python3 -m venv .venv
```

Windows

```powershell
python -m venv .venv
```

---

# Activate the Environment

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

You should now see:

```text
(.venv)
```

before your shell prompt.

---

# Install Dependencies

```bash
pip install -U pip

pip install -r requirements.txt
```

---

# Verify Installation

Run:

```bash
python --version

pip list
```

Ensure all required packages installed successfully.

---

# Configuration

Copy the example configuration.

```bash
cp .env.example .env
```

Edit:

```text
.env
```

Example:

```text
OPENAI_API_KEY=

ANTHROPIC_API_KEY=

GEMINI_API_KEY=
```

Only configure the providers you intend to use.

---

# Optional Providers

Trident is provider-independent.

Install only the integrations you need.

Examples:

OpenAI

```bash
pip install openai
```

Anthropic

```bash
pip install anthropic
```

Google Gemini

```bash
pip install google-generativeai
```

Ollama

```bash
pip install ollama
```

---

# Verify Providers

Example:

```bash
trident providers list
```

Example output:

```text
OpenAI        Ready

Anthropic     Not Configured

Gemini        Not Installed

Ollama        Running
```

---

# Run Trident

Example:

```bash
trident
```

or

```bash
python -m trident
```

Future versions may also include:

```bash
trident ui
```

to launch the web interface.

---

# Run the Test Suite

```bash
pytest
```

Expected:

```text
======================

All tests passed

======================
```

---

# Development Installation

Install development tools.

```bash
pip install -r requirements-dev.txt
```

Recommended tools include:

- pytest
- black
- ruff
- mypy
- pre-commit

---

# Install Git Hooks

```bash
pre-commit install
```

Hooks automatically validate code before commits.

---

# Updating Trident

Pull the latest changes.

```bash
git pull
```

Update dependencies.

```bash
pip install -U -r requirements.txt
```

---

# Troubleshooting

## Python Version

Verify:

```bash
python --version
```

Python 3.12+ is required.

---

## Virtual Environment Not Active

Verify your prompt begins with:

```text
(.venv)
```

---

## Missing API Keys

If a Provider reports authentication errors:

- Verify your `.env`
- Restart your shell
- Confirm the Provider is enabled

---

## Dependency Errors

Upgrade pip.

```bash
pip install --upgrade pip
```

Reinstall dependencies.

```bash
pip install -r requirements.txt
```

---

## Provider Issues

Check provider status.

```bash
trident providers list
```

---

# Docker (Future)

Future releases will support:

```bash
docker compose up
```

to launch:

- Trident Core
- Database
- API
- Web UI
- Example Providers

---

# Next Steps

Once installation is complete:

1. Read **Quick Start**
2. Create your first Mission
3. Explore the architecture
4. Build your first Serpent

---

> **Installation should take minutes.**

> **Understanding Trident is a journey.**

🔱