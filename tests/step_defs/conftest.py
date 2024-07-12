# Hooks
import allure
from allure_commons.types import AttachmentType
from configuration import *

def pytest_bdd_before_scenario(request, feature, scenario):
    pass


def pytest_bdd_after_scenario(request, feature, scenario):
    pass


def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    pass


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    try:
        global driverHook
        driverHook = step_func_args["browser"]
        if take_passed_Screen_Shots:
            allure.attach(step_func_args["browser"].get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    except:
        print("Cannot Take Screen Shot This step donot have driver arrgument is not found")
    try:
        global default_url 
        default_url = step_func_args["default_url"]
    except:
        print("Driver and default url not found")
    print(f'After Step: {step}')


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    try:
        if take_passed_Screen_Shots:
            allure.attach(step_func_args["browser"].get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    except:
        print("Cannot Take Screen Shot This step donot have driver arrgument is not found")
    try:
        driverHook.get(default_url)
    except:
        print(f'Default URL not Found')
    print(f'Step failed: {step}')

