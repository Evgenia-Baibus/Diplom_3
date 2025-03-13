from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    recovery_btn = (By.XPATH, ".//button[text() = 'Восстановить']")
    email_field = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

    def set_email(self, email):
        self._click_email_input()
        self.send_keys_to_input(self.email_field, email)

    def _click_email_input(self):
        self.click_element(self.email_field)


    def click_recovery_btn(self):
        self.click_element(self.recovery_btn)
