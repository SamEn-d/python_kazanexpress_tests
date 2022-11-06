import os
import allure
from allure_commons._allure import step
from python_kazanexpress_tests.mobile import appium_element
from python_kazanexpress_tests.mobile.browser_config import mobile_browser

phone = os.getenv('usernameAuth')
password = os.getenv('passwordAuth')
name = 'Имя'


@allure.parent_suite('Приложение')
@allure.suite('Авторизация')
@allure.title(f"Проверка авторизации")
def test_authorization(mobile_browser):
    appium_element.banner_close()

    appium_element.navigation_profile_click()
    appium_element.sign_in_button_click()
    appium_element.set_phone_number_text(phone)
    appium_element.set_password_input_text(password)
    appium_element.sign_in_button_click()

    appium_element.navigation_profile_click()
    appium_element.check_text_in_header('Личный кабинет')


@allure.parent_suite('Приложение')
@allure.suite('Поиск')
@allure.title(f"Поиска в категории")
def test_search_navigation_bottom(mobile_browser):
    appium_element.banner_close()
    appium_element.navigation_search_click()

    appium_element.category_title_name_search_click('Электроника')
    appium_element.category_title_name_search_click('Смартфоны и телефоны')
    appium_element.category_title_name_search_click('Смартфоны')

    appium_element.search_field_click()
    appium_element.input_search_request('эпл 12 512 золотой')
    appium_element.click_search_button()

    appium_element.Search_in_title_element().have_text('Apple')
    appium_element.Search_in_title_element().have_text('512')


@allure.parent_suite('Приложение')
@allure.suite('Поиск')
@allure.title(f"Поиск с главной страницы")
def test_search_top(mobile_browser):
    appium_element.banner_close()

    with step('Нажимаем на кнопку поиска на главной'):
        appium_element.by_class('android.widget.AutoCompleteTextView').click()

    appium_element.input_search_request('эпл 12 512 золотой')

    appium_element.click_search_button()

    appium_element.Search_in_title_element().have_text('Apple')
    appium_element.Search_in_title_element().have_text('512')


@allure.parent_suite('Приложение')
@allure.suite('Авторизация')
@allure.title(f"Изменение персональных данных")
def test_personal_data(mobile_browser):
    appium_element.banner_close()

    appium_element.navigation_profile_click()
    appium_element.sign_in_button_click()
    appium_element.set_phone_number_text(phone)
    appium_element.set_password_input_text(password)
    appium_element.sign_in_button_click()

    appium_element.navigation_profile_click()
    appium_element.profile_edit_data('Фамилия', name, 'Отчество')

    appium_element.check_text_in_header('Личный кабинет')
    appium_element.username_contains(name)


@allure.parent_suite('Приложение')
@allure.suite('Поиск')
@allure.title(f"Фильтрации товаров в категории")
def test_filter_in_category(mobile_browser):
    appium_element.banner_close()
    appium_element.navigation_search_click()

    appium_element.category_title_name_search_click('Электроника')
    appium_element.category_title_name_search_click('Смартфоны и телефоны')
    appium_element.category_title_name_search_click('Смартфоны')

    appium_element.filter_in_category_button()

    appium_element.Search_in_title_element().text_click('Бренд')
    appium_element.select_in_filter_text('Apple')
    appium_element.filter_apply()

    appium_element.Search_in_title_element().text_click('Встроенная память, Гб')
    appium_element.select_in_filter_text('512 Гб')
    appium_element.filter_apply()

    appium_element.Search_in_title_element().text_click('Число SIM-карт')
    appium_element.select_in_filter_text('1')
    appium_element.filter_apply()

    appium_element.filter_apply()
    appium_element.Search_in_title_element().have_text('Apple')


@allure.parent_suite('Приложение')
@allure.suite('Избранное')
@allure.title(f"Добавления товара в избранное")
def test_add_favorite(mobile_browser):
    appium_element.banner_close()

    appium_element.click_first_product_homepage()
    appium_element.product_orders_amount()

    appium_element.favorite_in_product_click()
    appium_element.click_button_back()

    appium_element.navigation_favorite_click()

    appium_element.favorite_product_visible()


@allure.parent_suite('Приложение')
@allure.suite('Избранное')
@allure.title(f"Удаления товара из избранного")
def test_remove_favorite(mobile_browser):
    appium_element.banner_close()
    appium_element.click_first_product_homepage()
    appium_element.product_orders_amount()

    appium_element.favorite_in_product_click()
    appium_element.click_button_back()

    appium_element.navigation_favorite_click()

    appium_element.favorite_in_category_click()

    appium_element.favorite_empty()


@allure.parent_suite('Приложение')
@allure.suite('Корзина')
@allure.title(f"Оформление заказа")
def test_add_to_cart(mobile_browser):

    appium_element.banner_close()
    appium_element.navigation_search_click()

    appium_element.category_title_name_search_click('Электроника')
    appium_element.category_title_name_search_click('Смартфоны и телефоны')
    appium_element.category_title_name_search_click('Смартфоны')

    appium_element.search_product_in_category_for_number(0)

    appium_element.add_to_cart_button_in_product_click()
    appium_element.go_to_cart_button_in_product_click()

    appium_element.buy_button_in_cart_click()

    appium_element.select_deliver_for_adress()

    appium_element.swipe_down(1500)

    appium_element.search_in_id_hint_click('Улица, дом')

    appium_element.adress_in_cart_type()

    appium_element.click_first_adress_title()
    appium_element.click_first_adress_title()

    appium_element.set_adress(0, '1')
    appium_element.set_adress(1, '1')
    appium_element.set_adress(2, '1')
    appium_element.set_adress(3, '1')

    appium_element.click_in_city_name()

    appium_element.swipe_down(1400)

    appium_element.search_in_id_hint_click('Дата')
    appium_element.select_in_popup_first()

    appium_element.search_in_id_hint_click('Время')
    appium_element.select_in_popup_first()

    appium_element.swipe_down(400)
    appium_element.set_personal_data(0, 'Фамилия')
    appium_element.set_personal_data(1, 'Имя')
    appium_element.set_personal_data(2, '9009009000')
    appium_element.set_personal_data(3, 'w@wth.su')

    appium_element.click_in_city_name()
    appium_element.pay_by_card_click()

    appium_element.check_text_in_header('Вход')
