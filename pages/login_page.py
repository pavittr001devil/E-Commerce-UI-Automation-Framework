from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Login Form Locators
        self.email_input = page.locator("input[data-qa='login-email']")
        self.password_input = page.locator("input[data-qa='login-password']")
        self.login_button = page.locator("button[data-qa='login-button']")

        # Post-Login Locators
        self.logout_link = page.locator("a[href='/logout']")
        self.logged_in_as = page.locator("li:has-text('Logged in as')")
        self.error_message = page.locator("p:has-text('Your email or password is incorrect!')")

    def navigate(self):
        self.page.goto("https://automationexercise.com/")


    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()