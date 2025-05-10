import logging

import allure
import pytest
from allure_commons._allure import StepContext
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os
from appium import webdriver
from dotenv import load_dotenv
from utils import attach


def general_settings(options):
    browser.config.driver = webdriver.Remote('http://hub.browserstack.com/wd/hub', options=options)
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(context=StepContext)

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

def get_creeds():
    load_dotenv()
    USERNAME = os.getenv('BSTACK_USERNAME')
    PASSWORD = os.getenv('BSTACK_ACCESSKEY')
    print(USERNAME)
    print(PASSWORD)
    logging.info(USERNAME)
    logging.info(PASSWORD)
    return USERNAME, PASSWORD

@pytest.fixture(scope='function')
def android_management():
    creeds = get_creeds()
    print(creeds)
    USERNAME = creeds[0]
    PASSWORD = creeds[1]

    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",  # Название проекта которое будет отображаться в Browserstack
            "buildName": "browserstack-build-1",  # Название сборки которое будет отображаться в Browserstack
            "sessionName": "BStack first_test",  # Название сессии которое будет отображаться в Browserstack

            # Set your access credentials
            "userName": USERNAME,  # Ваш логин в Browserstack
            "accessKey": PASSWORD  # Ваш ключ доступа в Browserstack
        }

        # Add your caps here
    })

    print(USERNAME)
    print(PASSWORD)

    general_settings(options)

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    session_id = browser.config.driver.session_id
    attach.add_video(session_id, USERNAME, PASSWORD)

    with allure.step('teardown app session'):
        browser.quit()


@pytest.fixture(scope='function')
def browser_management():
    browser.config.base_url = 'https://www.wikipedia.org'

    browser.config.driver_name = 'chrome'

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # browser.config.driver_options = chrome_options

    browser.config.hold_driver_at_exit = 'true'

    browser.config.window_width = '1024'
    browser.config.window_height = '768'
    browser.config.timeout = float('3.0')

    yield

    attach.add_screenshot(browser)
    browser.quit()
