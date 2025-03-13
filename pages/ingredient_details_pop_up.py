from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import Urls


class IngredientDetailsPopUp(BasePage):
    close_btn = (By.CLASS_NAME, 'Modal_modal__close__TnseK')

    @staticmethod
    def ingredient_title(name):
        return By.XPATH, f".//p[text() = '{name}']"

    def is_opened(self, ingredient_name, ingredient_id):
        self.wait_for_element(self.ingredient_title(ingredient_name))
        return self.driver.current_url == Urls.make_ingredient_url(ingredient_id)

    def click_close_btn(self):
        self.click_element(self.close_btn)
