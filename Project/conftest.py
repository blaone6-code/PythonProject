import pytest
from playwright.sync_api import Browser, BrowserContext, Page

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()