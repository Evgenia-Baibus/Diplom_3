import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    recovery_password_btn = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
    email_field = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")
    sign_in_btn = (By.XPATH, ".//button[text() = 'Войти']")

    @allure.step('Авторизоваться')
    def login(self, login_data):
        self._set_email(login_data["email"])
        self._set_password(login_data["password"])
        self._click_sign_in_btn()

    @allure.step('Загрузка страницы авторизации пользователя')
    def wait_for_load_login_page(self):
        self.wait_for_element(self.recovery_password_btn)

    @allure.step('Нажать на кнопку восстановления пароля')
    def click_recovery_password_btn(self):
        self.scroll_to_element(self.recovery_password_btn)
        self.click_element(self.recovery_password_btn)

    @allure.step('Ввести email')
    def _set_email(self, email):
        self.send_keys_to_input(self.email_field, email)

    @allure.step('Ввести пароль')
    def _set_password(self, password):
        self.send_keys_to_input(self.password_input, password)

    @allure.step('Нажать на кнопку «Войти»')
    def _click_sign_in_btn(self):
        self.scroll_to_element(self.sign_in_btn)
        self.click_element(self.sign_in_btn)
