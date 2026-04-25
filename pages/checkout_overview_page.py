from pages.base_page import BasePage
from utils.helpers import parse_price


class CheckoutOverviewPage(BasePage):
    SUBTOTAL_LABEL = ".summary_subtotal_label"
    TAX_LABEL = ".summary_tax_label"
    TOTAL_LABEL = ".summary_total_label"
    FINISH_BTN = "[data-test='finish']"
    CANCEL_BTN = "[data-test='cancel']"

    def get_item_total(self) -> float:
        text = self.page.locator(self.SUBTOTAL_LABEL).inner_text()
        return parse_price(text.split("$")[-1])

    def get_tax(self) -> float:
        text = self.page.locator(self.TAX_LABEL).inner_text()
        return parse_price(text.split("$")[-1])

    def get_total(self) -> float:
        text = self.page.locator(self.TOTAL_LABEL).inner_text()
        return parse_price(text.split("$")[-1])

    def click_finish(self):
        self.page.click(self.FINISH_BTN)

    def click_cancel(self):
        self.page.click(self.CANCEL_BTN)
