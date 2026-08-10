import pytest
from playwright.sync_api import Browser, Page, sync_playwright, expect

# Base URL of the form page under test
BASE_URL = "https://qaplayground.com/practice/input-fields"
NAME_OF_MOVIE = "Interstellar"
APPENDED_TEXT = " Endgame"

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

'''Test-Case INP001: Text can be typed into an input field 
   Expected: The field holds the typed value after entry'''
def test_input_field(page):
    input_move = page.locator("#movieNameInput")
    button = page.get_by_role("button", name = "Submit")
    result = page.locator("#result-s01")

    expect(page.get_by_test_id("scenario-type-movie")).to_be_visible()
    expect(input_move).to_be_visible()
    input_move.fill(NAME_OF_MOVIE)
    expect(input_move).to_have_value(NAME_OF_MOVIE)

'''Test-Case INP002: Submitting the typed value updates the result 
   Expected: Result reflects exactly what was entered '''
def test_submit(page):
    input_move = page.locator("#movieNameInput")
    button = page.get_by_role("button", name="Submit")
    result = page.locator("#result-s01")
    input_move.fill(NAME_OF_MOVIE)
    button.click()

    expect(result).to_contain_text(NAME_OF_MOVIE)


'''Test-Case INP003: Placeholder is replaced when text is entered
   Expected: Placeholder hides once the field has a value'''

def test_placeholder_hidden_after_typing(page):
    input_move = page.locator("#movieNameInput")
    expect(input_move).to_have_attribute("placeholder","Enter a movie name…")
    input_move.fill(NAME_OF_MOVIE)
    expect(input_move).to_have_value(NAME_OF_MOVIE)

'''Test-Case INP004: Text is appended to existing content
   Expected: New text is added after the pre-filled value, not replacing it'''

def test_append_input(page):
    append_input = page.locator("#appendInput")
    result = page.locator("#result-s02")
    expect(append_input).to_have_value("Avengers")
    append_input.click()
    append_input.press("End")
    append_input.type(APPENDED_TEXT)
    append_input.press("Tab")
    expect(result).to_have_text("Current value: Avengers Endgame")



