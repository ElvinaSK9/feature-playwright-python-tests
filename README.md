# Playwright Python Test Automation

UI test automation project built with Python, Playwright and pytest.

The project is under active development. 
New pages, test scenarios and AI-assisted testing workflows are added incrementally.

## Coverage

Current automated coverage includes:

- ExpandTesting — login scenarios
- QA Playground — input fields
- QA Playground — data table and pagination

## Tech Stack

- Python
- Playwright Sync API
- pytest
- Allure
- Page Object Model
- Codex — AI-assisted test generation and review

## Project Structure

```text
Playwright-Python/
├── agents/
│   ├── test_generator.md
│   └── test_reviewer.md
├── docs/
│   ├── main.md
│   └── qaplayground_forms_test_cases.md
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── data_table.py
│   └── input_fields_page.py
├── reports/
│   ├── allure-results/
│   └── allure-report/
├── tests/
│   ├── test_data_table.py
│   ├── test_expandtesting_login.py
│   └── test_input_field.py
├── AGENTS.md
├── .gitignore
├── conftest.py
├── pytest.ini
└── README.md
```

## Architecture

The project follows the Page Object Model.

- `pages/` — locators and reusable UI actions
- `tests/` — test scenarios and assertions
- `conftest.py` — shared pytest fixtures
- `docs/` — test documentation and test cases
- `AGENTS.md` — project-wide automation and AI coding rules
- `agents/` — instructions used by Codex for test generation and review

Assertions are kept in tests, while reusable UI interactions and locators are kept in Page Objects.

## AI-Assisted Testing with Codex

Codex is used as an additional development and review tool.

Project conventions are defined in `AGENTS.md` so generated changes follow the same rules as manually written tests.

### Test Generator

`agents/test_generator.md`

The generator:

- reads project rules
- inspects existing tests, fixtures and Page Objects
- reuses existing functionality where possible
- inspects the UI when necessary
- proposes minimal changes
- generates Playwright/pytest tests
- runs targeted tests after implementation

### Test Reviewer

`agents/test_reviewer.md`

The reviewer checks generated changes for:

- requirement coverage
- Page Object boundaries
- locator stability
- assertion placement
- duplicated functionality
- unnecessary changes
- possible false positives
- compliance with project rules

The reviewer does not modify the code automatically.

### Workflow

```text
Test requirement
       ↓
Codex Test Generator
       ↓
Playwright / pytest implementation
       ↓
Targeted test run
       ↓
Codex Test Reviewer
       ↓
Regression test run
```

AI-generated changes are reviewed and validated with pytest before being accepted.

## Installation

Install dependencies:

```bash
pip install pytest playwright allure-pytest
```

Install Chromium:

```bash
playwright install chromium
```

## Running Tests

Run the full test suite:

```bash
pytest
```

Run a single test module:

```bash
pytest tests/test_data_table.py
```

Run a specific test:

```bash
pytest tests/test_data_table.py::test_name
```

## Allure Report

Generate test results with pytest and open the report:

```bash
allure serve reports/allure-results
```

## Codex Workflow

Start Codex from the project root:

```bash
codex
```

Codex reads the repository rules from `AGENTS.md`.

For test generation, use:

```text
Read agents/test_generator.md and follow it for this task.
```

For test review, use:

```text
Read agents/test_reviewer.md and review the current test changes.
Do not modify files.
```