import pytest
from pages.inventory_page import InventoryPage
from utils.helpers import parse_price


class TestInventory:

    # TC_INV_01
    def test_inventory_displays_six_products(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        assert inventory.get_product_count() == 6

    # TC_INV_02
    def test_sort_by_price_low_to_high(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.sort_by("lohi")
        prices_text = inventory.get_all_product_prices()
        prices = [parse_price(p) for p in prices_text]
        assert prices == sorted(prices)
        assert prices[0] == 7.99
        assert prices[-1] == 49.99

    # TC_INV_03
    def test_sort_by_name_z_to_a(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.sort_by("za")
        names = inventory.get_all_product_names()
        assert names == sorted(names, reverse=True)

    # TC_INV_04
    def test_adding_product_increments_cart_badge(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        assert not inventory.is_cart_badge_visible()
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        assert inventory.get_cart_badge_count() == 1
        inventory.add_product_to_cart_by_name("Sauce Labs Bike Light")
        assert inventory.get_cart_badge_count() == 2

    # TC_INV_05
    def test_removing_product_decrements_cart_badge_to_zero(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        assert inventory.get_cart_badge_count() == 1
        inventory.remove_product_from_cart_by_name("Sauce Labs Backpack")
        assert not inventory.is_cart_badge_visible()
