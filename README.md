# Diplom_3

# Автотесты UI для сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site)

Сервис [Stellar Burgers](https://stellarburgers.nomoreparties.site) - это сайт для заказа бургеров.

## Структура проекта 

* [tests](tests) - директория с тестами
* [tests](tests/test_basic_functionality.py) - файл с проверками списка заказов юзера
* [tests](tests/test_order_list.py) - файл с проверками совершения заказа
* [test](tests/test_personal_account.py) - файл с проверками логина юзера
* [test](tests/test_recovery_password.py) - файл с проверками регистрации юзера
* [pages](pages) - директория с Pages Objects
* [pages](pages/base_page.py) - файл с базовыми функциями, характерными для всех страниц
* [pages](pages/forgot_password_page.py) - файл с Pages Objects страницы ввода почты для восстановления пароля
* [pages](pages/header.py) - файл с Pages Objects хедера сайта
* [pages](pages/ingredient_details_pop_up.py) - файл с Pages Objects всплывающего окна деталей ингредиента
* [pages](pages/login_page.py) - файл с Pages Objects страницы авторизации
* [pages](pages/main_page.py) - файл с Pages Objects главной страницы
* [pages](pages/order_details_pop_up.py) - файл с Pages Objects всплывающего окна деталей заказа
* [pages](pages/personal_account_page.py) - файл с Pages Objects личного аккаунта
* [pages](pages/reset_password_page.py) - файл с Pages Objects страницы восстановления пароля
* [data.py](data.py) - файл с данными ингредиентов
* [urls.py](urls.py) - файл с эндроинтами
* [allure_results](allure_results) - каталог с отчетом тестирования
* [conftest.py](tests/conftest.py) - файл с фикстурами
* [helpers.py](helpers.py) - файл с вспомогательными методами и классами

## Запуск автотестов

**Установка зависимостей**
```bash
pip install -r requirements.txt
```

Для запуска тестов выполнить:
```bash
pytest tests --alluredir=allure_results
```

Для генерации репорта выполнить:
```bash
allure generate --single-file allure_results -o allure_report
```
