from data import IngredientData
from pages.header import Header
from pages.ingredient_details_pop_up import IngredientDetailsPopUp
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from urls import Urls


class TestBasicFunctionality:

    def test_success_transition_to_constructor(self, authorized_driver):
        header = Header(authorized_driver)
        main_page = MainPage(authorized_driver)

        header.click_constructor_btn()

        assert main_page.is_loaded()

    def test_success_transition_to_order_list(self, authorized_driver):
        header = Header(authorized_driver)
        order_list = OrderListPage(authorized_driver)

        header.click_order_list_btn()
        order_list.wait_for_load_order_list_page()

        assert order_list.is_loaded()

    def test_open_pop_up_with_ingredients_details(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        ingredient_details_pop_up = IngredientDetailsPopUp(authorized_driver)

        main_page.wait_for_main_page()
        main_page.click_ingredient(IngredientData.bun_name)

        assert ingredient_details_pop_up.is_opened(IngredientData.bun_name, IngredientData.bun_id)

    def test_close_pop_up_with_ingredients_details(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        ingredient_details_pop_up = IngredientDetailsPopUp(authorized_driver)

        main_page.wait_for_main_page()
        main_page.click_ingredient(IngredientData.bun_name)
        ingredient_details_pop_up.is_opened(IngredientData.bun_name, IngredientData.bun_id)
        ingredient_details_pop_up.click_close_btn()

        assert main_page.is_main_page_open()

    def test_success_order_burger_for_authorized_user(self, authorized_driver):
        main_page = MainPage(authorized_driver)

        main_page.wait_for_main_page()
        main_page.drag_and_drop_bun()
        main_page.drag_and_drop_sauces()
        main_page.drag_and_drop_fillings()
        main_page.click_place_order_btn()

        assert main_page.is_main_page_open()
