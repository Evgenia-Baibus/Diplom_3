from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    order_history_section = (By.XPATH, ".//a[text() = 'История заказов']")
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")
    order_displayed = (By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList__374GU')]/li[last()]/a/div/p")

    def wait_for_personal_account_page(self):
        self.wait_for_element(self.exit_btn)

    def click_order_history_section(self):
        self.click_element(self.order_history_section)

    def click_exit_btn(self):
        self.click_element(self.exit_btn)

    def is_order_displayed(self, order_id):
        order_displayed = self.wait_for_element(self.order_displayed, timeout=5)
        return order_displayed.text == f'#0{order_id}'


