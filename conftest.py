import pytest
import os
from playwright.sync_api import sync_playwright
from config import Config
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.aboutus_page import ContactPage

@pytest.fixture(scope="function")
def page(context):
    """
    Overriding the default page fixture to set a specific viewport.
    The 'context' fixture is provided by pytest-playwright.
    """
    page = context.new_page()
    page.set_viewport_size({"width": 1280, "height": 720})
    yield page
    page.close()

@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)

@pytest.fixture(scope="function")
def register_page(page):
    return RegisterPage(page)

@pytest.fixture(scope="function")
def cart_page(page):
    return CartPage(page)

@pytest.fixture(scope="function")
def contact_page(page):
    return ContactPage(page)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshots on failure.
    This works perfectly with the pytest-html report.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        page = item.funcargs.get('page')
        if page:
            screenshot_path = f"reports/screenshots/{item.name}.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            page.screenshot(path=screenshot_path)