from time import sleep

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

    def is_loaded(self):
        self.wait_for_main_page()
        return self.driver.current_url == Urls.BASE_URL

    def wait_for_main_page(self):
        self.wait_for_element(self.place_order_btn)

    def click_ingredient(self):
        self.click_element(self.bun)

    def is_main_page_open(self):
        return self.wait_for_element(self.sauces_section).text == 'Соусы'

    def drag_and_drop_bun(self):
        self.drag_and_drop(self.bun, self.create_order_zone)

    def drag_and_drop_sauces(self):
        self.drag_and_drop(self.sauces, self.create_order_zone)

    def drag_and_drop_fillings(self):
        self.drag_and_drop(self.fillings, self.create_order_zone)

    def click_place_order_btn(self):
        self.click_element(self.place_order_btn)
