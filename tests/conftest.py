import pytest
from selenium import webdriver
from helpers import WebdriverFactory
from urls import Urls


@pytest.fixture(params = ['firefox'])
def driver(request):
    driver = WebdriverFactory.getWebdriver(request.param)
    yield driver
    driver.quit()

@pytest.fixture
def authorized_driver(driver):
    driver.get(Urls.)

    WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignInPageLocators.sign_in_btn))
    driver.find_element(*SignInPageLocators.name_input).send_keys(SignInData.email)
    driver.find_element(*SignInPageLocators.password_input).send_keys(SignInData.password)
    driver.find_element(*SignInPageLocators.sign_in_btn).click()

    return driver

