import allure

from data import IngredientData
from pages.header import Header
from pages.ingredient_details_pop_up import IngredientDetailsPopUp
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage


class TestBasicFunctionality:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('Кликаем на «Конструктор» и проверяем, что открылась главная страница')
    def test_success_transition_to_constructor(self, authorized_driver):
        header = Header(authorized_driver)
        main_page = MainPage(authorized_driver)

        header.click_constructor_btn()

        assert main_page.is_loaded()

    @allure.title('Проверка перехода по клику на «Лента заказов»»')
    @allure.description('Кликаем на «Лента заказов» и проверяем, что открылась лента заказов')
    def test_success_transition_to_order_list(self, authorized_driver):
        header = Header(authorized_driver)
        order_list = OrderListPage(authorized_driver)

        header.click_order_list_btn()
        order_list.wait_for_load_order_list_page()

        assert order_list.is_loaded()

    @allure.title('Проверка открытия pop up с деталями по клику на ингредиент')
    @allure.description('Кликаем на ингредиент и проверяем, что открывается pop up')
    def test_open_pop_up_with_ingredients_details(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        ingredient_details_pop_up = IngredientDetailsPopUp(authorized_driver)

        main_page.wait_for_main_page()
        main_page.click_ingredient(IngredientData.bun_name)

        assert ingredient_details_pop_up.is_opened(IngredientData.bun_name, IngredientData.bun_id)

    @allure.title('Проверка закрытия pop up с деталями по клику на ингредиент')
    @allure.description('Кликаем на кнопку закрытия pop up и проверяем, что отображается главная страница')
    def test_close_pop_up_with_ingredients_details(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        ingredient_details_pop_up = IngredientDetailsPopUp(authorized_driver)

        main_page.wait_for_main_page()
        main_page.click_ingredient(IngredientData.bun_name)
        ingredient_details_pop_up.is_opened(IngredientData.bun_name, IngredientData.bun_id)
        ingredient_details_pop_up.click_close_btn()

        assert main_page.is_main_page_open()

    @allure.title('Проверка, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.description('Проверяем каунтер до и после добавления ингредиента в заказ')
    def test_increase_ingredient_counter(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        main_page.wait_for_main_page()
        bun = IngredientData.bun

        count_before = main_page.get_ingredient_count(bun)
        main_page.drag_and_drop_ingredient(bun)
        count_after = main_page.get_ingredient_count(bun)

        assert count_after > count_before


    @allure.title('Проверка оформления заказа авторизованным пользователем')
    @allure.description('Добавляем ингредиенты в заказ и проверяем, что создается заказ')
    def test_success_order_burger_for_authorized_user(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        bun = IngredientData.bun
        sauce = IngredientData.sauce
        filling = IngredientData.filling

        main_page.wait_for_main_page()
        main_page.drag_and_drop_ingredient(bun)
        main_page.drag_and_drop_ingredient(sauce)
        main_page.drag_and_drop_ingredient(filling)
        main_page.click_place_order_btn()

        assert main_page.is_main_page_open()
