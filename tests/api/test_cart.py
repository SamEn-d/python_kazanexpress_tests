import allure
import requests
from allure_commons._allure import step
from python_kazanexpress_tests.api.add_to_cart import add_to_cart
from python_kazanexpress_tests.api.token import api_token


token = {"Authorization": "Bearer " + api_token()}
add_url = 'https://api.kazanexpress.ru/api/cart/add'
remove_url = 'https://api.kazanexpress.ru/api/cart/remove'
skuId = 4800380


@allure.parent_suite('API')
@allure.suite('Корзина')
@allure.title(f"Добавление товара в корзину")
def test_add_to_cart():
	with step('Добавляем товар в корзину'):
		request = requests.post(add_url, json=add_to_cart(skuId), headers=token)
	with step('Проверяем что товар добавился в корзину'):
		assert request.json()['payload'][0]['skuId'] == skuId
	with step('Чистим за собой'):
		requests.post(remove_url, json=add_to_cart(skuId), headers=token)


@allure.parent_suite('API')
@allure.suite('Корзина')
@allure.title(f"Удаление товара из корзины")
def test_remove_to_cart():
	with step('Добавляем товар в корзину'):
		requests.post(add_url, json=add_to_cart(skuId), headers=token)
	with step('Удаляем товар из корзины'):
		request = requests.post(remove_url, json=add_to_cart(skuId), headers=token)
	with step('Проверяем что товар удалился из корзины'):
		assert request.json()['timestamp']
