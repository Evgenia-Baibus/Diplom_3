from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from urls import Urls
from pages.login_page import LoginPage


class TestRecoveryPassword:

    def test_success_transition_to_forgot_password_page(self, driver):
        driver.get(Urls.LOGIN_PAGE)

        login_page = LoginPage(driver)
        login_page.click_recovery_password_btn()

        assert driver.current_url == Urls.FORGOT_PASSWORD

    def test_success_transition_to_reset_password_page(self, driver, login_data):
        driver.get(Urls.FORGOT_PASSWORD)

        recovery_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        recovery_password_page.set_email(login_data["email"])
        recovery_password_page.click_recovery_btn()
        reset_password_page.wait_for_load_reset_password_page()

        assert driver.current_url == Urls.RESET_PASSWORD

    def test_password_field_selection_when_click_on_password_hide_icon(self, driver, login_data):
        driver.get(Urls.FORGOT_PASSWORD)

        recovery_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        recovery_password_page.set_email(login_data["email"])
        recovery_password_page.click_recovery_btn()
        reset_password_page.wait_for_load_reset_password_page()
        reset_password_page.click_password_hide_icon()

        assert reset_password_page.is_password_field_active()
