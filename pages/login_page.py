from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    recovery_password_btn = (By.XPATH, ".//a[text() = 'Восстановить пароль']")

    def wait_for_load_login_page(self):
        self.wait_for_element(self.recovery_password_btn)

    def click_recovery_password_btn(self):
        self.scroll_to_element(self.recovery_password_btn)
        self.click_element(self.recovery_password_btn)
