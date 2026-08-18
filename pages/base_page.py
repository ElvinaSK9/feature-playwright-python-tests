class BasePage:
    BASE_URL = "https://qaplayground.com"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(f"{self.BASE_URL}{self.PATH}")
