from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class DataTablePage(BasePage):
    PATH = "/practice/data-table"

    def __init__(self, page: Page):
        super().__init__(page)

        self.table: Locator = page.locator('[data-testid="data-table"]')
        self.headers: Locator = self.table.get_by_role("columnheader")

        self.table_body: Locator = self.table.get_by_test_id("table-body")
        self.book_row: Locator = self.table_body.get_by_test_id("book-row")

        self.pagination: Locator = page.get_by_test_id("pagination")
        self.previous_button: Locator = self.pagination.get_by_test_id("pagination-prev")
        self.next_button: Locator = self.pagination.get_by_test_id("pagination-next")
        self.row_count: Locator = self.pagination.get_by_test_id("row-count")

        self.edit_dialog: Locator = page.locator('[data-testid="edit-book-dialog"]')
        self.search_input: Locator = page.locator('[data-testid="table-search"]')

        self.isbn_cells: Locator = self.book_row.locator('[data-col="book-isbn"]')

    def header_by_name(self, name: str) -> Locator:
        return self.table.get_by_role("columnheader", name=name, exact=True)

    def page_button(self, number: int) -> Locator:
        return self.pagination.get_by_test_id(f"pagination-page-{number}")

    def row_by_text(self, text: str) -> Locator:
        return self.book_row.filter(has_text=text)

    def book_author_cell(self, book_name: str) -> Locator:
        row = self.row_by_text(book_name)
        return row.locator('[data-col="book-author"]')

    def edit_button_for_row(self, row_text: str) -> Locator:
        row = self.row_by_text(row_text)
        return row.get_by_role("button", name="Edit")

    def search(self, text: str) -> None:
        self.search_input.fill(text)

