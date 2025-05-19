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
        attach.add_video(session_id, config.bstack_userName, config.bstack_accessKey)