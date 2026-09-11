import pytest
from playwright.sync_api import Page, expect
from pages.data_table import DataTablePage

ROWS = 5
TOTAL_BOOKS = 25
CURRENT_PAGE = 1
SECOND_PAGE = 2
TOTAL_PAGES = TOTAL_BOOKS // ROWS
CLEAN_CODE = "Clean Code"
GEORGE_ORWELL = "George Orwell"
BOOK_1984 = "1984"
TEXT = "1 book"
PAGE_2_SERIAL_NUMBERS = ["6", "7", "8", "9", "10"]

EXPECTED_HEADERS = [
    "Sr No.",
    "Book Name",
    "Book Genre",
    "Book Author",
    "Book ISBN",
    "Book Published",
    "Actions",
]

GENRE_LIST = [
    "All",
    "Technology",
    "Fantasy",
    "Science Fiction",
    "Dystopian",
    "Fiction",
    "Non-Fiction",
]

@pytest.fixture
def data_page(page: Page):
    data_page = DataTablePage(page)
    data_page.open()
    return data_page


def test_table_headers_are_present_and_correct(data_page: DataTablePage):
    """DT_001: Verify all expected table headers are present."""

    expect(data_page.headers).to_have_count(len(EXPECTED_HEADERS))
    for header in EXPECTED_HEADERS:
        expect(data_page.header_by_name(header)).to_be_visible()


def test_table_rows_are_present_and_correct(data_page: DataTablePage):
    """DT_002: Table displays exactly 5 rows on page 1 (25 total across 5 pages)"""

    expect(data_page.book_row).to_have_count(ROWS)
    expect(data_page.row_count).to_have_text(
        f"{TOTAL_BOOKS} books — page {CURRENT_PAGE} of {TOTAL_PAGES}"
    )


def test_table_rows_contain_name(data_page: DataTablePage):
    """DT_003 — Find the row containing Clean Code and verify its data
    Expected: The row containing Clean Code is visible and contains the author Robert C. Martin.'"""

    expect(data_page.row_by_text(CLEAN_CODE)).to_be_visible()
    expect(data_page.book_author_cell(CLEAN_CODE)).to_have_text("Robert C. Martin")


def test_find_and_click(data_page: DataTablePage):
    """DT_004 — Find the row for author 'George Orwell' and click its Edit button
    Expected: Edit dialog is displayed for the George Orwell row"""

    data_page.search(GEORGE_ORWELL)
    expect(data_page.row_by_text(GEORGE_ORWELL)).to_be_visible()

    edit_button = data_page.edit_button_for_row(GEORGE_ORWELL)
    expect(edit_button).to_be_visible()
    edit_button.click()

    expect(data_page.edit_dialog).to_be_visible()


def test_search_by_book_name(data_page: DataTablePage):
    """DT_007 —Searching by a book name filters the visible rows
    Expected: Only rows matching the search term remain visible"""

    expect(data_page.search_input).to_be_visible()
    data_page.search(BOOK_1984)

    expect(data_page.search_input).to_have_value(BOOK_1984)
    expect(data_page.book_row).to_have_count(1)
    expect(data_page.book_author_cell(BOOK_1984)).to_have_text(GEORGE_ORWELL)


def test_table_not_empty(data_page: DataTablePage):
    """DT_005 —Table is not empty after initial page load
    Expected: tbody contains at least one visible row"""

    expect(data_page.table_body).to_be_visible()
    assert data_page.book_row.count() > 0
    expect(data_page.book_row.first).to_be_visible()

def test_value_in_the_columnISBN(data_page: DataTablePage):
    """DT_006 —All values in the Book ISBN column start with 'ISBN-'
    Expected: Every ISBN cell begins with the prefix 'ISBN-'"""
    checked_isbn_count = 0
    for page_number in range(1,TOTAL_PAGES+1):
        if page_number != 1:
            data_page.page_button(page_number).click()

        isbn_values = data_page.isbn_cells.all_text_contents()

        for isbn_value in isbn_values:
            clean_isbn = isbn_value.strip()

            assert clean_isbn.startswith("ISBN-")

            checked_isbn_count += 1

    assert checked_isbn_count == TOTAL_BOOKS

