import os

import allure
import requests
from allure_commons._allure import step

from python_kazanexpress_tests.api.personal_data import personal_data
from python_kazanexpress_tests.api.token import api_token

token = {"Authorization": "Bearer " + api_token()}
firstname = 'Евгения'
lastname = 'Иванова'
email = 'aw@wth.su'
phone = os.getenv('APIPhone')
APIAuthURL = os.getenv('APIAuthURL')

@allure.parent_suite('API')
@allure.suite('Личный кабинет')
@allure.title(f"Изменение персональных данных")
def test_personal_data_change():
	personal_data_change = personal_data(email=email, firstname=firstname, lastname=lastname, phone=phone)
	with step('Отпрввляем запрос на изменение персональных данных'):
		response = requests.post(APIAuthURL, json=personal_data_change, headers=token)
	with step('Проверяем изменение'):
		assert response.json()['timestamp']