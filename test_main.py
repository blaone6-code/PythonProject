from playwright.sync_api import Page, expect

def test_first(page: Page):
    page.goto("https://ya.ru/")

    welcome_page = page.get_by_role("search", name="Поиск в интернете")
    #expect(welcome_page).to_be_visible(5000)

    search_input= page.get_by_role("searchbox")
    search_input.click()

