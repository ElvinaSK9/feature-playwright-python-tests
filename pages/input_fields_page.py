from pages.base_page import BasePage
from playwright.sync_api import Page, Locator

class InputFieldsPage(BasePage):
    PATH = "/practice/input-fields"

    def __init__(self, page: Page):
        super().__init__(page)

        # INP001 / INP002 / INP003: Movie name input
        self.movie_input: Locator = page.locator("#movieNameInput")
        self.submit_button: Locator = page.get_by_role("button", name="Submit")
        self.movie_result: Locator = page.locator("#result-s01")
        self.movie_scenario: Locator = page.get_by_test_id("scenario-type-movie")

        # INP004 / INP005: Append input and blur result
        self.append_input: Locator = page.locator("#appendInput")
        self.append_result: Locator = page.locator("#result-s02")

        # INP006: Read current field value
        self.read_value_input: Locator = page.locator("#readValueInput")
        self.read_value_button: Locator = page.get_by_role("button", name="Read Value")
        self.read_value_result: Locator = page.locator("#result-s03")

        # INP007: Clear populated field
        self.clear_input: Locator = page.locator("#clearInput")
        self.clear_button: Locator = page.get_by_role("button", name="Clear")
        self.clear_result: Locator = page.locator("#result-s04")

        # INP008: Disabled input
        self.disabled_input: Locator = page.locator("#disabledInput")
        self.disabled_result: Locator = page.locator("#result-s05")

        # INP009 / INP010: Readonly input
        self.readonly_input: Locator = page.locator("#readonlyInput")
        self.readonly_result: Locator = page.locator("#result-s06")

    # def open(self):
    #     """Open the Input Fields practice page."""
    #     super().open(self.PATH)

    def type_movie_name(self, movie_name: str):
        """INP001: Type text into the movie name input."""
        self.movie_input.fill(movie_name)

    def submit_movie_name(self):
        """INP002: Submit the typed movie name."""
        self.submit_button.click()

    def append_text(self, text: str):
        """INP004: Append text to the pre-filled append input."""
        self.append_input.click()
        self.append_input.press("End")
        self.append_input.type(text)

    def blur_append_input(self):
        """INP005: Press Tab to move focus away from the append input."""
        self.append_input.press("Tab")

    def read_current_value(self):
        """INP006: Click the button to read the current input value."""
        self.read_value_button.click()

    def clear_populated_field(self):
        """INP007: Clear the populated input field."""
        self.clear_button.click()

    def try_typing_into_readonly_input(self, text: str):
        """INP009: Try typing into the readonly input as a user."""
        self.readonly_input.click()
        self.page.keyboard.type(text)