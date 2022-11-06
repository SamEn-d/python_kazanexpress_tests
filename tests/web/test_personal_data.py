import allure
from python_kazanexpress_tests.web import authorization
from python_kazanexpress_tests.web.browser_web import browser_url, browser_size_standart


@allure.parent_suite('Web')
@allure.suite('Персональные данные')
@allure.title(f"Изменение персональных данных")
def test_change_personal_data(setup_browser):
    browser_url()
    browser_size_standart()

    authorization.button()
    authorization.by_password()

    authorization.login_and_password_input()

    authorization.check()
    authorization.go_to_settings()

    authorization.personal_data_change('Фамилия', 'Имя', 'Отчество', 'w@wth.su')
