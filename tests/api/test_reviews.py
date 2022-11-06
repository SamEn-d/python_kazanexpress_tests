import allure
from allure_commons._allure import step

from python_kazanexpress_tests.api.token import api_token
import requests


token = {"Authorization": "Bearer " + api_token()}

@allure.parent_suite('API')
@allure.suite('Товар')
@allure.title(f"Проверка количества отзывов")
def test_reviews():
    with step('Отправляем запрос на количество отзывов'):
        response = requests.get('https://api.kazanexpress.ru/api/product/1950402/reviews', headers=token)
    with step('Проверяем что отзывы отображаются'):
        assert len(response.json()['payload']) >= 13
