import os

import allure
import requests
from allure_commons._allure import step

from python_kazanexpress_tests.api.favorites import favorites_body
from python_kazanexpress_tests.api.token import api_token

APIURL = os.getenv('APIURL')

token = {"Authorization": "Bearer " + api_token()}
url_favorites_add = APIURL + 'api/favorites/add'
url_favorites_remove = APIURL + 'api/favorites/remove'
favorites_id = 126041


@allure.parent_suite('API')
@allure.suite('Избранные')
@allure.title(f"Добавление товара в избранные")
def test_add_favorites():
    with step('Добавляем товар в избранное'):
        response = requests.post(url_favorites_add, json=favorites_body(favorites_id), headers=token)
    with step('Проверям что товар присутствует в избранном'):
        assert response.json()['timestamp']
    with step('Чистим за собой'):
        requests.post(url_favorites_remove, json=favorites_body(favorites_id), headers=token)


@allure.parent_suite('API')
@allure.suite('Избранные')
@allure.title(f"Добавление товара в избранные")
def test_remove_favorites():
    with step('Добавляем товар в избранное'):
        requests.post(url_favorites_add, json=favorites_body(favorites_id), headers=token)
    with step('Удаляем товар из избранного'):
        response = requests.post(url_favorites_remove, json=favorites_body(favorites_id), headers=token)
    with step('Проверям что избранные товары отсутствуют'):
        assert response.json()['timestamp']
