import pytest
from allure_commons._allure import StepContext
from pydantic_settings import BaseSettings
from selene import browser, support
from config import config
from utils import attach

@pytest.fixture(scope='function', autouse=True)
def browser_management():

    browser.config.base_url = config.base_url
    browser.config.driver_name = config.driver_name
    browser.config._wait_decorator = support._logging.wait_with(context=StepContext)

    browser.config.hold_driver_at_exit = config.hold_driver_at_exit

    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.timeout = config.timeout

    yield

    attach.add_screenshot(browser)
    browser.quit()
