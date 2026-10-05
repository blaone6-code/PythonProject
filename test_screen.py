from datetime import datetime
import time
from playwright.sync_api import Page, expect

def test_wikipedia_search_screencast(page: Page):
    # 1. Настраиваем HD-разрешение окна для качественной записи
    page.set_viewport_size({"width": 1280, "height": 720})

    # 1. Генерируем уникальный хвост на основе текущего времени: ГГГГММДД_ЧЧММСС
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_filename = f"wikipedia_search_{timestamp}.webm"

    # 2. Включаем запись экрана
    page.screencast.start(path=video_filename)

    # 3. Переходим на главную страницу русской Википедии
    page.goto("https://ru.wikipedia.org/")

    # Проверяем, что блок приветствия отобразился
    welcome_title = page.get_by_role("heading", name="Добро пожаловать в Википедию")
    expect(welcome_title).to_be_visible(timeout=5000)

    # 4. Активируем поисковую строку
    search_input = page.get_by_role("searchbox")
    search_input.click()

    # Плавный ввод текста (задержка 100мс имитирует действия реального пользователя)
    search_input.press_sequentially("the doors", delay=100)

    # 5. Проверяем интерактивность: при вводе должен появиться контейнер с подсказками
    # Ищем выпадающее меню результатов поиска по его системному классу или роли
    suggestions_dropdown = page.locator(".cdx-typeahead-search__menu, .suggestions-dropdown").first

    # Ожидаем появление меню на экране (подтверждает, что сайт отреагировал на ввод)
    expect(suggestions_dropdown).to_be_visible(timeout=5000)

    # 6. Даем скринкасту записать открывшееся меню подсказок (2 секунды)
    time.sleep(2)

    # 7. Завершаем сессию записи и сохраняем видеоролик
    page.screencast.stop()
