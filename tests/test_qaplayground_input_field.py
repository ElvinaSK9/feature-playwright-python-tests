import pytest
from playwright.sync_api import expect
from pages.input_fields_page import InputFieldsPage

NAME_OF_MOVIE = "Interstellar"
MOVIE_PLACEHOLDER = "Enter a movie name…"

INITIAL_APPEND_VALUE = "Avengers"
APPENDED_TEXT = " Endgame"
EXPECTED_APPEND_VALUE = INITIAL_APPEND_VALUE + APPENDED_TEXT

READ_VALUE = "The Matrix"
WORD_FOR_DELETE = "Inception"
READONLY_VALUE = "Read-only content"

@pytest.fixture
def input_fields_page(page):
    input_fields_page = InputFieldsPage(page)
    input_fields_page.open()
    return input_fields_page

def test_input_field(input_fields_page):
    """Test-Case INP001: Text can be typed into an input field
    Expected: The field holds the typed value after entry"""

    expect(input_fields_page.movie_scenario).to_be_visible()
    expect(input_fields_page.movie_input).to_be_visible()

    input_fields_page.movie_input.fill(NAME_OF_MOVIE)
    expect(input_fields_page.movie_input).to_have_value(NAME_OF_MOVIE)

def test_submit(input_fields_page):
    """Test-Case INP002: Submitting the typed value updates the result
    Expected: Result reflects exactly what was entered"""

    input_fields_page.movie_input.fill(NAME_OF_MOVIE)
    input_fields_page.submit_movie_name()
    expect(input_fields_page.movie_result).to_contain_text(NAME_OF_MOVIE)

def test_placeholder_hidden_after_typing(input_fields_page):
    """Test-Case INP003: Placeholder is replaced when text is entered
    Expected: Placeholder hides once the field has a value"""

    expect(input_fields_page.movie_input).to_have_attribute("placeholder", MOVIE_PLACEHOLDER)
    input_fields_page.type_movie_name(NAME_OF_MOVIE)
    expect(input_fields_page.movie_input).to_have_value(NAME_OF_MOVIE)

def test_append_input(input_fields_page):
    """Test-Case INP004/INP005: Append text and press Tab updates result
    Expected: New text is added after the pre-filled value, not replacing it.
    Field loses focus and the blur result is recorded"""

    expect(input_fields_page.append_input).to_have_value(INITIAL_APPEND_VALUE)
    input_fields_page.append_text(APPENDED_TEXT)
    expect(input_fields_page.append_input).to_have_value(EXPECTED_APPEND_VALUE)
    input_fields_page.blur_append_input()
    expect(input_fields_page.append_result).to_have_text( f"Current value: {EXPECTED_APPEND_VALUE}")
    expect(input_fields_page.append_input).not_to_be_focused()

def test_read_current_field(input_fields_page):
    """Test-Case INP006: Current field value can be read
    Expected: Reading returns the value currently in the field"""

    expect(input_fields_page.read_value_input).to_have_value(READ_VALUE)
    input_fields_page.read_current_value()
    expect(input_fields_page.read_value_result).to_have_text(f"Value: {READ_VALUE}")

def test_clear_input(input_fields_page):
    """Test-Case INP007: A populated field can be cleared
    Expected: Field becomes empty after clearing"""
    expect(input_fields_page.clear_input).to_have_value(WORD_FOR_DELETE)
    expect(input_fields_page.clear_result).to_have_text(f"Field contains: {WORD_FOR_DELETE}")

    input_fields_page.clear_populated_field()

    expect(input_fields_page.clear_input).to_have_value("")
    expect(input_fields_page.clear_result).to_have_text("Field cleared ✓")

def test_disabled_input_rejects_keyboard_input(input_fields_page):
    """Test-Case INP008: Disabled input rejects keyboard input
    Expected: Field is disabled and cannot receive text"""
    expect(input_fields_page.disabled_input).to_be_visible()
    expect(input_fields_page.disabled_input).to_be_disabled()
    expect(input_fields_page.disabled_input).not_to_be_focused()

    expect(input_fields_page.disabled_result).to_be_visible()
    expect(input_fields_page.disabled_result).to_have_text("Input is disabled — typing is blocked")

def test_readonly_input_rejects_keyboard_input(input_fields_page):
    """Test-Case INP009/010: Readonly input cannot be edited and Readonly value is still readable
    Expected: Field has a value that the user cannot modify,value can be read even though it is not editable"""
    expect(input_fields_page.readonly_input).to_have_attribute("readonly", "")
    expect(input_fields_page.readonly_input).to_have_value(READONLY_VALUE)

    input_fields_page.try_typing_into_readonly_input("New text")

    expect(input_fields_page.readonly_input).to_have_value(READONLY_VALUE)
    expect(input_fields_page.readonly_result).to_have_text("Readonly — value can be read but not edited")



