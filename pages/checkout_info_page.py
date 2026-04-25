from pages.base_page import BasePage


class CheckoutInfoPage(BasePage):
    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    CONTINUE_BTN = "[data-test='continue']"
    CANCEL_BTN = "[data-test='cancel']"
    ERROR_MESSAGE = "[data-test='error']"

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        self.page.click(self.CONTINUE_BTN)

    def click_cancel(self):
        self.page.click(self.CANCEL_BTN)

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()

    def is_error_displayed(self) -> bool:
        return self.page.locator(self.ERROR_MESSAGE).is_visible()
