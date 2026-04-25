from pages.base_page import BasePage
from utils.config import BASE_URL


class CartPage(BasePage):
    URL = f"{BASE_URL}/cart.html"
    CART_ITEMS = ".cart_item"
    ITEM_NAMES = ".inventory_item_name"
    CART_QUANTITY = ".cart_quantity"
    ITEM_PRICE = ".inventory_item_price"
    CHECKOUT_BTN = "[data-test='checkout']"
    CONTINUE_SHOPPING_BTN = "[data-test='continue-shopping']"
    CART_BADGE = ".shopping_cart_badge"

    def open(self):
        self.navigate(self.URL)

    def get_item_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()

    def get_item_names(self) -> list:
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def remove_item_by_name(self, name: str):
        item = self.page.locator(self.CART_ITEMS).filter(has_text=name)
        item.get_by_role("button", name="Remove").click()

    def click_checkout(self):
        self.page.click(self.CHECKOUT_BTN)

    def click_continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING_BTN)

    def is_cart_badge_visible(self) -> bool:
        return self.page.locator(self.CART_BADGE).is_visible()
