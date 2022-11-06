from typing import Optional

from selene.support.shared import browser


def browser_url(url: Optional[str] = ''):
    browser.open('https://kazanexpress.ru/' + url )

def browser_size_standart():
    browser.driver.set_window_size(width=1920, height=1080)