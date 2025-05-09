import allure
from allure_commons.types import AttachmentType
import requests

# Скриншоты
def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

def add_xml(browser):
    xml_dump = browser.driver.page_source
    allure.attach(body=xml_dump, 
                  name='XML screen', 
                  attachment_type=allure.attachment_type.XML, extension='.xml')


def add_video(session_id, login, access_key):
    browserstack_session = requests.get(
        url=f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(login, access_key)
    ).json()
    video_url = browserstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )