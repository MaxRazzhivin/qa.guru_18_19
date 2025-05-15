import allure
import pytest
from allure_commons._allure import StepContext
from selene import browser, support
import os
from appium import webdriver
from dotenv import load_dotenv
import config
from utils import attach


def general_settings(options):
    browser.config.driver = webdriver.Remote(config.remote_url, options=options)
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(context=StepContext)

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function')
def android_management():
    options = config.driver_options()

    with allure.step("init app session"):
        general_settings(options)

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    if config.runs_on_bstack:
        session_id = browser.config.driver.session_id
        attach.add_video(session_id, config.USERNAME, config.PASSWORD)


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
