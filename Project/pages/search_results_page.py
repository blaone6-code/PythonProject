import re
from pages.base_page import BasePage
from playwright.sync_api import Page


class SearchResultsPage(BasePage):

    SORT_FILTER = "[data-testid='filter-sort']"

    ARTICLE_PRICE = "[data-testid^='search-result-price-']"

    def __init__(self, page: Page):
        super().__init__(page)

    def set_sort_filter(self, filter_value: str):
        locator = self.page.locator(self.SORT_FILTER).first
        locator.wait_for(state="visible")
        locator.select_option(value=filter_value)
        self.page.wait_for_load_state("networkidle")

    def get_first_n_prices(self, n: int) -> list[float]:
        prices_locator = self.page.locator(self.ARTICLE_PRICE)

        prices_locator.first.wait_for(state="visible")

        prices = []
        count = min(n, prices_locator.count())

        for i in range(count):
            # Получаем текст i-го элемента цены
            text = prices_locator.nth(i).inner_text().strip()

            clean_text = re.sub(r'[^\d.]', '', text.replace(',', '.'))

            if clean_text:
                prices.append(float(clean_text))

        return prices