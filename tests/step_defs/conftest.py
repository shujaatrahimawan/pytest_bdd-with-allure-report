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
    if take_passed_Screen_Shots:
        allure.attach(step_func_args["browser"].get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    print(f'After Step: {step}')


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    allure.attach(step_func_args["browser"].get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    print(f'Step failed: {step}')

