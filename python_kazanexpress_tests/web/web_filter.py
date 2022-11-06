import allure
from selene import have, be
from selene.support.shared import browser

from python_kazanexpress_tests.web import test_id


def go_to_filter(name):
    with allure.step(f'Переходим в категорию {name}'):
        browser.all('.children-category-item .children-title').element_by(have.text(name)).click()
    with allure.step(f'Переходим в категорию {name}'):
        test_id.element_id('text__title').with_(timeout=10).should(be.visible).should(have.text(name))
        # browser.element('[data-test-id="text__title"]').with_(timeout=10).should(be.visible).should(have.text(name))
    with allure.step(f'Проверям что категория {name} выбран как фильтр'):
        browser.all('.filter-checkbox--label').element_by(have.text(name)).element('.is-checked')

def select_filter_by_text(name):
    with allure.step(f'Выбираем категорию {name} в фильтрах'):
        browser.all('.filter-checkbox--label').with_().element_by(have.text(name)).click()

def builtin_memory(memory):
    with allure.step(f'Выбираем фильтр Встроенная память'):
        test_id.all_id('block__filter').element_by(have.text('Встроенная память, Гб')).with_(timeout=10).should(be.visible).click()
    with allure.step(f'Выбираем фильтр {memory}'):
        browser.all('.filter-checkbox--label').element_by(have.text(f'{memory} Гб')).click()
    with allure.step(f'Проверям что Встроенная память {memory} выбран как фильтр'):
        browser.all('.filter-checkbox--label').element_by(have.text(memory)).element('.is-checked')

def filter_assert(name, memory):
    with allure.step(f'Проверям что товары содержат '):
        test_id.all_id('text__product-name').element_by(have.text(name))
        test_id.all_id('text__product-name').element_by(have.text(memory))
        # browser.all('[data-test-id="text__product-name"]').element_by(have.text(name))
        # browser.all('[data-test-id="text__product-name"]').element_by(have.text(memory))

def reset_all():
    with allure.step(f'Нажимаем очистить все фильтры'):
        browser.element('.noselect.clear-all').click()
    with allure.step(f'Проверям что все фильтры пусты'):
        test_id.element_id('button__clear-price').should(be.hidden)

def reser_first():
    with allure.step(f'Нажимаем очистить один фильтр'):
        test_id.element_id('button__clear-price').click()
    with allure.step(f'Проверяем что фильтры отсутствуют'):
        test_id.element_id('button__clear-price').should(be.hidden)
        # browser.element('[data-test-id="button__clear-price"]').should(be.hidden)






