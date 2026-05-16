import pytest
from utils.config import BASE_URL
from pages.login_page import LoginPage
from test_data.users import VALID_USER, LOCKED_OUT_USER, INVALID_USER

class TestLogin:

    # TC_LOGIN_01
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(VALID_USER["username"], VALID_USER["password"])
        page.wait_for_url("**/inventory.html")
        assert "inventory.html" in page.url
        assert page.locator(".title").is_visible()
        assert page.locator(".title").inner_text() == "Products" #using .title == "Products" because .title != "Swag labs", and "Swag labs" is name of shop introduced in the login page
        assert page.locator(".inventory_item").count() >= 1
        assert not login_page.is_error_displayed()

    # TC_LOGIN_02
    def test_login_invalid_credentials(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(INVALID_USER["username"], INVALID_USER["password"])
        assert "/" in page.url and "inventory" not in page.url
        assert login_page.is_error_displayed()
        assert "Username and password do not match" in login_page.get_error_message()

    # TC_LOGIN_03
    def test_login_empty_username(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("", VALID_USER["password"])
        assert login_page.is_error_displayed()
        assert "Username is required" in login_page.get_error_message()

    # TC_LOGIN_04
    def test_login_empty_password(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(VALID_USER["username"], "")
        assert login_page.is_error_displayed()
        assert "Password is required" in login_page.get_error_message()

    # TC_LOGIN_05
    def test_locked_out_user(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(LOCKED_OUT_USER["username"], LOCKED_OUT_USER["password"])
        assert login_page.is_error_displayed()
        assert "Sorry, this user has been locked out" in login_page.get_error_message()
        assert "inventory" not in page.url

    # TC_LOGIN_06
    def test_successful_logout(self, logged_in_page):
        from pages.inventory_page import InventoryPage
        inventory = InventoryPage(logged_in_page)
        inventory.logout()
        logged_in_page.wait_for_url("**/")
        assert "inventory" not in logged_in_page.url
        assert logged_in_page.locator("#user-name").is_visible()
        assert logged_in_page.locator("#password").is_visible()
        # Verify session is cleared — navigating to inventory redirects to login
        logged_in_page.goto(f"{BASE_URL}/inventory.html")
        assert "inventory" not in logged_in_page.url or logged_in_page.locator("#login-button").is_visible()
