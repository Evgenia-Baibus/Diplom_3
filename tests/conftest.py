import pytest

from helpers import WebdriverFactory, User
from pages.login_page import LoginPage
from urls import Urls


@pytest.fixture(params = ['firefox'])
def driver(request):
    driver = WebdriverFactory.get_webdriver(request.param)
    yield driver
    driver.quit()

@pytest.fixture
def authorized_driver(driver, login_data):
    driver.get(Urls.LOGIN_PAGE)

    login_page = LoginPage(driver)
    login_page.login(login_data)

    return driver

@pytest.fixture
def login_data():
    user_data = User.sign_up_and_get_user_data()
    yield user_data
    User.delete_user(user_data['accessToken'])




#authorized_user_with_orders

