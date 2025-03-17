import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import Urls


class OrderListPage(BasePage):
    order_list_title = (By.XPATH, ".//h1[text() = 'Лента заказов']")
    order_item = (By.XPATH, ".//ul[@class ='OrderFeed_list__OLh59']/li[1]")
    order_id = (By.XPATH, ".//ul[@class ='OrderFeed_list__OLh59']/li[1]/a/div/p")
    order_count_for_all_time = (By.XPATH, ".//div/p[text() = 'Выполнено за все время:']/following-sibling::p")
    order_count_today = (By.XPATH, ".//div/p[text() = 'Выполнено за сегодня:']/following-sibling::p")

    @staticmethod
    def order_in_progress(order_number):
        return By.XPATH, f".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[contains(normalize-space(), '{order_number}')]"

    @staticmethod
    def order_in_feed(order_number):
        return By.XPATH, f".//ul[contains(@class, 'OrderFeed_list__OLh59')]//p[contains(@class, 'text_type_digits-default') and contains(text(), '{order_number}')]"

    @allure.step('Загрузка страницы Лента заказов')
    def wait_for_load_order_list_page(self):
        self.wait_for_element(self.order_list_title)

    @allure.step('Нажать на заказ')
    def click_order_item(self):
        order_number = self.wait_for_element(self.order_id).text
        self.click_element(self.order_item)
        return order_number

    @allure.step('Получить кол-во заказов "Выполнено за всё время"')
    def get_order_count_for_all_time(self):
        order_count_for_all_time = self.wait_for_element(self.order_count_for_all_time).text
        return int(order_count_for_all_time)

    @allure.step('Получить кол-во заказов "Выполнено за сегодня"')
    def get_order_count_today(self):
        order_count_today = self.wait_for_element(self.order_count_today).text
        return int(order_count_today)

    @allure.step('Проверить, что заказ есть в списке "В работе"')
    def is_order_in_progress(self, order_number):
        order_in_progress = self.wait_for_element(self.order_in_progress(order_number), timeout=10)
        return order_in_progress.text == f'0{order_number}'

    @allure.step('Проверить, что заказ есть в списке заказов')
    def is_order_in_feed(self, order_number):
        order_in_feed = self.wait_for_element(self.order_in_feed(order_number), timeout=5)
        return order_in_feed.text == f'#0{order_number}'

    @allure.step('Проверить, что текущий урл - урл ленты заказов')
    def is_loaded(self):
        self.wait_for_load_order_list_page()
        return self.driver.current_url == Urls.FEED

