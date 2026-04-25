from pages.base_page import BasePage
from utils.config import BASE_URL


class InventoryPage(BasePage):
    URL = f"{BASE_URL}/inventory.html"
    PAGE_TITLE = ".title"
    INVENTORY_ITEMS = ".inventory_item"
    ITEM_NAMES = ".inventory_item_name"
    ITEM_PRICES = ".inventory_item_price"
    SORT_DROPDOWN = "[data-test='product_sort_container']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    HAMBURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def open(self):
        self.navigate(self.URL)

    def get_product_count(self) -> int:
        return self.page.locator(self.INVENTORY_ITEMS).count()

    def get_all_product_names(self) -> list:
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def get_all_product_prices(self) -> list:
        return self.page.locator(self.ITEM_PRICES).all_inner_texts()

    def sort_by(self, option_value: str):
        self.page.select_option(self.SORT_DROPDOWN, option_value)

    def add_product_to_cart_by_name(self, name: str):
        item = self.page.locator(self.INVENTORY_ITEMS).filter(has_text=name)
        item.get_by_role("button", name="Add to cart").click()

    def remove_product_from_cart_by_name(self, name: str):
        item = self.page.locator(self.INVENTORY_ITEMS).filter(has_text=name)
        item.get_by_role("button", name="Remove").click()

    def get_cart_badge_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        if badge.is_visible():
            return int(badge.inner_text())
        return 0

    def is_cart_badge_visible(self) -> bool:
        return self.page.locator(self.CART_BADGE).is_visible()

    def go_to_cart(self):
        self.page.click(self.CART_LINK)

    def click_product_name(self, name: str):
        self.page.get_by_text(name, exact=True).click()

    def logout(self):
        self.page.click(self.HAMBURGER_MENU)
        self.page.click(self.LOGOUT_LINK)
