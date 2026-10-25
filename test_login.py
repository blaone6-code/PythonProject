from playwright.sync_api import Page
from faker import Faker

fake = Faker()
URL = "http://2.26.162.45:8080/"


def test_first(page: Page):
    page.goto(URL)
    page.get_by_test_id("nav-login").click()
    page.get_by_test_id("login-username").fill(fake.email())
    page.get_by_test_id("login-password").fill(fake.password(length=10))
    page.get_by_test_id("login-submit").click()

    expected_error = "Invalid login or password."
    error_locator = page.get_by_test_id("login-error-inline")
    error_locator.filter(has_text=expected_error).wait_for()

    actual_text = error_locator.inner_text()

    assert expected_error in actual_text, (
        f"Ошибка валидации формы авторизации!\n"
        f"Ожидаемый результат: '{expected_error}',\n"
        f"Фактический результат: '{actual_text}'"
    )