from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        # Navigation Menu Locators
        self.home_link = page.locator("a:has-text('Home')")
        self.products_link = page.locator("a[href='/products']")
        self.cart_link = page.locator("a[href='/view_cart']")
        self.contact_us_link = page.locator("a[href='/contact_us']")

        # Featured Items
        self.featured_items = page.locator(".features_items")
        self.subscription_input = page.locator("#susbscribe_email")
        self.subscribe_button = page.locator("#subscribe")
        self.success_subscribe_msg = page.locator("#success-subscribe")

    def navigate(self):
        self.page.goto("https://automationexercise.com/")



    def subscribe(self, email):
        self.subscription_input.scroll_into_view_if_needed()
        self.subscription_input.fill(email)
        self.subscribe_button.click()