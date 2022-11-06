import allure
from python_kazanexpress_tests.web.browser_web import browser_size_standart, browser_url
from python_kazanexpress_tests.web import authorization


@allure.parent_suite('Web')
@allure.suite('Авторизация')
@allure.title(f"Вход в систему")
def test_authorization(setup_browser): #setup_browser
    browser_url()
    browser_size_standart()

    authorization.button()
    authorization.by_password()

    authorization.login_and_password_input()

    authorization.check()


@allure.parent_suite('Web')
@allure.suite('Авторизация')
@allure.title(f"Выход из системы")
def test_logout(setup_browser):
    browser_url()
    browser_size_standart()

    authorization.button()
    authorization.by_password()

    authorization.login_and_password_input()

    authorization.go_to_settings()
    authorization.button_logout_click()
    authorization.not_authorization()
