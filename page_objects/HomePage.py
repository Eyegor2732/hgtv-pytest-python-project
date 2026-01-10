from selenium.webdriver.common.by import By
from utilities.SharedClass import xpath_contains_text_ci


class HomePage:

    email_entry = (By.CSS_SELECTOR, 'input[type="email"]')
    begin_entry_button = (By.ID, 'xCheckUser')
    next_button_small = \
        (By.XPATH, xpath_contains_text_ci("//form[@id='xSecondaryForm']//span", "Next"))
    enter_button = (By.XPATH, "//form[@id='xSecondaryForm']//span[contains(text(),'Enter')]")
    enter_again_button = (By.ID, "reentry-link")
    enter_again_discovery_button = (By.CLASS_NAME, "editorial-link-no-style")
    enter_again_food_button = (By.CSS_SELECTOR, "[class*='sweeps-enter-again']")
    already_entered_message = (By.XPATH, '//*[@class="xCopy xContentBody"]//b')
    already_entered_message_small = (By.ID, "xInviteModalHeader")
    agree_button = (By.ID, "ltp-submit-btn")
