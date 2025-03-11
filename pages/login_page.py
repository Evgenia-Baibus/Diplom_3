from selenium.webdriver.common.by import By

from data import LoginData
from pages.base_page import BasePage

class LoginPage(BasePage):
    recovery_password_btn = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
    email_field = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")
    sign_in_btn = (By.XPATH, ".//button[text() = 'Войти']")


    def wait_for_load_login_page(self):
        self.wait_for_element(self.recovery_password_btn)

    def click_recovery_password_btn(self):
        self.scroll_to_element(self.recovery_password_btn)
        self.click_element(self.recovery_password_btn)

    def set_email(self):
        self.send_keys_to_input(self.email_field, LoginData.email)

    def set_password(self):
        self.send_keys_to_input(self.password_input, LoginData.password)

    def click_sign_in_btn(self):
        self.scroll_to_element(self.sign_in_btn)
        self.click_element(self.sign_in_btn)


