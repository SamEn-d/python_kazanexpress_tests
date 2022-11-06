import allure
from selene import be, have
from selene.support.shared import browser
from python_kazanexpress_tests.web import test_id


def add_to_cart_first_product():
    with allure.step(f'Добавляем первый товар на главной странице в корзину'):
        test_id.element_id('item__product-card', 'button__add-to-cart').click()

def popup_product_select():
    if browser.element('.slideUp').with_(timeout=10).should(be.visible):
        with allure.step(f'Выбираем характеристики продукта'):
            test_id.element_id('tooltip__sku-not-chosen').with_(timeout=10).should(be.visible).element('.radio-item.regular:not(.disabled)').click()

def add_cart():
        with allure.step(f'Нажимаем добавить в корзину'):
            # test_id.element_id('block__info-container', 'button__add-cart').click()
            test_id.element_id('button__add-cart').click()

def go_to_cart():
    with allure.step(f'Нажимаем Перейти в корзину'):
        test_id.element_id('button__go-to-cart').click()

def check_checkout():
    with allure.step(f'Проверяем что перешли в корзину'):
        browser.element('h1.slightly').with_(timeout=10).should(be.visible).should(have.text('Ваша корзина'))

def checkout():
    with allure.step(f'Нажимаем Перейти к оформлению'):
        test_id.element_id('button__go-checkout').click()

def select_pvz():
    with allure.step(f'Выбор пункта самовывоза'):
        test_id.element_id('radio-button__select-pvz').element('div').click()

def fill_personal_data(lastname: str = None, firstname: str = None, phone: int = None, email: str = None):
    with allure.step(f'Вводим фамилию: {lastname}'):
        test_id.element_id('input__lastname').set(lastname)
    with allure.step(f'Вводим имя: {firstname}'):
        test_id.element_id('input__firstname').set(firstname)
    with allure.step(f'Вводим телефон: {phone}'):
        test_id.element_id('input__phone').set(phone)
    with allure.step(f'Вводим почту: {email}'):
        test_id.element_id('input__email').set(email)


def pay_card_click():
    with allure.step(f'Нажимаем подтвердить и оплатить'):
        test_id.element_id('button__pay-card').click()

def assert_popup_registration():
    with allure.step(f'Проверям что появилось окно "Введите номер телефона"'):
        browser.element('.slideUp .title').should(have.text('Введите номер телефона'))

def more_click():
    with allure.step(f'Нажимаем Ещё в шапке'):
        browser.element('.bottom-header-wrapper .more').click()

def categories_title_search_and_click(title: str = None):
    with allure.step(f'Нажимаем по категории {title}'):
        browser.all('.parent-category-item .title').element_by(have.text(title)).click()

def select_first_product_in_category():
    with allure.step(f'Выбираем первый товар категории'):
        browser.element('[data-test-id="list__products"]').element('a').click()

def add_to_cart_in_category():
    with allure.step(f'Добавляем товар в корзину'):
        test_id.element_id('button__add-to-cart').with_(timeout=10).should(be.visible).click()
        # browser.element('[data-test-id="button__add-to-cart"]').with_(timeout=10).should(be.visible).click()

def products_in_cart_count():
    with allure.step(f'Проверяем что количество товаров в корзине 1'):
        test_id.element_id('button__cart').element('.products-in-cart-count').should(have.text('1'))

def header_hover():
    with allure.step(f'Наводим мышку на корзину'):
        test_id.element_id('button__cart').hover()
    # browser.element('[data-test-id="button__cart"]').hover()

def remove_in_header():
    with allure.step(f'Удаляем товар из корзины'):
        browser.element('[cart-preview]').should(be.visible).element('.delete').click()

def remove_in_header_assert():
    with allure.step(f'Проверяем что товар удалился'):
        browser.element('.products-in-cart-count').should(be.hidden)

def remove_product_in_cart():
    with allure.step(f'Удаляем товар из корзины'):
        test_id.element_id('button__delete-from-cart').click()
        # browser.element('[data-test-id="button__delete-from-cart"]').click()

def remove_product_in_cart_assert():
    with allure.step(f'Проверям что корзина пуста'):
        test_id.element_id('block__empty-page').should(be.visible)
    # browser.element('[data-test-id="block__empty-page"]').should(be.visible)

