import os
from appium.options.android import UiAutomator2Options
from pydantic_settings import BaseSettings
import utils
from dotenv import load_dotenv

class Config(BaseSettings):
    base_url: str = 'https://www.wikipedia.org'
    driver_name: str = 'chrome'
    hold_driver_at_exit: bool = False
    window_width: int = 1900
    window_height: int = 1200
    timeout: float = 3.0


load_dotenv()
config = Config()

bstack_userName = os.getenv('bstack_userName')
bstack_accessKey = os.getenv('bstack_accessKey')
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
                "userName": bstack_userName,  # Ваш логин в Browserstack
                "accessKey": bstack_accessKey  # Ваш ключ доступа в Browserstack
            })

    return options