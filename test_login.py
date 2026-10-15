from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker()
URL = "http://2.26.162.45:8080/"

def test_first(page: Page):
    random_email = fake.email()
    random_password = fake.password(length=10)

    page.goto(URL)

    search_login = page.get_by_role("link", name="Login")
    search_login.click()

    username_field = page.get_by_test_id("login-username")
    password_field = page.get_by_test_id("login-password")
    username_field.fill(random_email)
    password_field.fill(random_password)

    page.get_by_test_id("login-submit").click()

    error_message_locator = page.get_by_test_id("login-error-inline").get_by_text("Invalid login or password.")
    error_message_locator.wait_for(state="visible", timeout=5000)

    actual_error = error_message_locator.inner_text()
    expected_error = "Invalid login or password."

    assert actual_error == expected_error, (
        f"Ошибка валидации формы авторизации!\n"
        f"Ожидали: '{expected_error}'\n"
        f"Получили: '{actual_error}'"
    )
    #Проверка авторизации
