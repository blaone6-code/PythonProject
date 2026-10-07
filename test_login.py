from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker()


def test_first(page: Page):
    random_email = fake.email()
    random_password = fake.password(length=10)

    page.goto("http://2.26.162.45:8080/")
    search_login = page.get_by_role("link", name="Login")
    search_login.click()
    expect(page.get_by_test_id("login-title")).to_have_text("Authorization")
    page.get_by_test_id("login-username").click()
    page.get_by_test_id("login-username").fill(random_email)
    page.get_by_test_id("login-password").click()
    page.get_by_test_id("login-password").fill(random_password)
    page.get_by_test_id("login-submit").click()

    error_message = page.get_by_test_id("login-error-inline")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Invalid login or password.")
    #Проверка авторизации
