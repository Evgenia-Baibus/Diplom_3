from time import sleep

import allure
from selenium import webdriver
import requests
from faker import Faker

from data import IngredientData
from urls import ApiUrls


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == 'firefox':
            return webdriver.Firefox()
        elif browser_name == 'chrome':
            return webdriver.Chrome()
        else:
            raise ValueError(f'Unknown browser {browser_name}')


class UserDataGeneration:

    @staticmethod
    def generate_valid_user_data():
        fake = Faker()

        email = fake.email()
        password = fake.password()
        name = fake.name()

        return {
            "email": email,
            "password": password,
            "name": name
        }

class UserData:
    valid_data = UserDataGeneration.generate_valid_user_data()

class User:

    @staticmethod
    def sign_up_and_get_user_data():
        data = UserData.valid_data
        response = requests.post(ApiUrls.SIGN_UP, data=data)
        return {"email": data["email"], "password": data["password"], "accessToken": response.json()["accessToken"]}


    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        response = requests.delete(ApiUrls.DELETE_USER, headers=headers)
        return response

    @staticmethod
    def create_order(access_token, ingredients):
        headers = {"Authorization": access_token}

        data = {
            "ingredients": ingredients
        }

        response = requests.post(ApiUrls.CREATE_ORDER, headers = headers, data = data)
        return response.json()['order']['number']

    @staticmethod
    @allure.step('Сделать заказ')
    def make_order(login_data):
        User.create_order(login_data['accessToken'], [IngredientData.ingredient_id])
        sleep(1)  # give ui time to update
