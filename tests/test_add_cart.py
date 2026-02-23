import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from config import Config

def test_add_to_cart_flow(page):
    home = HomePage(page)
    cart = CartPage(page)

    # 1. Navigate to Home
    home.navigate()
    assert home.featured_items.is_visible()

    # 2. Add first product to cart
    # Note: We use a direct locator here if a dedicated ProductPage isn't built yet
    page.locator(".add-to-cart").first.click()
    page.locator("u:has-text('View Cart')").click()

    # 3. Verify Cart
    assert len(cart.get_product_names()) > 0
    assert cart.get_quantity(0) == "1"