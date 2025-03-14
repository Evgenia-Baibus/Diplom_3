import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    place_order_btn = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    create_order_zone = (By.XPATH, ".//span[@class = 'constructor-element__row']")
    sauces_section = (By.XPATH, ".//h2[text() = 'Соусы']")

    @staticmethod
    def ingredient(name):
        return By.CSS_SELECTOR, f"img[alt*='{name}']"

    @staticmethod
    def ingredient_counter(ingredient_id):
        return By.XPATH, f".//a[contains(@href, '{ingredient_id}')]//p[contains(@class, 'counter_counter__num__3nue1')]"

    @allure.step('Загрузка главной страницы')
    def is_loaded(self):
        self.wait_for_main_page()
        return self.driver.current_url == Urls.BASE_URL

    @allure.step('Проверить, что загрузилась главная страница')
    def wait_for_main_page(self):
        self.wait_for_element(self.place_order_btn)

    def click_ingredient(self, name):
        with allure.step(f"Нажать на ингредиент '{name}'"):
            self.click_element(self.ingredient(name))

    @allure.step('Открытие главной страницы после закрытия pop up с деталями ингредиента')
    def is_main_page_open(self):
        return self.wait_for_element(self.sauces_section).text == 'Соусы'

    def drag_and_drop_ingredient(self, ingredient):
        with allure.step(f"Перенести ингредиент '{ingredient.name}' в поле заказа"):
            self.drag_and_drop(self.ingredient(ingredient.name), self.create_order_zone)

    @allure.step('Нажать на кнопку «Оформить заказ»')
    def click_place_order_btn(self):
        self.click_element(self.place_order_btn)

    @allure.step('Получить каунтер ингредиента')
    def get_ingredient_count(self, ingredient):
        counter = self.wait_for_element(self.ingredient_counter(ingredient.ingredient_id))
        ingredient_count = int(counter.text)
        return ingredient_count