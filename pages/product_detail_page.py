from pages.base_page import BasePage


class ProductDetailPage(BasePage):
    PRODUCT_NAME = ".inventory_details_name"
    PRODUCT_DESC = ".inventory_details_desc"
    PRODUCT_PRICE = ".inventory_details_price"
    ADD_TO_CART_BTN = "[data-test='add-to-cart']"
    BACK_TO_PRODUCTS_BTN = "[data-test='back-to-products']"

    def get_product_name(self) -> str:
        return self.page.locator(self.PRODUCT_NAME).inner_text()

    def get_product_price(self) -> str:
        return self.page.locator(self.PRODUCT_PRICE).inner_text()

    def get_product_description(self) -> str:
        return self.page.locator(self.PRODUCT_DESC).inner_text()

    def click_add_to_cart(self):
        self.page.click(self.ADD_TO_CART_BTN)

    def click_back_to_products(self):
        self.page.click(self.BACK_TO_PRODUCTS_BTN)

    def is_add_to_cart_visible(self) -> bool:
        return self.page.locator(self.ADD_TO_CART_BTN).is_visible()

    def is_back_to_products_visible(self) -> bool:
        return self.page.locator(self.BACK_TO_PRODUCTS_BTN).is_visible()
