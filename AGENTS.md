# QA Automation Project Rules

## Stack

- Python
- pytest
- Playwright Sync API
- Page Object Model

## Project Structure

- `pages/` — Page Objects
- `tests/` — test files
- `conftest.py` — shared pytest fixtures
- `docs/` — test documentation
- New pages and test modules may be added as the project grows.

## Tests

- Test files must start with `test_`.
- Test functions must start with `test_`.
- Test names must clearly describe the behavior being verified.
- Each test should verify one clear scenario or behavior.
- Tests should use existing Page Objects instead of interacting with `page`
  directly when a Page Object already exists.
- Reuse existing fixtures where possible.
- Do not initialize Playwright or browsers directly inside tests.
- Avoid duplicating test setup.

## Page Objects

- UI locators belong in Page Objects.
- Reusable UI actions belong in Page Objects.
- Assertions belong in tests, not Page Objects.
- Page Objects should not contain business test expectations.
- Before adding a new locator or method, check whether an existing one can
  already be reused.
- Page Object methods should have clear names describing the action or data
  they provide.
- Add Python return type annotations to Page Object methods when possible.

## Locators

Preferred locator order:

1. `get_by_role`
2. `get_by_test_id`
3. `get_by_label`
4. `get_by_text`
5. CSS locator only when necessary

- Prefer stable semantic locators.
- Do not use fragile selectors based on DOM position.
- Do not use selectors such as `nth-child()` unless there is no stable
  alternative.
- Do not duplicate the same locator in multiple tests.
- Scope locators to a parent element when it improves reliability.

## Assertions

Use Playwright `expect()` for Locator/UI state checks:

- visibility
- text
- value
- count
- attributes
- enabled/disabled state

Use Python `assert` for non-Locator values:

- calculated values
- returned Python lists
- strings
- numbers
- business/data conditions

Example principle:

UI state -> Playwright expect
Python data -> assert

## Waiting

- Do not use `time.sleep()`.
- Do not use arbitrary `wait_for_timeout()`.
- Prefer Playwright auto-waiting and `expect()`.
- Explicit waiting should only be added when there is a clear technical reason.

## Fixtures

- Shared fixtures belong in `conftest.py`.
- Browser lifecycle should be handled by fixtures.
- Test-specific Page Object fixtures may be placed close to their tests until
  they become reusable across multiple modules.
- Promote fixtures to `conftest.py` when several test modules need them.

## Test Data

- Repeated values should be extracted into clearly named constants.
- Avoid magic numbers and unexplained strings.
- Constants should describe their meaning, not only their value.

## AI-generated changes

When generating or modifying tests:

1. Inspect existing Page Objects first.
2. Inspect related tests.
3. Inspect available fixtures.
4. Follow this document.
5. Reuse existing code before creating new abstractions.
6. Do not restructure unrelated parts of the project.
7. Do not modify production/test infrastructure unless required by the task.