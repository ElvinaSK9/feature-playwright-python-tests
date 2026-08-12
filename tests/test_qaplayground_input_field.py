import pytest
from playwright.sync_api import Browser, Page, sync_playwright, expect

# Base URL of the form page under test
BASE_URL = "https://qaplayground.com/practice/input-fields"
NAME_OF_MOVIE = "Interstellar"
APPENDED_TEXT = " Endgame"
READ_VALUE = "The Matrix"
WORD_FOR_DELETE = "Inception"

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

'''Test-Case INP004/INP005: Append text and press Tab updates result
   Expected: New text is added after the pre-filled value, not replacing it.
   Field loses focus and the blur result is recorded'''
def test_append_input(page):
    append_input = page.locator("#appendInput")
    result = page.locator("#result-s02")
    expect(append_input).to_have_value("Avengers")
    append_input.click()
    append_input.press("End")
    append_input.type(APPENDED_TEXT)
    expect(append_input).to_have_value("Avengers Endgame")
    append_input.press("Tab")
    expect(result).to_have_text("Current value: Avengers Endgame")
    expect(append_input).not_to_be_focused()

'''Test-Case INP006: Current field value can be read
   Expected: Reading returns the value currently in the field'''
def test_read_current_field(page):
    read_value = page.locator("#readValueInput")
    button = page.get_by_role("button", name="Read Value")
    result = page.locator("#result-s03")
    expect(read_value).to_have_value(READ_VALUE)
    button.click()
    expect(result).to_have_text(f"Value: {READ_VALUE}")

'''Test-Case INP007: A populated field can be cleared
   Expected: Field becomes empty after clearing'''
def test_clear_input(page):
    clear_input = page.locator("#clearInput")
    clear_button = page.get_by_role("button", name="Clear")
    result = page.locator("#result-s04")

    expect(clear_input).to_have_value(WORD_FOR_DELETE)
    expect(result).to_have_text(f"Field contains: {WORD_FOR_DELETE}")
    clear_button.click()
    expect(clear_input).to_have_value("")
    expect(result).to_have_text("Field cleared ✓")

'''Test-Case INP008: Disabled input rejects keyboard input
   Expected: Field is disabled and cannot receive text'''
def test_disabled_input_rejects_keyboard_input(page):
    disabled_input = page.locator("#disabledInput")
    result = page.locator("#result-s05")
    expect(disabled_input).to_be_visible()
    expect(disabled_input).to_be_disabled()
    expect(disabled_input).not_to_be_focused()
    expect(result).to_be_visible()
    expect(result).to_have_text("Input is disabled — typing is blocked")


'''Test-Case INP009/010: Readonly input cannot be edited and Readonly value is still readable
   Expected: Field has a value that the user cannot modify,value can be read even though it is not editable'''
def test_readonly_input_rejects_keyboard_input(page):
    readonly_input = page.locator("#readonlyInput")
    expect(readonly_input).to_have_attribute("readonly","")
    readonly_input.click()
    page.keyboard.type("New text")
    expect(readonly_input).to_have_value("Read-only content")
    result = page.locator("#result-s06")
    expect(result).to_have_text("Readonly — value can be read but not edited")





