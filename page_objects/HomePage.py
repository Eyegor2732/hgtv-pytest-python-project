from selenium.webdriver.common.by import By


class HomePage:

    email_entry = (By.CSS_SELECTOR, 'input[type="email"]')
    begin_entry_button = (By.ID, 'xCheckUser')
    enter_button = (By.XPATH, "//form[@id='xSecondaryForm']//span[contains(text(),'Enter')]")
    enter_again_button = (By.ID, "reentry-link")
    already_entered_message = (By.XPATH, '//*[@class="xCopy xContentBody"]//b')
