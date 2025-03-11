from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    order_history_section = (By.XPATH, ".//a[text() = 'История заказов']")
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")

    def wait_for_personal_account_page(self):
        self.wait_for_element(self.exit_btn)

    def click_order_history_section(self):
        self.click_element(self.order_history_section)

    def click_exit_btn(self):
        self.click_element(self.exit_btn)


