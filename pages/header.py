from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Header(BasePage):
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")
    order_list_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")

    def click_personal_account_button(self):
        self.click_element(self.personal_account_btn)

    def click_constructor_btn(self):
        self.click_element(self.constructor_btn)

    def click_order_list_btn(self):
        self.click_element(self.order_list_btn)
