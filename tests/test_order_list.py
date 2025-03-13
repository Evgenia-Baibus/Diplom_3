from data import IngredientData
from helpers import User
from pages.header import Header
from pages.main_page import MainPage
from pages.order_details_pop_up import OrderDetailsPopUp
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderList:

    def test_open_pop_up_with_order_details(self, authorized_driver):

        header = Header(authorized_driver)
        order_list_page = OrderListPage(authorized_driver)
        order_details_pop_up = OrderDetailsPopUp(authorized_driver)

        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()
        order_id = order_list_page.click_order_item()

        assert order_details_pop_up.is_order_details_pop_up_displayed(order_id)

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


    def test_increase_order_counter_for_all_time(self, authorized_driver,  login_data):
        header = Header(authorized_driver)
        order_list_page = OrderListPage(authorized_driver)

        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()

        order_count = order_list_page.get_order_count_for_all_time()

        User.create_order(login_data['accessToken'], [IngredientData.ingredient_id])


        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()

        assert order_list_page.is_order_counter_increase_for_all_time(order_count)

    def test_increase_order_counter_today(self, authorized_driver,  login_data):
        header = Header(authorized_driver)
        order_list_page = OrderListPage(authorized_driver)

        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()

        order_count = order_list_page.get_order_count_today()

        User.create_order(login_data['accessToken'], [IngredientData.ingredient_id])



        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()

        assert order_list_page.is_order_counter_increase_today(order_count)

    def test_order_in_progress(self, authorized_driver, order_number):

        header = Header(authorized_driver)
        order_list_page = OrderListPage(authorized_driver)


        header.click_order_list_btn()
        order_list_page.wait_for_load_order_list_page()

        assert order_list_page.is_order_in_progress(order_number)






