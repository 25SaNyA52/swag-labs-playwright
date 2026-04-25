from pages.base_page import BasePage
from utils.config import BASE_URL


class LoginPage(BasePage):
    URL = BASE_URL
    USERNAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def open(self):
        self.navigate(self.URL)

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_FIELD, username)
        self.page.fill(self.PASSWORD_FIELD, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()

    def is_error_displayed(self) -> bool:
        return self.page.locator(self.ERROR_MESSAGE).is_visible()
