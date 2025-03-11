import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from helpers import WebdriverFactory
from pages.login_page import LoginPage
from urls import Urls


@pytest.fixture(params = ['firefox'])
def driver(request):
    driver = WebdriverFactory.getWebdriver(request.param)
    yield driver
    driver.quit()

@pytest.fixture
def authorized_driver(driver):
    driver.get(Urls.LOGIN_PAGE)

    login_page = LoginPage(driver)
    login_page.wait_for_load_login_page()
    login_page.set_email()
    login_page.set_password()
    login_page.click_sign_in_btn()

    return driver

