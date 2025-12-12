import allure
from playwright.sync_api import Page

@allure.feature("Login Feature")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(page: Page):

    with allure.step("Open Login Page"):
        page.goto("https://groceryapp.uniqassosiates.com/admin/login")

    with allure.step("Enter username"):
        page.fill("//input[@name='username']", "admin")

    with allure.step("Enter password"):
        page.fill("//input[@name='password']", "admin123")

    with allure.step("Click Login"):
        page.click("//button[@type='submit']")

    with allure.step("Verify Dashboard"):
        assert page.title() == "Login | 7rmart supermarket"
