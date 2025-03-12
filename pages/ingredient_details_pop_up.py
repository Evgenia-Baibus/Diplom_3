from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class IngredientDetailsPopUp(BasePage):
    ingredient_details_title = (By.XPATH, ".//h2[text() = 'Детали ингредиента']")
    close_btn = (By.CLASS_NAME, 'Modal_modal__close__TnseK')


    def wait_for_load_ingredient_details_pop_up(self):
        self.wait_for_element(self.ingredient_details_title)

    def click_close_btn(self):
        self.click_element(self.close_btn)

    def get_order_id(self):
        order_id = self.wait_for_element(self.order_id).text
        return order_id
