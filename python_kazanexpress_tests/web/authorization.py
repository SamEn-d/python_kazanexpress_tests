import os

import allure
from selene import have, be
from selene.support.shared import browser

from python_kazanexpress_tests.web import test_id

phone = os.getenv('usernameAuth')
password = os.getenv('passwordAuth')

def button():
    with allure.step(f'Нажать кнопку авторизаци'):
        browser.all('.store-action-buttons .action-button')[0].click()


def login_and_password_input():
    with allure.step(f'Вводим логин и пароль'):
        test_id.element_id('input__login').set(phone)
        test_id.element_id('input__password').set(password).press_enter()


def check():
    with allure.step(f'Проверяем авторизацию'):
        test_id.element_id('button__user').click()
        test_id.element_id('text__empty').should(have.text('Здесь пусто :('))
        # browser.element('[data-test-id="button__user"] .visible-sm').click()
        # browser.element('[data-test-id="text__empty"]').should(have.text('Здесь пусто :('))

def by_password():
    if browser.element('.by-password').matching(be.visible):
        with allure.step(f'Переключаем метод авторизации'):
            browser.element('.by-password').click()


def go_to_settings():
    with allure.step(f'Переходим на страницу пользователя'):
        test_id.element_id('button__user').click()

    with allure.step(f'Переходим на страницу Настройки'):
        browser.all('#caregory-content-wrapper .wrapper a')[1].should(have.text('Настройки')).click()

def button_logout_click():
    with allure.step(f'Нажимаем на кнопку Выйти из системы'):
        test_id.element_id('button__logout').click()


def not_authorization():
    with allure.step(f'Проверяем что мы не авторизованы'):
        test_id.element_id('button__user').element('[href="#"]')

def personal_data_change(surname, firstname, lastname, email):
    with allure.step(f'Изменяем фамилию на {surname}'):
        browser.element('[placeholder="Фамилия"]').set(surname)
    with allure.step(f'Изменяем имя на {firstname}'):
        browser.element('[placeholder="Имя"]').set(firstname)
    with allure.step(f'Изменяем отчество на {lastname}'):
        browser.element('[placeholder="Отчество"]').set(lastname)
    with allure.step(f'Изменяем почту на {email}'):
        browser.element('[placeholder="example@mail.ru"]').set(email)
    with allure.step(f'Сохраняем изменения'):
        browser.element('.end-mbs button').click()
    with allure.step(f'Проверям что изменения сохранились'):
        browser.element('.hug.first-sm').should(have.text('Сохранено'))

