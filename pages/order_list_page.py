from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderListPage(BasePage):

    order_list_title = (By.XPATH, ".//h1[text() = 'Лента заказов']")
    order_item = (By.XPATH, ".//ul[@class ='OrderFeed_list__OLh59']/li[1]")
    order_id = (By.XPATH, ".//ul[@class ='OrderFeed_list__OLh59']/li[1]/a/div/p")
    order_count_for_all_time = (By.XPATH, ".//div/p[text() = 'Выполнено за все время:']/following-sibling::p")
    order_count_today = (By.XPATH, ".//div/p[text() = 'Выполнено за сегодня:']/following-sibling::p")
    order_in_progress = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[starts-with(text(),'0')]") # неправильный селектор
    order_in_feed = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list__OLh59')]/li[1]/a/div/p")


    def wait_for_load_order_list_page(self):
        self.wait_for_element(self.order_list_title)

    def click_order_item(self):
        order_number = self.wait_for_element(self.order_id).text
        self.click_element(self.order_item)
        return order_number

    def get_order_count_for_all_time(self):
        order_count_for_all_time = self.wait_for_element(self.order_count_for_all_time).text
        return int(order_count_for_all_time)


    def is_order_counter_increase_for_all_time(self, order_count_for_all_time):
        order_count_for_all_time_after = self.wait_for_element(self.order_count_for_all_time).text
        return int(order_count_for_all_time_after) > order_count_for_all_time

    def get_order_count_today(self):
        order_count_today = self.wait_for_element(self.order_count_today).text
        return int(order_count_today)


    def is_order_counter_increase_today(self, order_count_today):
        order_count_today_after = self.wait_for_element(self.order_count_today).text
        return int(order_count_today_after) > order_count_today

    def is_order_in_progress(self, order_id):
        order_in_progress = self.wait_for_element(self.order_in_progress, timeout=5)
        return order_in_progress.text == f'0{order_id}'

    def is_order_in_feed(self, order_id):
        order_in_feed = self.wait_for_element(self.order_in_feed, timeout=5)
        return order_in_feed.text == f'#0{order_id}'

