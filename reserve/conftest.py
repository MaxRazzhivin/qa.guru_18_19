import allure
import pytest
from allure_commons._allure import StepContext
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os
from appium import webdriver
from dotenv import load_dotenv
import config
from utils import attach


def general_settings(options):
    browser.config.driver = webdriver.Remote(
        'http://127.0.0.1:4723',
        options=options)
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(context=StepContext)

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function')
def android_management():

    if config.context == 'bstack':
        options = UiAutomator2Options().load_capabilities({
            # Specify device and os_version for testing
            "platformName": "android",
            "platformVersion": "15.0",
             "deviceName": "emulator-5554",

            "app": "/Users/maxnovo/Downloads/app-alpha-universal-release.apk",
            "appWaitActivity": 'org.wikipedia.*'

            # Add your caps here
        })

    general_settings(options)

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    with allure.step('teardown app session'):
        browser.quit()