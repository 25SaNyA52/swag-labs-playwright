import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.login_page import LoginPage
from test_data.users import VALID_USER
from utils.config import BASE_URL
from utils.helpers import parse_price


class TestCheckout:

    def _add_item_and_go_to_checkout(self, page):
        """Helper: add Sauce Labs Backpack and navigate to checkout step one."""
        inventory = InventoryPage(page)
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.go_to_cart()
        cart = CartPage(page)
        cart.click_checkout()
        page.wait_for_url("**/checkout-step-one.html")

    # TC_CHK_01
    def test_checkout_error_when_first_name_missing(self, logged_in_page):
        self._add_item_and_go_to_checkout(logged_in_page)
        info = CheckoutInfoPage(logged_in_page)
        info.fill_info("", "Doe", "12345")
        info.click_continue()
        assert "checkout-step-one" in logged_in_page.url
        assert info.is_error_displayed()
        assert "First Name is required" in info.get_error_message()

    # TC_CHK_02
    def test_checkout_error_when_last_name_missing(self, logged_in_page):
        self._add_item_and_go_to_checkout(logged_in_page)
        info = CheckoutInfoPage(logged_in_page)
        info.fill_info("John", "", "12345")
        info.click_continue()
        assert "checkout-step-one" in logged_in_page.url
        assert info.is_error_displayed()
        assert "Last Name is required" in info.get_error_message()

    # TC_CHK_03
    def test_checkout_error_when_zip_missing(self, logged_in_page):
        self._add_item_and_go_to_checkout(logged_in_page)
        info = CheckoutInfoPage(logged_in_page)
        info.fill_info("John", "Doe", "")
        info.click_continue()
        assert "checkout-step-one" in logged_in_page.url
        assert info.is_error_displayed()
        assert "Postal Code is required" in info.get_error_message()

    # TC_CHK_04
    def test_valid_checkout_info_proceeds_to_overview(self, logged_in_page):
        self._add_item_and_go_to_checkout(logged_in_page)
        info = CheckoutInfoPage(logged_in_page)
        info.fill_info("John", "Doe", "12345")
        info.click_continue()
        logged_in_page.wait_for_url("**/checkout-step-two.html")
        assert "checkout-step-two" in logged_in_page.url
        assert not info.is_error_displayed()
        assert logged_in_page.locator(".summary_info").is_visible()

    # TC_CHK_05
    def test_completing_order_shows_confirmation_and_clears_cart(self, logged_in_page):
        self._add_item_and_go_to_checkout(logged_in_page)
        info = CheckoutInfoPage(logged_in_page)
        info.fill_info("John", "Doe", "12345")
        info.click_continue()
        logged_in_page.wait_for_url("**/checkout-step-two.html")

        overview = CheckoutOverviewPage(logged_in_page)
        overview.click_finish()
        logged_in_page.wait_for_url("**/checkout-complete.html")

        complete = CheckoutCompletePage(logged_in_page)
        assert "checkout-complete" in logged_in_page.url
        assert "Thank you for your order" in complete.get_complete_header()
        assert logged_in_page.locator("[data-test='back-to-products']").is_visible()

        # Navigate to cart and verify it is empty
        logged_in_page.goto(f"{BASE_URL}/cart.html")
        cart = CartPage(logged_in_page)
        assert cart.get_item_count() == 0
        assert not cart.is_cart_badge_visible()

    # TC_E2E_01
    def test_full_happy_path_purchase(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(VALID_USER["username"], VALID_USER["password"])
        page.wait_for_url("**/inventory.html")

        inventory = InventoryPage(page)
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.go_to_cart()
        page.wait_for_url("**/cart.html")

        cart = CartPage(page)
        cart.click_checkout()
        page.wait_for_url("**/checkout-step-one.html")

        info = CheckoutInfoPage(page)
        info.fill_info("John", "Doe", "12345")
        info.click_continue()
        page.wait_for_url("**/checkout-step-two.html")

        overview = CheckoutOverviewPage(page)
        # Verify price totals
        item_total = overview.get_item_total()
        tax = overview.get_tax()
        grand_total = overview.get_total()
        assert abs(grand_total - (item_total + tax)) < 0.01
        assert abs(tax - round(item_total * 0.08, 2)) < 0.01

        overview.click_finish()
        page.wait_for_url("**/checkout-complete.html")

        complete = CheckoutCompletePage(page)
        assert "Thank you for your order" in complete.get_complete_header()
        assert not page.locator(".shopping_cart_badge").is_visible()
        assert "checkout-complete.html" in page.url
