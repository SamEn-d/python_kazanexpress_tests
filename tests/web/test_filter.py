import allure
from python_kazanexpress_tests.web import web_filter
from python_kazanexpress_tests.web.browser_web import browser_url, browser_size_standart
from python_kazanexpress_tests.web.cart import more_click


@allure.parent_suite('Web')
@allure.suite('Фильтры')
@allure.title(f"Фильтрация товаров")
def test_category_filter(setup_browser):
    browser_url()
    browser_size_standart()

    more_click()
    web_filter.go_to_filter('Смартфоны')

    web_filter.select_filter_by_text('Apple')
    web_filter.builtin_memory('512')

    web_filter.filter_assert('Apple', '512')


@allure.parent_suite('Web')
@allure.suite('Фильтры')
@allure.title(f"Очистка всех фильтров")
def test_reset_all_category_filter(setup_browser):
    browser_url()
    browser_size_standart()

    more_click()
    web_filter.go_to_filter('Смартфоны')

    web_filter.select_filter_by_text('Apple')
    web_filter.builtin_memory('512')

    web_filter.reset_all()


@allure.parent_suite('Web')
@allure.suite('Фильтры')
@allure.title(f"Очистка одного фильтра")
def test_reset_one_category_filter(setup_browser):
    browser_url()
    browser_size_standart()

    more_click()
    web_filter.go_to_filter('Смартфоны')

    web_filter.select_filter_by_text('Apple')

    web_filter.reser_first()
