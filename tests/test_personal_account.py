import allure

from pages.header import Header
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from tests.conftest import authorized_driver
from urls import Urls


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    @allure.description('Кликнуть на кнопку «Личный кабинет» на главной странице')
    def test_success_transition_to_personal_account(self, authorized_driver):
        header = Header(authorized_driver)
        personal_account_page = PersonalAccountPage(authorized_driver)

        header.click_personal_account_button()
        personal_account_page.wait_for_personal_account_page()

        assert authorized_driver.current_url == Urls.PROFILE

    @allure.title('Проверка перехода в раздел «История заказов»')
    @allure.description('Кликнуть на кнопку «История заказов» на странице личного кабинета')
    def test_success_transition_to_history_section(self, authorized_driver):
        header = Header(authorized_driver)
        personal_account_page = PersonalAccountPage(authorized_driver)

        header.click_personal_account_button()
        personal_account_page.wait_for_personal_account_page()
        personal_account_page.click_order_history_section()

        assert authorized_driver.current_url == Urls.ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Кликнуть на кнопку «Выход» на странице личного кабинета')
    def test_success_log_out(self, authorized_driver):
        header = Header(authorized_driver)
        personal_account_page = PersonalAccountPage(authorized_driver)
        login_page = LoginPage(authorized_driver)

        header.click_personal_account_button()
        personal_account_page.wait_for_personal_account_page()
        personal_account_page.click_exit_btn()
        login_page.wait_for_load_login_page()

        assert authorized_driver.current_url == Urls.LOGIN_PAGE


