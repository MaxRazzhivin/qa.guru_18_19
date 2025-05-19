import allure
import pytest
from allure_commons._allure import StepContext
from selene import browser, support
import os
from appium import webdriver
from dotenv import load_dotenv
import config
from utils import attach

@pytest.fixture(scope='function')
def browser_management():
    browser.config.base_url = 'https://www.wikipedia.org'
    browser.config.driver_name = 'chrome'

    browser.config.hold_driver_at_exit = 'true'

    browser.config.window_width = '1024'
    browser.config.window_height = '768'
    browser.config.timeout = float('3.0')

    yield

    attach.add_screenshot(browser)
    browser.quit()
