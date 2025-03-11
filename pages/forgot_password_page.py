from selenium.webdriver.common.by import By
from data import LoginData
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    recovery_btn = (By.XPATH, ".//button[text() = 'Восстановить']")
    email_field = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

    def click_email_input(self):
        self.click_element(self.email_field)

    def set_email(self):
        self.send_keys_to_input(self.email_field, LoginData.email)

    def click_recovery_btn(self):
        self.click_element(self.recovery_btn)
