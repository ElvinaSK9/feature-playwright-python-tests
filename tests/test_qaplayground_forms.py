import pytest
from playwright.sync_api import Browser, Page, sync_playwright, expect

# Base URL of the form page under test
BASE_URL = "https://qaplayground.com/practice/forms"

# Test data used in positive form submission
FIRST_NAME = "FirstName"
LAST_NAME = "LastName"
PASSWORD = "123456789!A"
COUNTRY = "Australia"

# List of required fields that should be visible on the form
REQUIRED_FIELDS = [
    ("First Name", "input-first-name"),
    ("Last Name", "input-last-name"),
    ("Email", "input-email"),
    ("Phone", "input-phone"),
    ("Date of Birth", "input-dob"),
    ("Gender", "gender-group"),
    ("Country", "select-country"),
    ("City", "input-city"),
    ("Password", "input-password"),
    ("Confirm Password", "input-confirm-password"),
    ("Terms and Conditions", "checkbox-terms"),
]

# Valid text data for filling the form
VALID_TEXT_FIELDS = [
    ("First Name", "input-first-name", FIRST_NAME),
    ("Last Name", "input-last-name", LAST_NAME),
    ("Email", "input-email", "firstname@gmail.com"),
    ("Phone", "input-phone", "9876543210"),
    ("Date of Birth", "input-dob", "1990-10-10"),
    ("City", "input-city", "Sydney"),
    ("Password", "input-password", PASSWORD),
    ("Confirm Password", "input-confirm-password", PASSWORD),
]

# Expected validation errors for empty required fields
REQUIRED_FIELD_ERRORS = [
    ("error-first-name", "First name is required."),
    ("error-last-name", "Last name is required."),
    ("error-email", "Email is required."),
    ("error-phone", "Phone number is required."),
    ("error-dob", "Date of birth is required."),
    ("error-gender", "Please select a gender."),
    ("error-country", "Please select a country."),
    ("error-city", "City is required."),
    ("error-password", "Password is required."),
    ("error-confirm-password", "Please confirm your password."),
    ("error-terms", "You must accept the terms."),
]


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def form_page(browser):
    form_page = browser.new_page()
    form_page.goto(BASE_URL)
    yield form_page
    form_page.close()

# Fill all text fields with valid data.
def fill_valid_text_fields(form_page: Page):
    for field_name, test_id, value in VALID_TEXT_FIELDS:
        field = form_page.get_by_test_id(test_id)

        field.fill(value)

        expect(field,f"{field_name} should contain entered value").to_have_value(value)

# Select gender and verify that it is selected.
def select_gender(form_page: Page):
    gender_radio_button = form_page.get_by_test_id("radio-gender-male")
    gender_radio_button.check()

    expect(gender_radio_button).to_be_checked()

# Select country from the dropdown and verify selected value.
def select_country(form_page: Page, country):
    country_dropdown = form_page.get_by_test_id("select-country")
    country_dropdown.click()
    form_page.get_by_role("option", name=country).click()

    expect(country_dropdown).to_contain_text(country)

# Accept Terms & Conditions and verify checkbox state.
def accept_terms(form_page: Page):
    terms_checkbox = form_page.get_by_test_id("checkbox-terms")
    terms_checkbox.check()

    expect(terms_checkbox).to_be_checked()

# Submit the registration form.
def submit_form(form_page: Page):
    form_page.get_by_test_id("submit-form-btn").click()

# Check that text fields keep entered values after validation error.
def expect_text_fields_keep_values(form_page: Page):

    for field_name, test_id, value in VALID_TEXT_FIELDS:
        expect(form_page.get_by_test_id(test_id),f"{field_name} should keep entered value").to_have_value(value)


@pytest.mark.smoke
@pytest.mark.qaplayground
def test_form_elements_are_visible(form_page: Page):
    """TC001: Check that the form page and main form elements are visible"""
    expect(form_page).to_have_url(BASE_URL)
    expect(form_page.get_by_test_id("user-registration-form")).to_be_visible()

    # Check that all required fields are visible
    for field_name, test_id in REQUIRED_FIELDS:
        expect(
            form_page.get_by_test_id(test_id),
            f"{field_name} field should be visible"
        ).to_be_visible()

    # Check that Submit and Reset buttons are visible
    expect(form_page.get_by_test_id("submit-form-btn")).to_be_visible()
    expect(form_page.get_by_test_id("reset-form-btn")).to_be_visible()


@pytest.mark.smoke
@pytest.mark.qaplayground
def test_submit_form_with_valid_data(form_page: Page):
    """TC002: Check that user can submit the form with valid data."""

    fill_valid_text_fields(form_page)

    # Select required non-text fields
    select_gender(form_page)
    select_country(form_page, COUNTRY)

    # Accept Terms & Conditions
    accept_terms(form_page)

    # Submit the form
    submit_form(form_page)

    # Check that success message is visible
    expect(form_page.get_by_test_id("form-success-msg")).to_be_visible()

    # Check success message title
    expect(
        form_page.get_by_role("heading", name="Form Submitted Successfully!")
    ).to_be_visible()

    # Check that submitted name  and confirmation are shown correctly
    expect(form_page.get_by_test_id("submitted-name")).to_have_text( f"{FIRST_NAME} {LAST_NAME}" )
    expect(form_page.get_by_text("your details have been recorded.")).to_be_visible()


@pytest.mark.qaplayground
def test_empty_form_shows_required_field_errors(form_page: Page):
    """ TC003: Check that required field errors appear after empty submit."""

    # Submit the form without filling any fields
    submit_form(form_page)

    # Check validation messages for all required fields
    for test_id, error_text in REQUIRED_FIELD_ERRORS:
        expect(form_page.get_by_test_id(test_id)).to_have_text(error_text)

    # Check that the form was not submitted successfully
    expect(form_page.get_by_test_id("form-success-msg")).not_to_be_visible()


@pytest.mark.qaplayground
def test_entered_valid_data_is_not_cleared_after_validation_error(form_page: Page):
# TC004: Check that entered data is not cleared after validation error.

    fill_valid_text_fields(form_page)
    select_gender(form_page)
    select_country(form_page, COUNTRY)

    # Terms checkbox is intentionally not checked.
    # This should trigger validation error after submit.
    submit_form(form_page)

    # Check that the form was not submitted successfully and Terms & Conditions validation error is shown
    expect(form_page.get_by_test_id("form-success-msg")).not_to_be_visible()
    expect(form_page.get_by_test_id("error-terms")).to_be_visible()

    # Check that text fields still contain entered data
    expect_text_fields_keep_values(form_page)
    expect(form_page.get_by_test_id("radio-gender-male")).to_be_checked()
    expect(form_page.get_by_test_id("select-country")).to_contain_text(COUNTRY)