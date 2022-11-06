import pytest
from appium import webdriver
from selene.support.shared import browser
from python_kazanexpress_tests.mobile import config_mobile

@pytest.fixture(scope='function')
def mobile_browser():
    browser.config.driver = webdriver.Remote(
        config_mobile.settings.remote_url, options=config_mobile.settings.driver_options
    )

    yield browser
    browser.quit()