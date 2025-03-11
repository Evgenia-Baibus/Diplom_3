from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderListPage(BasePage):

    order_list_title = (By.XPATH, ".//h1[text() = 'Лента заказов']")

    def wait_for_load_order_list_page(self):
        self.wait_for_element(self.order_list_title)

