#  Contributing to LLM-Powered-Robot-Agent

Thank you for your interest in contributing to **LLM-Powered-Robot-Agent**! 
This document outlines the standards and workflow to ensure high-quality, maintainable contributions.

---

## 📌 Table of Contents
- Code of Conduct
- Project Structure
- Development Setup
- Contribution Rules
- Writing Functions
- Writing Tests
- Commit Message Guidelines
- Pull Request Guidelines
- Running Tests
- Need Help?

---

## 📜 Code of Conduct

Be respectful, inclusive, and constructive.  
Harassment, discrimination, or unprofessional behavior will not be tolerated.

---

## 🗂 Project Structure

```
llm-powered-robot-agent/
│
├── functions/        # Core logic (one function per file)
├── tests/            # Pytest-based tests
├── models/           # LLM / ML models
├── simulation/       # Robot simulation code
├── scripts/          # Utility scripts
├── docs/             # Documentation
├── requirements.txt
└── CONTRIBUTING.md
```

---

## 🛠 Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/ERS-IIITJ/llm-powered-robot-agent.git
   cd llm-powered-robot-agent
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚨 Contribution Rules (IMPORTANT)

These rules are strictly enforced:

1. All core functions must be placed inside `functions/`
2. Every function must have a corresponding test file
3. Tests must use `pytest`
4. Pull requests without tests will not be merged
5. Functions must return values, not print them
6. Do not modify unrelated files
7. Keep changes small and focused

---

## ✍️ Writing Functions

### Example

```python
def listen(audio_input):
    if not audio_input:
        raise ValueError("audio_input cannot be empty")

    return {
        "text": "hello robot",
        "confidence": 0.95,
        "language": "en"
    }
```

Rules:
- One responsibility per function
- Clear input and output
- No hard-coded paths
- Avoid unnecessary side effects

---

## 🧪 Writing Tests

### Required Mapping

```
functions/listen.py  →  tests/test_listen.py
```

### Example Test

```python
import pytest
from functions.listen import listen


def test_listen_returns_expected_structure():
    result = listen("sample.wav")

    assert isinstance(result, dict)
    assert "text" in result
    assert "confidence" in result
    assert "language" in result


def test_listen_raises_error_on_empty_input():
    with pytest.raises(ValueError):
        listen("")
```

Testing Rules:
- Do NOT call test functions manually
- Every test must include at least one `assert`
- Prefer multiple focused tests
- Mock external dependencies when required

---

## 🧾 Commit Message Guidelines

This project follows **Conventional Commits**.

### Format

```
<type>: <short description>
```

### Allowed Types
- `feat` – New feature
- `fix` – Bug fix
- `test` – Adding or updating tests
- `docs` – Documentation
- `refactor` – Code restructuring
- `chore` – Maintenance tasks

### Examples

```bash
feat: add listen function
test: add tests for listen
fix: handle empty audio input
docs: update contributing guide
```

Avoid vague messages like:
- `update code`
- `fix stuff`

---

## 🔀 Pull Request Guidelines

### Before Opening a PR

Ensure:
- All tests pass (`pytest`)
- Code follows project structure
- Tests cover new functionality
- Commits follow the guidelines

### PR Title Format

```
<type>: short description
```

Example:
```
feat: implement listen function with tests
```

### PR Description Template

```md
## Description
Brief explanation of the change.

## Changes Made
- Added listen function
- Added tests

## Tests
- [x] pytest
```

---

## ▶️ Running Tests

From project root:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_listen.py
```

🚫 Do NOT run tests using:
```bash
python test_file.py
```

---

## 🆘 Need Help?

- Check existing issues
- Ask questions in issue comments
- Keep discussions technical and focused

Happy contributing! 🤖🚀