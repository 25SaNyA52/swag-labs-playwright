import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:

    # TC_CART_01
    def test_cart_displays_correct_added_item(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        assert cart.get_item_count() == 1
        assert "Sauce Labs Backpack" in cart.get_item_names()
        assert logged_in_page.locator(".cart_quantity").first.inner_text() == "1"
        assert logged_in_page.locator(".inventory_item_price").first.inner_text() == "$29.99"
        assert logged_in_page.locator(".cart_item").first.get_by_role("button", name="Remove").is_visible()
        assert logged_in_page.locator("[data-test='continue-shopping']").is_visible()
        assert logged_in_page.locator("[data-test='checkout']").is_visible()

    # TC_CART_02
    def test_removing_item_from_cart_empties_cart(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        cart.remove_item_by_name("Sauce Labs Backpack")

        assert cart.get_item_count() == 0
        assert not cart.is_cart_badge_visible()
        assert logged_in_page.locator("[data-test='continue-shopping']").is_visible()
        assert logged_in_page.locator("[data-test='checkout']").is_visible()
