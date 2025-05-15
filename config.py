import os

from appium.options.android import UiAutomator2Options

import utils
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('BSTACK_USERNAME')
PASSWORD = os.getenv('BSTACK_ACCESSKEY')
# context = os.getenv('context', 'bstack')
# run_on_bstack = os.getenv('run_on_bstack', 'false').lower() == 'true'
remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')
deviceName = os.getenv('deviceName')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
app = os.getenv('app', './app-alpha-universal-release.apk')
runs_on_bstack = app.startswith('bs://')
if runs_on_bstack:
    remote_url = 'http://hub.browserstack.com/wd/hub'

def driver_options():
    options = UiAutomator2Options()

    if deviceName:
        options.set_capability('deviceName', deviceName)

    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)

    options.set_capability('app', (
        app if (app.startswith('/') or runs_on_bstack)
        else utils.file.abs_path_from_project(app)
    ))

    if runs_on_bstack:
        options.set_capability('platformVersion', '9.0')
        options.set_capability(
            'bstack:options', {
                "projectName": "First Python project",  # Название проекта которое будет отображаться в Browserstack
                "buildName": "browserstack-build-1",  # Название сборки которое будет отображаться в Browserstack
                "sessionName": "BStack first_test",  # Название сессии которое будет отображаться в Browserstack
                "userName": USERNAME,  # Ваш логин в Browserstack
                "accessKey": PASSWORD  # Ваш ключ доступа в Browserstack
            })

    return options