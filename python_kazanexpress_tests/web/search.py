import allure
from selene import be, have
from selene.support.shared import browser
from typing import Optional

from python_kazanexpress_tests.web import test_id


def search_input_and_press_enter(request):
    with allure.step(f'Вводим поисковый запрос {request} и производим поиск'):
        test_id.element_id('input__search').set(request).press_enter()
        # browser.element('[data-test-id="input__search"]').set(request).press_enter()
    with allure.step(f'Проверям что поиск произошел по запросу {request} '):
        test_id.element_id('text__title').with_(timeout=10).should(be.visible).should(have.text(request))
        # browser.element('[data-test-id="text__title"]').with_(timeout=10).should(be.visible).should(have.text(request))

def result(text, text2: Optional[str] = None):
    test_id.all_id('text__product-name')[0].should(have.text(text))
    # browser.all('data-test-id="text__product-name"')[0].should(have.text(text))
    if text2 != None:
        test_id.all_id('text__product-name')[0].should(have.text(text2))
