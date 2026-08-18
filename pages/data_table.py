from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class DataTablePage(BasePage):
    PATH = "/practice/data-table"

    def __init__(self, page: Page):
        super().__init__(page)

        # DT_001: Table headers
        self.table: Locator = page.locator('[data-testid="data-table"]')
        self.headers: Locator = self.table.get_by_role("columnheader")
    def header_by_name(self, name: str) -> Locator:
        return self.table.get_by_role("columnheader", name=name, exact=True)
