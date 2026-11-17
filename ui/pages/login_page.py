from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginLocators
from config.config import Config

class LoginPage(BasePage):
    def open_app(self):
        self.goto(Config.BASE_URL)

    def open_clinic(self):
        self.click(LoginLocators.CLINIC_CARD)
        self.click(LoginLocators.OPEN_BUTTON)