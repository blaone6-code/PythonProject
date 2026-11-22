from pages.base_page import BasePage
from playwright.sync_api import Page


class MainPage(BasePage):
    SEARCH_INPUT = "[data-testid='search-input']"
    SEARCH_BUTTON = "[data-testid='search-button']"

    def __init__(self, page: Page):
        super().__init__(page)

    def search_article(self, query: str):
        self.wait_and_fill(self.SEARCH_INPUT, query)
        self.wait_and_click(self.SEARCH_BUTTON)