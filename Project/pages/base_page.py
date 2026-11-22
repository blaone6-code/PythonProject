from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def wait_and_fill(self, selector: str, text: str):
        locator = self.page.locator(selector).first
        locator.wait_for(state="visible")
        locator.fill(text)

    def wait_and_click(self, selector: str):
        locator = self.page.locator(selector).first
        locator.wait_for(state="visible")
        locator.click()