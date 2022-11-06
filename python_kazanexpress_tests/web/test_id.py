from selene.support.shared import browser


def element_id(*args):
    if len(args) == 1:
        return browser.element(f'[data-test-id="{args[0]}"]')
    elif len(args) == 2:
        return browser.element(f'[data-test-id="{args[0]}"]').element(f'[data-test-id="{args[1]}"]')
    else:
        print('Error len args = ' + str(len(args)) + 'max len 2')
        assert len(args) <= 2


def all_id(id: str = None):
    return browser.all(f'[data-test-id="{id}"]')