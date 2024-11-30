from selenium.webdriver.common.by import By


class HomePage:

    email_entry = (By.CSS_SELECTOR, 'input[type="email"]')
    begin_entry_button = (By.ID, 'xCheckUser')
    next_button_small = (By.XPATH, "//form[@id='xSecondaryForm']//span[contains(text(),'Next')]")
    enter_button = (By.XPATH, "//form[@id='xSecondaryForm']//span[contains(text(),'Enter')]")
    enter_again_button = (By.ID, "reentry-link")
    enter_again_discovery_button = (By.CLASS_NAME, "editorial-link-no-style")
    already_entered_message = (By.XPATH, '//*[@class="xCopy xContentBody"]//b')
    already_entered_message_small = (By.ID, "xInviteModalHeader")
