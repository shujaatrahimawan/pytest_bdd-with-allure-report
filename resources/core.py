import time
import pytest
import os

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from resources.utilities import *


@pytest.fixture(scope="module")
def browser():
    match executable_browser.replace(" ", "").lower():
        case 'chrome':
            project_path = "" if use_chrome_absolute_path else os.getcwd().replace("\\", "/")
            print("the path is : "+project_path)
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--user-agent=>9]7Td-(Selenium)-'x8`ydPdjW-(Cloudways)")
            chrome_options.add_experimental_option("useAutomationExtension", False)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            if headless:
                chrome_options.add_argument("headless")
                chrome_options.add_argument("disable-gpu")
            if use_chrome_executable_path:
                print("The executable path is : " + project_path + chrome_driver_path)
                driver = webdriver.Chrome(executable_path=project_path + chrome_driver_path, options=chrome_options)
            else:
                chrome_service = ChromeService(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            driver.implicitly_wait(10)
        case 'firefox':
            project_path = "" if use_firefox_absolute_path else os.getcwd().replace("\\", "/")
            firefox_options = FireFoxOptions()

            if headless:
                firefox_options.add_argument("headless")
                firefox_options.add_argument("disable-gpu")
            if use_firefox_executable_path:
                driver = webdriver.Firefox(executable_path=project_path + firefox_driver_path, options=firefox_options)
            else:
                fire_fox_service = FireFoxService(GeckoDriverManager().install())
                driver = webdriver.Firefox(service=fire_fox_service, options=firefox_options)
            driver.implicitly_wait(10)
            pass
        case 'edge':
            project_path = "" if use_edge_absolute_path else os.getcwd().replace("\\", "/")
            capabilities = webdriver.DesiredCapabilities().EDGE
            capabilities['acceptSslCerts'] = True
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            edge_options.add_experimental_option("useAutomationExtension", False)
            edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            if headless:
                edge_options.add_argument("headless")
                edge_options.add_argument("disable-gpu")
            if use_edge_executable_path:
                driver = webdriver.Edge(executable_path=project_path + edge_driver_path, options=edge_options,
                                        capabilities=capabilities)
            else:
                edge_service = EdgeService(EdgeChromiumDriverManager().install())
                driver = webdriver.Edge(service=edge_service, options=edge_options, capabilities=capabilities)
            driver.implicitly_wait(10)
            pass
        case 'safari':
            project_path = "" if use_chrome_absolute_path else os.getcwd().replace("\\", "/")
            safari_options = SafariOptions()
            if headless:
                safari_options.add_argument("headless")
                safari_options.add_argument("disable-gpu")
            if use_safari_executable_path:
                driver = webdriver.Chrome(executable_path=project_path + safari_driver_path, options=safari_options)
            else:
                chrome_service = SafariService()  # not implemented yet
                driver = webdriver.Chrome(service=chrome_service, options=safari_options)
            driver.implicitly_wait(10)
        case default:
            project_path = "" if use_chrome_absolute_path else os.getcwd().replace("\\", "/")
            chrome_options = ChromeOptions()
            chrome_options.add_experimental_option("useAutomationExtension", False)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            if headless:
                chrome_options.add_argument("headless")
                chrome_options.add_argument("disable-gpu")
            if use_chrome_executable_path:
                driver = webdriver.Chrome(executable_path=project_path + chrome_driver_path, options=chrome_options)
            else:
                chrome_service = ChromeService(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            driver.implicitly_wait(10)

    return driver


def close_browser(browser):
    browser.close()


def wait(seconds):
    time.sleep(seconds)


def click(browser, locator, key='locator', count=0):
    try:
        get_element(browser, locator, key).click()
    except Exception as e:
        if count == retry_attempt:
            raise Exception('Error is : ' + str(e))
        else:
            wait(1)
            click(browser, locator, key, count + 1)


def enter_data(browser, locator, data, key='locator', by_char=False, count=0):
    try:
        if by_char:
            for char_item in data:
                get_element(browser, locator, key).send_keys(char_item)
        else:
            get_element(browser, locator, key).send_keys(Keys.CONTROL + 'a' + Keys.NULL,data)
    except Exception as e:
        if count == retry_attempt:
            raise Exception('Error is : ' + str(e))
        else:
            wait(1)
            enter_data(browser, locator, data, key, by_char, count + 1)


def select(browser, locator, value, key='locator', count=0):
    try:
        dropdown = Select(get_element(browser, locator, key))
        # dropdown.select_by_index(3)
        dropdown.select_by_value(value)
        # dropdown.select_by_visible_text('Python')
    except Exception as e:
        if count == retry_attempt:
            raise Exception('Error is : ' + str(e))
        else:
            wait(1)
            select(browser, locator, value, key, count + 1)


def get_text(browser, locator, key='locator', count=0):
    result = ''
    try:
        result = get_element(browser, locator, key).text
    except Exception as e:
        if count == retry_attempt:
            raise Exception('Error is : ' + str(e))
        else:
            wait(1)
            get_text(browser, locator, key, count + 1)
    return result


def open_url(browser, url):
    browser.get(url)
    if default_full_screen_browser:
        browser.fullscreen_window()


def browser_minimize(browser):
    browser.minimize_window()


def browser_maximize(browser):
    browser.maximize_window()


def js_executor(browser, script, elem=None):
    browser.execute_script(script, elem)


def go_back(browser):
    browser.back()


def go_forward(browser):
    browser.go_forward()


def get_current_url(browser):
    return browser.current_url


def get_title(browser):
    wait(1)
    return browser.title


def switch_tab(browser, tab_name_or_index):
    current_tab = browser.current_window_handle
    if str(type(tab_name_or_index)) == "<class 'str'>":
        for index in range(len(browser.window_handles)):
            wait(1)
            if current_tab != browser.window_handles[index]:
                browser.switch_to.window(browser.window_handles[
                                                                       index])
            if get_title(browser) == tab_name_or_index:
                break
    else:
        browser.switch_to.window(browser.window_handles[tab_name_or_index])


def new_tab(browser,url, switch_tab_name_or_index):
    js_executor(browser, "window.open('"+url+"');")
    if switch_tab_name_or_index != "":
        switch_tab(browser, switch_tab_name_or_index)


def close_tab(browser, switch_tab_name_or_index):
    browser.close()
    if switch_tab_name_or_index != "":
        switch_tab(browser, switch_tab_name_or_index)
