import allure
from python_kazanexpress_tests.web import favorites
from python_kazanexpress_tests.web.browser_web import browser_url, browser_size_standart


@allure.parent_suite('Web')
@allure.suite('Избранное')
@allure.title(f"Добавление товара в избранное")
def test_add_favorites(setup_browser):
    browser_url()
    browser_size_standart()

    favorites.add_to_favorites()
    favorites.go_to_favorites()
    favorites.favorites_assert()


@allure.parent_suite('Web')
@allure.suite('Избранное')
@allure.title(f"Удаление товара из избранного")
def test_remove_favorites(setup_browser):
    browser_url()
    browser_size_standart()

    favorites.add_to_favorites()
    favorites.go_to_favorites()

    favorites.remove_favorites()
