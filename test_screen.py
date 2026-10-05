from datetime import datetime
import time
from playwright.sync_api import Page, expect

def test_wikipedia_search_screencast(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_filename = f"wikipedia_search_{timestamp}.webm"

    page.screencast.start(path=video_filename)

    page.goto("https://ru.wikipedia.org/")

    welcome_title = page.get_by_role("heading", name="Добро пожаловать в Википедию")
    expect(welcome_title).to_be_visible(timeout=5000)

    search_input = page.get_by_role("searchbox")
    search_input.click()

    search_input.press_sequentially("the doors", delay=100)

    suggestions_dropdown = page.locator(".cdx-typeahead-search__menu, .suggestions-dropdown").first

    expect(suggestions_dropdown).to_be_visible(timeout=5000)

    time.sleep(2)

    page.screencast.stop()
