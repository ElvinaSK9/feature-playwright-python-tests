import pytest
from playwright.sync_api import Browser, Page, sync_playwright, expect

# Base URL of the form page under test
BASE_URL = "https://qaplayground.com/practice/input-fields"
NAME_OF_MOVIE = "Interstellar"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()

# Test-Case INP001: Text can be typed into an input field
# Expected: The field holds the typed value after entry
def test_input_field(page):
    input_move = page.locator("#movieNameInput")
    button = page.get_by_role("button", name = "Submit")
    result = page.locator("#result-s01")

    expect(page.get_by_test_id("scenario-type-movie")).to_be_visible()
    expect(input_move).to_be_visible()
    input_move.fill(NAME_OF_MOVIE)
    expect(input_move).to_have_value(NAME_OF_MOVIE)

# Test-Case INP002: Submitting the typed value updates the result
# Expected: Result reflects exactly what was entered
def test_submit(page):
    input_move = page.locator("#movieNameInput")
    button = page.get_by_role("button", name="Submit")
    result = page.locator("#result-s01")

    input_move.fill(NAME_OF_MOVIE)
    button.click()

    expect(result).to_contain_text(NAME_OF_MOVIE)
