import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    recovery_btn = (By.XPATH, ".//button[text() = 'Восстановить']")
    email_field = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

    @allure.step('Ввести email')
    def set_email(self, email):
        self.send_keys_to_input(self.email_field, email)

    @allure.step('Нажать на кнопку Восстановить')
    def click_recovery_btn(self):
        self.click_element(self.recovery_btn)
