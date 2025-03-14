import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    place_order_btn = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    bun = (By.CSS_SELECTOR, "img[alt*='Флюоресцентная булка R2-D3']")
    sauces = (By.CSS_SELECTOR, "img[alt*='Соус Spicy-X']")
    fillings = (By.CSS_SELECTOR, "img[alt*='Мясо бессмертных моллюсков Protostomia']")
    create_order_zone = (By.XPATH, ".//span[@class = 'constructor-element__row']")
    sauces_section = (By.XPATH, ".//h2[text() = 'Соусы']")

    @staticmethod
    @allure.step('Функция возвращает локатор с введенным текстом')
    def ingredient(name):
        return By.CSS_SELECTOR, f"img[alt*='{name}']"

    @staticmethod
    @allure.step('Функция возвращает локатор каунтера ингредиента')
    def ingredient_counter(ingredient_id):
        return By.XPATH, f".//a[contains(@href, '{ingredient_id}')]//p[contains(@class, 'counter_counter__num__3nue1')]"

    @allure.step('Загрузка главной страницы')
    def is_loaded(self):
        self.wait_for_main_page()
        return self.driver.current_url == Urls.BASE_URL

    @allure.step('Загрузка главной страницы')
    def wait_for_main_page(self):
        self.wait_for_element(self.place_order_btn)

    @allure.step('Нажать на ингредиент')
    def click_ingredient(self, name):
        with allure.step(f"Нажать на ингредиент '{name}'"):
            self.click_element(self.ingredient(name))

    @allure.step('Открытие главной страницы после закрытия pop up с деталями ингредиента')
    def is_main_page_open(self):
        return self.wait_for_element(self.sauces_section).text == 'Соусы'

    @allure.step('Перенести ингредиент в поле заказа')
    def drag_and_drop_ingredient(self, ingredient):
        self.drag_and_drop(self.ingredient(ingredient.name), self.create_order_zone)

    #передать параметр
    @allure.step('Перенести булку в поле заказа')
    def drag_and_drop_bun(self):
        self.drag_and_drop(self.bun, self.create_order_zone)

    @allure.step('Перенести соус в поле заказа')
    def drag_and_drop_sauces(self):
        self.drag_and_drop(self.sauces, self.create_order_zone)

    @allure.step('Перенести начинку в поле заказа')
    def drag_and_drop_fillings(self):
        self.drag_and_drop(self.fillings, self.create_order_zone)

    @allure.step('Нажать на кнопку оформления заказа')
    def click_place_order_btn(self):
        self.click_element(self.place_order_btn)

    @allure.step('Получить каунтер ингредиента')
    def get_ingredient_count(self, ingredient):
        counter = self.wait_for_element(self.ingredient_counter(ingredient.ingredient_id))
        ingredient_count = int(counter.text)
        return ingredient_count