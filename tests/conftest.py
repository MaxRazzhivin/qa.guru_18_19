import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from selenium import webdriver
from dotenv import load_dotenv

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def android_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",  # Название проекта которое будет отображаться в Browserstack
            "buildName": "browserstack-build-1",  # Название сборки которое будет отображаться в Browserstack
            "sessionName": "BStack third_test",  # Название сессии которое будет отображаться в Browserstack

            # Set your access credentials
            "userName": os.getenv('USERNAME'),  # Ваш логин в Browserstack
            "accessKey": os.getenv("ACCESSKEY")  # Ваш ключ доступа в Browserstack
        }

        # Add your caps here
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub",
                              options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
