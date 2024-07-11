from selenium.webdriver import ActionChains
from tests.PageFactory import locator as loc

from configuration import *

def get_locator_vars(locator, key='locator'):
    return vars(loc)[locator][key]


def get_element(dri, locator, key='locator'):
    a = ActionChains(dri)
    m = dri.find_element(get_locator_vars(locator, 'type'), get_locator_vars(locator, key))
    a.move_to_element(m).perform()
    return m


def get_elements(dri, locator, key='locator'):
    return dri.find_elements(get_locator_vars(locator, 'type'), get_locator_vars(locator, key))