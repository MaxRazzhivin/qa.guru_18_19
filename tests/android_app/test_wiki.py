from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search(android_management):
    with step('Type search'):
        search_element = browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        search_element.click()
        search_input = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        search_input.type("Selene")

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Selene'))

def test_open_aricle(android_management):

    with step('Type search'):
        search_element = browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        search_element.click()
        search_input = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        search_input.type("Selene")

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.first.should(have.text('Selene')).click()