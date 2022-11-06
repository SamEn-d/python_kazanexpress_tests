import os
import pytest
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

import os.path
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from python_kazanexpress_tests import attach

# from renlife_b2b_test.path_to_directory import path_to_download_resources
# from renlife_b2b_test import attach
# from renlife_b2b_test.path_to_directory import filename

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

DEFAULT_BROWSER_VERSION = '100.0'
DEFAULT_BROWSER_VERSION = 'chrome'

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

DEFAULT_WEB_BROWSER_VERSION = '100'
DEFAULT_WEB_BROWSER = 'chrome'

@pytest.fixture(scope='function')
def setup_browser(request):
    # web_browser = request.config.getoption('--browser')
    # web_browser = web_browser if web_browser != "" else DEFAULT_WEB_BROWSER
    #
    # web_browser_version = request.config.getoption('--browser_version')
    # web_browser_version = web_browser_version if web_browser_version != "" else DEFAULT_WEB_BROWSER_VERSION

    browser.config.hold_browser_open = True
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": '100',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_browser = os.getenv('BROWSER')
    driver = webdriver.Remote(
        command_executor = f"{selenoid_browser}",
        options=options
    )
    browser.config.driver = driver

    yield browser
    attach.add_pagesource(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    browser.quit()

def abs_path_from_project(relative_path: str):
    import python_kazanexpress_tests
    from pathlib import Path

    return (
        Path(python_kazanexpress_tests.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )