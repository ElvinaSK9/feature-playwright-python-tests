
import pytest
from playwright.sync_api import Page, sync_playwright, expect

BASE_URL="https://qaplayground.com/practice/forms"
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
DATA = [
    ("First Name", "input-first-name","FirstName"),
    ("Last Name", "input-last-name","LastName"),
    ("Email", "input-email","Firstname@gmail.com"),
    ("Phone", "input-phone","9876543210"),
    ("Date of Birth", "input-dob","1990-10-10"),
    # ("Gender", "gender-group","Male"),
    # ("Country", "select-country","Australia"),
    ("City","input-city","Sydney"),
    ("Password", "input-password","123456789!A"),
    ("Confirm Password", "input-confirm-password","123456789!A"),
    # ("Terms and Conditions", "checkbox-terms",True),
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

@pytest.mark.smoke
@pytest.mark.qaplayground
def test_form_elements_are_visible(form_page: Page):
    expect(form_page).to_have_url(BASE_URL)

    expect(form_page.get_by_test_id("user-registration-form")).to_be_visible()

    for field_name, test_id in REQUIRED_FIELDS:
        expect(
            form_page.get_by_test_id(test_id),
            f"{field_name} field should be visible"
        ).to_be_visible()

    expect(form_page.get_by_test_id("submit-form-btn")).to_be_visible()
    expect(form_page.get_by_test_id("reset-form-btn")).to_be_visible()

def test_submit_form_with_valid_data(form_page: Page):
    for field_name, test_id, value in DATA:
        form_page.get_by_test_id(test_id).fill(value)
        expect(form_page.get_by_test_id(test_id)).to_have_value(value)

    form_page.get_by_test_id("radio-gender-male").check()
    expect(form_page.get_by_test_id("radio-gender-male")).to_be_checked()

    form_page.get_by_test_id("select-country").click()
    form_page.get_by_role("option",  name = "Australia").click()
    expect(form_page.get_by_test_id("select-country")).to_contain_text("Australia")

    form_page.get_by_test_id("checkbox-terms").set_checked(True)
    expect(form_page.get_by_test_id("checkbox-terms")).to_be_checked()

    form_page.get_by_test_id("submit-form-btn").click()
    expect(form_page.get_by_test_id("form-success-msg")).to_be_visible()
