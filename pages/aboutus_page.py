from playwright.sync_api import Page


class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        # Form Locators
        self.name_input = page.locator("input[data-qa='name']")
        self.email_input = page.locator("input[data-qa='email']")
        self.subject_input = page.locator("input[data-qa='subject']")
        self.message_input = page.locator("#message")
        self.upload_file = page.locator("input[name='upload_file']")
        self.submit_button = page.locator("input[data-qa='submit-button']")

        # Success Locator
        self.success_msg = page.locator(".status.alert.alert-success")

    def navigate(self):  # <--- Verify this name matches EXACTLY
        self.page.goto("https://automationexercise.com/contact_us")


    def fill_contact_form(self, name, email, subject, message, file_path=None):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_input.fill(message)

        if file_path:
            self.upload_file.set_input_files(file_path)

    def submit_form(self):
        # This page shows a Javascript 'OK' popup when you click submit.
        # Playwright handles alerts automatically, but we can accept it explicitly:
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_button.click()