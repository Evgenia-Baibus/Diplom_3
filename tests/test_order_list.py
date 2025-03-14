import allure

from data import IngredientData
from helpers import User
from pages.header import Header
from pages.order_details_pop_up import OrderDetailsPopUp
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderList:

    @allure.title('Проверка открытия pop up с деталями заказа')
    @allure.description('При клике на заказ открывается pop up с деталями заказа')
    def test_open_pop_up_with_order_details(self, authorized_driver):
        header = Header(authorized_driver)
        order_list_page = OrderListPage(authorized_driver)
        order_details_pop_up = OrderDetailsPopUp(authorized_driver)

        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()
        order_id = order_list_page.click_order_item()

        assert order_details_pop_up.is_order_details_pop_up_displayed(order_id)

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('После оформления заказа его номер отображается в «История заказов» и в «Лента заказов»')
    def test_orders_displayed_in_order_history_and_order_list(self, authorized_driver, order_number):
        header = Header(authorized_driver)
        order_list_page = OrderListPage(authorized_driver)
        personal_account_page = PersonalAccountPage(authorized_driver)

        header.click_personal_account_button()
        personal_account_page.wait_for_personal_account_page()
        personal_account_page.click_order_history_section()

        assert personal_account_page.is_order_displayed(order_number)

        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()

        assert order_list_page.is_order_in_feed(order_number)

    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    @allure.description('Счетчик до оформления заказа меньше счетчика после оформления')
    def test_increase_order_counter_for_all_time(self, authorized_driver,  login_data):
        header = Header(authorized_driver)
        order_list_page = OrderListPage(authorized_driver)

        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()

        order_count_before = order_list_page.get_order_count_for_all_time()

        self.__make_order(login_data)

        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()
        order_count_after = order_list_page.get_order_count_for_all_time()

        assert order_count_after > order_count_before

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    @allure.description('Счетчик до оформления заказа меньше счетчика после оформления')
    def test_increase_order_counter_today(self, authorized_driver,  login_data):
        header = Header(authorized_driver)
        order_list_page = OrderListPage(authorized_driver)

        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()

        order_count_before = order_list_page.get_order_count_today()

        self.__make_order(login_data)

        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()
        order_count_after = order_list_page.get_order_count_today()

        assert order_count_after > order_count_before

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    @allure.description('После оформления заказа его номер отображается в разделе «В работе»')
    def test_order_in_progress(self, authorized_driver, order_number):
        header = Header(authorized_driver)
        order_list_page = OrderListPage(authorized_driver)

        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()

        assert order_list_page.is_order_in_progress(order_number)


    @staticmethod
    @allure.step('Сделать заказ')
    def __make_order(login_data):
        User.create_order(login_data['accessToken'], [IngredientData.ingredient_id])