def test_genre_filter(data_page: DataTablePage):
    """DT_008 — Genre filter reduces visible rows to the selected genre only
    Expected: Only books in the chosen genre are shown after filtering"""
    selected_genre = GENRE_LIST[2]
    data_page.filter_by_genre(selected_genre)
    genres = data_page.get_book_genres()
    assert len(genres) > 0

    for genre_value in genres:
        assert genre_value == selected_genre

def test_attribute(data_page: DataTablePage):
    """DT010 — Row can be located by its data-book-id attribute
    Expected: Row with data-book-id='book-004' contains 'The Hobbit'"""
    expect(data_page.attribute_row_book).to_be_visible()
    expect(data_page.book_name_from_attribute_row()).to_have_text("The Hobbit")

def test_clearing(data_page: DataTablePage):
    """DT011 — Clearing the search input restores all rows and resets pagination
    Expected: After clearing search, page 1 shows 5 rows and pagination shows 5 pages"""
    expect(data_page.table_body).to_be_visible()
    expect(data_page.book_row).to_have_count(ROWS)

    data_page.search("Pattern")

    expect(data_page.search_input).to_have_value("Pattern")
    expect(data_page.book_row).to_have_count(1)
    expect(data_page.row_by_text("Design Patterns")).to_be_visible()
    expect(data_page.row_counts).to_have_text(TEXT)
    data_page.clear_search()
    expect(data_page.book_row).to_have_count(ROWS)
    expect(data_page.row_count).to_have_text(
        f"{TOTAL_BOOKS} books — page {CURRENT_PAGE} of {TOTAL_PAGES}"
    )

def test_clicking_page_2_loads_serial_numbers_6_to_10(data_page: DataTablePage):
    """DT013 — Clicking page 2 loads the next set of rows
   Expected: Page 2 shows rows 6-10 and the active page button is highlighted"""

    data_page.page_button(SECOND_PAGE).click()

    expect(data_page.book_row).to_have_count(ROWS)
    expect(data_page.serial_number_cells).to_have_text(PAGE_2_SERIAL_NUMBERS)
    expect(data_page.page_button(SECOND_PAGE)).to_have_attribute("aria-current", "page")
    expect(data_page.row_count).to_have_text(f"{TOTAL_BOOKS} books — page {SECOND_PAGE} of {TOTAL_PAGES}")

def test_navigation_one_by_one(data_page: DataTablePage):
    """DT014 - Clicking Next navigates to the following page
    Expected: Next button advances pagination by one page"""

    expect(data_page.page_button(CURRENT_PAGE)).to_have_attribute("aria-current", "page")
    expect(data_page.row_count).to_have_text(
        f"{TOTAL_BOOKS} books — page {CURRENT_PAGE} of {TOTAL_PAGES}"
    )
    expect(data_page.next_button).to_be_enabled()
    data_page.next_button.click()

    expect(data_page.previous_button).to_be_enabled()
    expect(data_page.page_button(SECOND_PAGE)).to_have_attribute("aria-current", "page")
    expect(data_page.row_count).to_have_text(f"{TOTAL_BOOKS} books — page {SECOND_PAGE} of {TOTAL_PAGES}")

def test_previous_button_state(data_page: DataTablePage):
    """DT015 - Previous button is disabled on page 1 and enabled on page 2+
   Expected: Prev is disabled on first page, enabled on all others"""

    expect(data_page.page_button(CURRENT_PAGE)).to_have_attribute("aria-current", "page")
    expect(data_page.previous_button).to_be_disabled()

    data_page.page_button(SECOND_PAGE).click()

    expect(data_page.previous_button).to_be_enabled()
    expect(data_page.next_button).to_be_enabled()
    expect(data_page.page_button(SECOND_PAGE)).to_have_attribute("aria-current", "page")
