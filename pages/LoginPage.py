from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("//input[@name='username']")
        self.password_input = page.locator("//input[@name='password']")
        self.signin_button = page.locator("//button[@type='submit']")

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_signin_button(self):
        self.signin_button.click()
