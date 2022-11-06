import allure
from python_kazanexpress_tests.web import search
from python_kazanexpress_tests.web.browser_web import browser_url, browser_size_standart


@allure.parent_suite('Web')
@allure.suite('Поиск')
@allure.title(f"Поиск товара")
def test_search(setup_browser):
    browser_url()
    browser_size_standart()
    search.search_input_and_press_enter('эпл 12 512 золотой')

    search.result('Apple', '512')
