
import pytest
from playwright.sync_api import Page, expect

USERNAME = "practice"
PASSWORD = "SuperSecretPassword!"
BASE_URL = "https://practice.expandtesting.com/login"

@pytest.fixture(scope="function")
def login_page(browser):
    login_page = browser.new_page()
    login_page.goto(BASE_URL)
    yield login_page
    login_page.close()

def login(username,password,login_page:Page):
    input_username = login_page.get_by_label("username")
    input_password = login_page.get_by_label("password")
    input_username.fill(username)
    input_password.fill(password)
    login_btn = login_page.get_by_role('button', name='Login')
    login_btn.click()

def test_successful_login(login_page:Page):
    username="practice"
    password ="SuperSecretPassword!"
    login(username,password,login_page)

    expect(login_page).to_have_url("https://practice.expandtesting.com/secure")
    expect(login_page.get_by_text("You logged into a secure area!")).to_be_visible()
    expect(login_page.get_by_role('link', name = 'Logout')).to_be_visible()

def test_login_using_enter_key(login_page:Page):
    input_username = login_page.get_by_label("username")
    input_password = login_page.get_by_label("password")
    input_username.fill(USERNAME)
    input_password.fill(PASSWORD)
    input_password.press("Enter")

    expect(login_page).to_have_url("https://practice.expandtesting.com/secure")
    expect(login_page.get_by_text("You logged into a secure area!")).to_be_visible()

def test_tab_navigation_order(login_page:Page):
    input_username= login_page.get_by_label("username")
    input_password = login_page.get_by_label("password")
    input_username.focus()

    expect(input_username).to_be_focused()

    input_username.press("Tab")

    expect(input_password).to_be_focused()

    input_password.press("Tab")

    expect(login_page.get_by_role('button', name='Login')).to_be_focused()

def test_successful_login_after_failed_attempt(login_page:Page):
    username="practice_test"
    password ="SuperSecretPassword!"
    login(username,password,login_page)

    expect(login_page).to_have_url("https://practice.expandtesting.com/login")
    expect(login_page.get_by_text("Your username is invalid!")).to_be_visible()

    login(USERNAME,PASSWORD,login_page)

    expect(login_page).to_have_url("https://practice.expandtesting.com/secure")
    expect(login_page.get_by_text("You logged into a secure area!")).to_be_visible()


@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        pytest.param("practice_test",PASSWORD,"Your username is invalid!",
            id="invalid_username",
        ),
        pytest.param(USERNAME,"SuperSecretPassword_test!","Your password is invalid!",
            id="invalid_password",
        ),
        pytest.param("","", "Your username is invalid!",
            id="empty_credentials",
        ),
        pytest.param("",PASSWORD,"Your username is invalid!",
            id="empty_username",
        ),
        pytest.param(USERNAME,"","Your password is invalid!",
            id="empty_password",
        ),
        pytest.param("   ", PASSWORD, "Your username is invalid!",
            id="username_only_whitespace",
        ),
        pytest.param(USERNAME, "    ", "Your password is invalid!",
            id="password_only_whitespace",
        ),
        pytest.param(" practice ", PASSWORD,"Your username is invalid!",
            id="username_with_spaces",
        ),
        pytest.param("Practice",PASSWORD,"Your username is invalid!",
            id="username_wrong_case",
        ),
        pytest.param(USERNAME,"supersecretpassword!","Your password is invalid!",
            id="password_wrong_case",
        ),
        pytest.param("longUsernamepracticepracticepracticepracticepracticepracticepractice", PASSWORD,"Your username is invalid!",
            id="long_username",
        ),
        pytest.param("practice@#$%^&*(){}:<>?±±§{][].,",PASSWORD,"Your username is invalid!",
            id="username_special_characters",
        ),
    ]
)
def test_negative_scenarios(username,password,expected_message,login_page:Page):
    login(username,password,login_page)
    expect(login_page.get_by_text(expected_message)).to_be_visible()
    expect(login_page).to_have_url("https://practice.expandtesting.com/login")

