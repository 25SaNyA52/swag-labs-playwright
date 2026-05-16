import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from test_data.users import VALID_USER
from utils.config import BROWSER, HEADLESS


@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        browser = getattr(p, BROWSER).launch(headless=HEADLESS)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser_instance):
    context = browser_instance.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def logged_in_page(page):
    login = LoginPage(page)
    login.open()
    login.login(VALID_USER["username"], VALID_USER["password"])
    page.wait_for_url("**/inventory.html")
    return page
