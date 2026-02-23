from playwright.sync_api import Page

def take_screenshot(page: Page, name: str):
    """Captures a screenshot and saves it to a screenshots folder."""
    page.screenshot(path=f"screenshots/{name}.png")

def scroll_to_element(page: Page, selector: str):
    """Ensures an element is in view before interacting."""
    element = page.locator(selector)
    element.scroll_into_view_if_needed()