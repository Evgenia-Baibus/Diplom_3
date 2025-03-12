from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderDetailsPopUp(BasePage):
    order_id = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi')]/p[contains(@class, 'text_type_digits-default')]")

    def is_order_details_pop_up_displayed(self, order_number):
        order_number_pop_up = self.wait_for_element(self.order_id).text
        return order_number == order_number_pop_up
