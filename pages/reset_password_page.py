from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ResetPasswordPage(BasePage):

    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")
    password_hide_icon = (By.CLASS_NAME, 'input__icon-action')
    active_password_field = (By.CLASS_NAME, 'input_status_active')


    def wait_for_load_reset_password_page(self):
        self.wait_for_element(self.save_btn)

    def click_password_hide_icon(self):
        self.click_element(self.password_hide_icon)

    def is_password_field_active(self):
        return self.wait_for_element(self.active_password_field).text == 'Пароль'
