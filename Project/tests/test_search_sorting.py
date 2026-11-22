import pytest
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from utils.config_reader import ConfigReader

config = ConfigReader()
BASE_URL = config.get("environment.url")
TEST_CASES = config.get("test_data.search_cases")


@pytest.mark.parametrize("case", TEST_CASES)
def test_article_price_sorting(page, case):
    name = case["name"]
    n = case["n"]
    filter_value = case["filter_value"]

    main_page = MainPage(page)
    main_page.goto(BASE_URL)

    main_page.search_article(name)

    results_page = SearchResultsPage(page)

    results_page.set_sort_filter(filter_value)

    prices = results_page.get_first_n_prices(n)

    assert len(prices) > 0, f"Список цен пуст после поиска '{name}'"

    if filter_value == "price_asc":
        assert prices == sorted(prices), (
            f"Цены не отсортированы по возрастанию!\n"
            f"Ожидалось: {sorted(prices)}\n"
            f"Получено:   {prices}"
        )
    elif filter_value == "price_desc":
        assert prices == sorted(prices, reverse=True), (
            f"Цены не отсортированы по убыванию!\n"
            f"Ожидалось: {sorted(prices, reverse=True)}\n"
            f"Получено:   {prices}"
        )