import os
from typing import Optional
from selene.support.shared import browser

URL = os.getenv('URL')

def browser_url(url: Optional[str] = ''):
    browser.open(URL + url)

def browser_size_standart():
    browser.driver.set_window_size(width=1920, height=1080)