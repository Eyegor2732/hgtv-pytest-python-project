from selenium.webdriver.common.by import By
from utilities.SharedClass import xpath_contains_text_ci


class HomePage:
    Locator = tuple[str, str]

    email_entry: Locator = (By.CSS_SELECTOR, 'input[type="email"]')
    begin_entry_button: Locator = (By.ID, 'xCheckUser')
    next_button_small: Locator = \
        (By.XPATH, xpath_contains_text_ci("//form[@id='xSecondaryForm']//span", "Next"))
    enter_button: Locator = (By.XPATH, "//form[@id='xSecondaryForm']//span[contains(text(),'Enter')]")
    enter_again_button: Locator = (By.ID, "reentry-link")
    enter_again_discovery_button: Locator = (By.CLASS_NAME, "editorial-link-no-style")
    enter_again_food_button: Locator = (By.CSS_SELECTOR, "[class*='sweeps-enter-again']")
    already_entered_message: Locator = (By.XPATH, '//*[@class="xCopy xContentBody"]//b')
    already_entered_message_small: Locator = (By.ID, "xInviteModalHeader")
    agree_button: Locator = (By.ID, "ltp-submit-btn")
