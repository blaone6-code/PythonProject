from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker()
URL = "http://2.26.162.45:8080/"

def test_first(page: Page):
    random_email = fake.email()
    random_password = fake.password(length=10)

    page.goto(URL)

    search_login = page.get_by_test_id("nav-login")
    search_login.click()

    username_field = page.get_by_test_id("login-username")
    password_field = page.get_by_test_id("login-password")
    username_field.fill(random_email)
    password_field.fill(random_password)

    page.get_by_test_id("login-submit").click()

    error_locator = page.get_by_test_id("login-error-inline")
    expected_error = "Invalid login or password."

    error_locator.filter(has_text=expected_error).wait_for()

    actual_text = error_locator.text_content()

    assert expected_error in actual_text, (
        f"Ошибка валидации формы авторизации! "
        f"Ожидаем, что текст содержит: '{expected_error}', "
        f"но фактический текст: '{actual_text}'"
    )