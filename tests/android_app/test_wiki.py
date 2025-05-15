from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search(android_management):

    with step('Skip intro screen'):
        skip_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button'))
        skip_button.click()

    with step('Type search'):
        search_element = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_container"))
        search_element.click()
        search_input = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        search_input.type("Selenium")

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Selenium'))

def test_open_aricle(android_management):

    with step('Skip intro screen'):
        skip_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button'))
        skip_button.click()

    with step('Type search'):
        search_element = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_container"))
        search_element.click()
        search_input = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        search_input.type("Selenium")

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.first.should(have.text('Selenium')).click()


def test_continue_onboarding_screen(android_management):

        with step("Push continue on onboarding screen"):
            continue_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
            continue_button.click()
            assert browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('New ways to explore'))

        with step('Push continue 2nd time'):
            continue_button.click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                            ).should(have.text('Reading lists with sync'))
        with step('Push continue 3rd time'):
            continue_button.click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                            ).should(have.text('Data & Privacy'))
        with step("Push to start"):
            start_onboarding_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button'))
            start_onboarding_button.click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')
                            ).should(have.text('Wikipedia games'))