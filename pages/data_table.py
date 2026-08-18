from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class DataTablePage(BasePage):
    PATH = "/practice/data-table"

    def __init__(self, page: Page):
        super().__init__(page)

        # DT_001: Table headers
        self.table: Locator = page.locator('[data-testid="data-table"]')
        self.headers: Locator = self.table.get_by_role("columnheader")
        # DT_002: Rows 5
        self.table_body: Locator = self.table.get_by_test_id('table-body')
        self.book_row: Locator = self.table_body.get_by_test_id('book-row')
        self.pagination: Locator = page.get_by_test_id("pagination")
        self.previous_button: Locator = self.pagination.get_by_test_id('pagination-prev')
        self.next_button: Locator = self.pagination.get_by_test_id('pagination-next')
        self.row_count: Locator = self.pagination.get_by_test_id('row-count')

    def header_by_name(self, name: str) -> Locator:
        return self.table.get_by_role("columnheader", name=name, exact=True)


    def page_button(self,number: int) -> Locator:
        return self.pagination.get_by_test_id(f'pagination-page-{number}')


