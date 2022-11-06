from selene.support.shared import browser

from python_kazanexpress_tests.utils.path_to_directory import filename
import pickle

def save():
    pickle.dump(browser.driver.get_cookies(), open(filename() + "/cookies.pkl", 'wb'))


def load():
    print(filename())
    browser.driver.delete_all_cookies()
    for cookie in pickle.load(open(filename() + "/cookies.pkl", "rb")):
        # if cookie['name'] == 'user_session':
        browser.driver.add_cookie(cookie)
        print(cookie)
















