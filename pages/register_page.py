from playwright.sync_api import Page


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        # Step 1: Initial Signup locators
        self.signup_name = page.locator("input[data-qa='signup-name']")
        self.signup_email = page.locator("input[data-qa='signup-email']")
        self.signup_button = page.locator("button[data-qa='signup-button']")

        # Step 2: Full Account Information locators
        self.password_input = page.locator("#password")
        self.first_name = page.locator("#first_name")
        self.last_name = page.locator("#last_name")
        self.address = page.locator("#address1")
        self.state = page.locator("#state")
        self.city = page.locator("#city")
        self.zipcode = page.locator("#zipcode")
        self.mobile_number = page.locator("#mobile_number")
        self.create_account_button = page.locator("button[data-qa='create-account']")

        # Success Message
        self.account_created_msg = page.locator("h2[data-qa='account-created']")

    def navigate(self):
        """Navigates to the signup/login page."""
        self.page.goto("https://automationexercise.com/login")

    def fill_initial_signup(self, name, email):
        """Fills the first step of registration."""
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()

    def fill_account_details(self, details: dict):
        """
        Fills the full registration form.
        Using .get() prevents crashes if a key is missing in certain JSON objects.
        """
        self.password_input.fill(details.get('password', 'DefaultPass123'))
        self.first_name.fill(details.get('first_name', details.get('name', 'User')))
        self.last_name.fill(details.get('last_name', 'Student'))
        self.address.fill(details.get('address', 'NH-2 GLA University'))
        self.state.fill(details.get('state', 'Uttar Pradesh'))
        self.city.fill(details.get('city', 'Mathura'))
        self.zipcode.fill(str(details.get('zipcode', '281406')))
        self.mobile_number.fill(str(details.get('mobile', '9999999999')))

        # Submit the form
        self.create_account_button.click()