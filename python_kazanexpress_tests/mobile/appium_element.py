import selene
from allure_commons._allure import step
from selene import have, be
from selene.support.shared import browser
from python_kazanexpress_tests.mobile import appium_by
from typing import Optional

#Сделать для других
def by_id(id):# -> selene:
    return browser.element(appium_by.id(id))

def by_class(classname):
    return browser.element(appium_by.class_name(classname))

#Сделать для других
def appium_all_by_id(id) -> selene:
    return browser.all(appium_by.id(id))


def navigation_search_click():
    with step('Пеоеходим в "Поиск" с футере'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/navigation_search')).click()

def banner_close():
    with step('Закрываем баннер с акцией'):
        pass
        # browser.all(appium_by.class_name('android.view.View'))[2].with_(timeout=10).click()

def category_title_name_search_click(name):
    with step(f'Поиск категории {name}'):
        browser.all(appium_by.id('com.kazanexpress.ke_app:id/category_title')).element_by(have.exact_text(name)).click()

def search_product_in_category_for_number(number: int = 0):
    with step(f'Нажимаем на товар номер {number}'):
        browser.all(appium_by.id('com.kazanexpress.ke_app:id/image'))[number].click()

def add_to_cart_button_in_product_click():
    with step(f'Нажимаем на кнопку добавить в корзину'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/add_to_cart_button')).click()

def go_to_cart_button_in_product_click():
    with step(f'Нажимаем на кнопку "Перейти"'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/go_to_cart_screen_button')).click()

def buy_button_in_cart_click():
    with step(f'Нажимаем на кнопку "Оформить"'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/buy_button')).click()

def select_deliver_for_adress():
    with step(f'Выбираем способ получения "Курьером до двери"'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/courier_delivery_title')).click()

def swipe_down(number: int = 0):
    with step(f'Пролистываем вниз на {number}'):
        browser.driver.swipe(0, number, 0, 0, 1000)

def search_in_id_hint_click(text: str = None):
    with step(f'Нажимаем на {text}'):
        browser.all(appium_by.id('com.kazanexpress.ke_app:id/hint')).element_by(have.text(text)).click()

def adress_in_cart_type(adress: str = 'Адоратского'):
    with step(f'Вводим адрес {adress}'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/search_address')).set(adress)

def click_first_adress_title():
    with step(f'Выбор первого варианта предложенного в списке'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/result_recycler')).all(appium_by.id('com.kazanexpress.ke_app:id/title'))[0].click()

def set_data_input(number: int = None, data: str = None):
    return browser.all(appium_by.id('com.kazanexpress.ke_app:id/edit_text'))[number].click().set(data)

def select_in_popup_first():
    with step('Выбор первого варианта предложенного в списке'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/item_button')).click()

def pay_by_card_click():
    with step('Выбораем оплату картой'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/pay_by_card')).click()

def check_text_in_header(text):
    with step(f'Проверяем наличие текста {text}'):
        browser.all(appium_by.class_name('android.widget.TextView')).element_by(have.text(text))

def click_in_city_name():
    with step(f'Нажимаем на пустом поле'):
        browser.element(appium_by.class_name('android.view.View')).click()

def set_adress(number, data):
    with step(f'Заполняем поле адреса {data}'):
        set_data_input(number, data)

def set_personal_data(number, data):
    with step(f'Заполняем данные покупателя {data}'):
        set_data_input(number, data)

def favorite_in_category_click():
    with step('Нажимаем на кнопку в избранное в категории'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/favorite')).click()

def favorite_empty():
    with step('Проверяем что избранные товары отсутствуют'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/empty_view')).should(be.visible)

def favorite_in_product_click():
    with step('Нажимаем на кнопку "В избранное"'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/product_favorite_button')).click()

def click_button_back():
    with step('Нажимаем на кнопку назад'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/product_back_button')).click()

def product_orders_amount():
    browser.element(appium_by.id('com.kazanexpress.ke_app:id/product_orders_amount')).should(be.visible)

def navigation_favorite_click():
    with step('Переходим в "Желания"'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/navigation_favorite')).click()

def favorite_product_visible():
    with step('Проверка наличия товара в избранном'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/image_container')).should(be.visible)

def click_first_product_homepage():
    with step('Нажимаем на 1 товар на главной странице'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/itemImageNew')).click()

class Search_in_title_element():
    def __init__(self):
        self.title = browser.all(appium_by.id('com.kazanexpress.ke_app:id/title'))

    def text_click(self, text):
        with step(f'Клик на страницу {text}'):
            self.title.element_by(have.text(text)).click()

    def have_text(self, text, number: Optional[int] = 0):
        with step(f'Проверка на странице наличия {text}'):
            self.title[number].should(have.text(text))



def filter_in_category_button():
    with step(f'Нажимаем на кнопку фильтров'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/filter')).with_(timeout=10).should(be.visible).click()

def select_in_filter_text(text):
    with step(f'Поиск элемента {text} в списке'):
        browser.all(appium_by.id('com.kazanexpress.ke_app:id/name')).element_by(have.text(text)).click()


def filter_apply():
    with step(f'Нажимаем на кнопку Применить\Показать'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/apply')).click()

def navigation_profile_click():
    with step('Переходим на страницу "Кабинет"'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/navigation_profile')).click()

def sign_in_button_click():
    with step('Нажимаем на кнопку Войти'):
        browser.element(appium_by.id('com.kazanexpress.ke_app:id/sign_in_button')).click()

def set_phone_number_text(phone):
    with step(f'Вводим номер телефона {phone}'):
        by_id('com.kazanexpress.ke_app:id/phone_number_text').set(phone)

def set_password_input_text(password):
    with step(f'Вводим пароль {password}'):
        by_id('com.kazanexpress.ke_app:id/password_input_edit_text').set(password)

def click_search_button():
    with step('Нажимаем на поиск'):
        by_id('com.kazanexpress.ke_app:id/search').click()

def input_search_request(request):
    with step(f'Вводим поисковый запрос request'):
        by_class('android.widget.EditText').set(request)

def search_field_click():
    with step('Нажать на кнопку поиска'):
        by_id('com.kazanexpress.ke_app:id/search_field').click()

def profile_edit_data(surname, name, middle):
    with step(f'Изменяем персональные данные на {surname} {name} {middle}'):
        by_id('com.kazanexpress.ke_app:id/profile_text_view').click()
        by_id('com.kazanexpress.ke_app:id/order_surname_field').click().set(surname)
        by_id('com.kazanexpress.ke_app:id/order_name_field').click().set(name)
        by_id('com.kazanexpress.ke_app:id/patronymic_name_field').click().set(middle)
        by_id('com.kazanexpress.ke_app:id/parent_layout').click()
        by_id('com.kazanexpress.ke_app:id/submit_button').click()

def username_contains(name):
    with step(f'Проверка имени {name}'):
        by_id('com.kazanexpress.ke_app:id/user_name').should(have.text(name))





