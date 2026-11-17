from ui.pages.base_page import BasePage
from ui.locators.dashboard_locators import DashboardLocators

class DashboardPage(BasePage):
    def click_patients(self):
        self.page.locator("a[href*='patient']").first.click()

    def click_add_appointment(self):
        self.click(DashboardLocators.ADD_APPOINTMENT_BTN)