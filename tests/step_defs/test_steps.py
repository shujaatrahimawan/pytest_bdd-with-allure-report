import random
import re

from resources.core import *
from tests.step_defs.all_scenarios import *
from pytest_bdd import when, then, given, parsers


@given(parsers.parse('Open Website with "{url}"'))
def open_website_with(browser, url):
    open_url(browser, url)
    browser_maximize(browser)


@given(parsers.parse('Close Website'))
def open_website_with(browser):
    close_browser(browser)


@when(parsers.parse('the user enter "{data}" with "{locator}"'))
def data_phrase(browser, data, locator):
    if data == "null":
        tex = "\ue003\ue003"
    else:
        tex = data.replace("@random", str(random.randint(0, 100)))
    enter_data(browser, locator, tex)


@when(parsers.parse('wait for operation for "{locator}"'))
def operation_wait(browser, locator):
    minutes = 0
    number_regex = re.compile('[1-9]')
    for char in get_text(browser, locator):
        if number_regex.match(str(char)):
            minutes = int(char)
    wait(minutes * 60)


@given(parsers.parse('the user click on "{locator}"'))
@when(parsers.parse('the user click on "{locator}"'))
def data_phrase11(browser, locator):
    click(browser, locator)


@given(parsers.parse('the user select "{data}" on "{locator}"'))
@when(parsers.parse('the user select "{data}" on "{locator}"'))
def data_phrase11(browser, data, locator):
    wait(1)
    select(browser, locator, data)


@given(parsers.parse('the user click on with hover "{locator}"'))
@when(parsers.parse('the user click on with hover "{locator}"'))
def data_phrase23(browser, locator):
    click(browser, locator)


@given(parsers.parse('the user click on with condition "{locator}" with "{condition}"'))
@when(parsers.parse('the user click on with condition "{locator}" with "{condition}"'))
def data_phrase2(browser, locator, condition):
    if condition == "yes":
        click(browser, locator)


@given(parsers.parse('the user click on "{locator} with {data}"'))
@when(parsers.parse('the user click on "{locator} with {data}"'))
def click_with_data(browser, locator, data):
    if bool(data):
        click(browser, locator)


@given(parsers.parse('the user click on "{locator} with value {data}"'))
@when(parsers.parse('the user click on "{locator} with value {data}"'))
def click_with_data(browser, locator, data):
    if bool(data):
        click(browser, locator)


@when(parsers.parse('verify data "{data}" with "{locator}"'))
@then(parsers.parse('verify data "{data}" with "{locator}"'))
def data_phrase(browser, data, locator):
    if data != "null":
        print("["+get_text(browser, locator).replace("warning_amber", "").replace("\n", "")+"]")

        assert data == get_text(browser, locator).replace("warning_amber", "").replace("\n","")


@when(parsers.parse('the user select option "{data}" from "{locator}"'))
def data_phrase(browser, data, locator):
    click(browser, locator)

    click(browser, locator, data)
    # assert False
