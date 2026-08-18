import pytest
from playwright.sync_api import expect
from pages.data_table import DataTablePage
ROWS = 5
TOTAL_BOOKS = 25
CURRENT_PAGE = 1
TOTAL_PAGES = TOTAL_BOOKS // ROWS

EXPECTED_HEADERS = [
    "Sr No.",
    "Book Name",
    "Book Genre",
    "Book Author",
    "Book ISBN",
    "Book Published",
    "Actions",
]
@pytest.fixture
def data_page(page: Page):
    data_page = DataTablePage(page)
    data_page.open()
    return data_page

def test_table_headers_are_present_and_correct(data_page:DataTablePage):
    """DT_001: Verify all expected table headers are present."""

    expect(data_page.headers).to_have_count(len(EXPECTED_HEADERS))
    for header in EXPECTED_HEADERS:
        expect(data_page.header_by_name(header)).to_be_visible()

def test_table_rows_are_present_and_correct(data_page:DataTablePage):
    """	Table displays exactly 5 rows on page 1 (25 total across 5 pages)"""
    expect(data_page.book_row).to_have_count(ROWS)
    expect(data_page.row_count).to_have_text(f'{TOTAL_BOOKS} books — page {CURRENT_PAGE} of {TOTAL_PAGES}')
