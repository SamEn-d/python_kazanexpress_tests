import allure
from selene import be
from selene.support.shared import browser

from python_kazanexpress_tests.web import test_id


def add_to_favorites():
    with allure.step(f'Добавляем товар в изрбанное'):
        test_id.element_id('item__product-card', 'button__add-to-favorites').click()
        # browser.all('[data-test-id="item__product-card"]')[0].element('[data-test-id="button__add-to-favorites"]').click()
    with allure.step(f'Проверям что товар отображается как избранный'):
        test_id.element_id('item__product-card', 'button__add-to-favorites').element('.liked')
        # browser.all('[data-test-id="item__product-card"]')[0].element('[data-test-id="button__add-to-favorites"].liked')

def go_to_favorites():
    with allure.step(f'Переходим в изрбанное'):
        test_id.element_id('button__wishes').click()
        # browser.element('[data-test-id="button__wishes"]').click()
    with allure.step(f'Проверяем что находимся в избранном'):
        browser.element('#wishes-header h1').with_(timeout=10).should(be.visible)

def favorites_assert():
    with allure.step(f'Проверяем товар присутствует в избранных'):
        test_id.element_id('list__products').element('.list-complete-item')

def remove_favorites():
    with allure.step(f'Нажимаем удалить из избранного'):
        test_id.element_id('button__add-to-favorites').click()
    with allure.step(f'Проверяем что избранные товары отсутствуют'):
        test_id.element_id('block__empty-page').with_(timeout=10).should(be.visible)





