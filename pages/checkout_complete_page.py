from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = ".complete-header"
    COMPLETE_TEXT = ".complete-text"
    BACK_HOME_BTN = "[data-test='back-to-products']"

    def get_complete_header(self) -> str:
        return self.page.locator(self.COMPLETE_HEADER).inner_text()

    def get_complete_text(self) -> str:
        return self.page.locator(self.COMPLETE_TEXT).inner_text()

    def click_back_home(self):
        self.page.click(self.BACK_HOME_BTN)
