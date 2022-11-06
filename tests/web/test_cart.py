import allure
from python_kazanexpress_tests.web import cart
from python_kazanexpress_tests.web.browser_web import browser_url, browser_size_standart


@allure.parent_suite('Web')
@allure.suite('Корзина')
@allure.title(f"Оформление заказа")
def test_order(setup_browser):
    browser_url()
    browser_size_standart()

    cart.add_to_cart_first_product()
    cart.popup_product_select()
    cart.add_cart()

    cart.go_to_cart()
    cart.check_checkout()
    cart.checkout()

    cart.select_pvz()
    cart.fill_personal_data('Фамилия', 'Имя', 9999999999, 'w@wth.su')
    cart.pay_card_click()

    cart.assert_popup_registration()


@allure.parent_suite('Web')
@allure.suite('Корзина')
@allure.title(f"Удаление товара из корзины")
def test_remove_in_cart(setup_browser):
    browser_url()
    browser_size_standart()

    cart.more_click()
    cart.categories_title_search_and_click('Товары для взрослых')
    cart.add_to_cart_in_category()
    cart.go_to_cart()
    cart.check_checkout()

    cart.remove_product_in_cart()
    cart.remove_product_in_cart_assert()


@allure.parent_suite('Web')
@allure.suite('Корзина')
@allure.title(f"Удаление товара из корзины в шапке")
def test_remove_in_cart_header(setup_browser):
    browser_url()
    browser_size_standart()

    cart.more_click()
    cart.categories_title_search_and_click('Товары для взрослых')

    cart.add_to_cart_in_category()
    cart.header_hover()
    cart.remove_in_header()
    cart.remove_in_header_assert()


@allure.parent_suite('Web')
@allure.suite('Корзина')
@allure.title(f"Добавление товара в корзину")
def test_add_to_cart_in_product(setup_browser):
    browser_url()
    browser_size_standart()

    cart.more_click()
    cart.categories_title_search_and_click('Товары для взрослых')

    cart.select_first_product_in_category()
    cart.add_cart()
    cart.products_in_cart_count()


@allure.parent_suite('Web')
@allure.suite('Корзина')
@allure.title(f"Добавление товара в корзину из категории")
def test_add_to_cart_in_category(setup_browser):
    browser_url()
    browser_size_standart()

    cart.more_click()
    cart.categories_title_search_and_click('Товары для взрослых')

    cart.add_to_cart_in_category()
    cart.products_in_cart_count()
