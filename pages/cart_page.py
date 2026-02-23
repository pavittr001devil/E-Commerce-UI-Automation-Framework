from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        # Cart Table Locators
        self.cart_rows = page.locator("tbody tr")
        self.product_names = page.locator(".cart_description h4 a")
        self.prices = page.locator(".cart_price p")
        self.quantities = page.locator(".cart_quantity button")
        self.total_prices = page.locator(".cart_total_price")
        self.delete_buttons = page.locator(".cart_quantity_delete")
        self.empty_cart_msg = page.locator("#empty_cart")


    def get_product_names(self):
        return self.product_names.all_inner_texts()

    def delete_item(self, index=0):
        self.delete_buttons.nth(index).click()

    def get_quantity(self, index=0):
        return self.quantities.nth(index).inner_text()