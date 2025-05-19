import os

import pytest
from allure_commons._allure import StepContext
from selene import browser, support
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    browser.config.base_url = os.getenv('base_url', 'https://www.wikipedia.org')
    browser.config.driver_name = os.getenv('driver_name', 'chrome')
    browser.config._wait_decorator = support._logging.wait_with(context=StepContext)

    browser.config.hold_driver_at_exit = 'true'

    browser.config.window_width = os. getenv('window_width', '1900')
    browser.config.window_height = os. getenv('window_height', '1200')
    browser.config.timeout = float(os.getenv("timeout", '3.0'))

    yield


    attach.add_screenshot(browser)
    browser.quit()
