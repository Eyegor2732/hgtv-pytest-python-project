import math
import time
import logging
from selenium.webdriver import ActionChains
from page_objects.HomePage import HomePage


def get_logger():
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)  # file handler object
    logger.setLevel(logging.DEBUG)
    return logger


class HomePageActions(HomePage):

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(*HomePage.email_entry).send_keys(email)

    def begin_entry(self):
        self.driver.find_element(*HomePage.begin_entry_button).click()

    def enter(self):
        self.driver.find_element(*HomePage.enter_button).click()

    def enter_again_button_element(self):
        return self.driver.find_element(*HomePage.enter_again_button)

    def enter_again(self):
        self.driver.find_element(*HomePage.enter_again_button).click()

    def already_entered_element(self):
        return self.driver.find_element(*HomePage.already_entered_message)

    def already_entered(self):
        return self.already_entered_element().text.startswith("Sorry!")

    #   ==============================================

    def entry(self, emails, frames, sites):
        logger = get_logger()
        action = ActionChains(self.driver)

        count = 0
        allowed_entries = len(emails) * 2

        while count < allowed_entries:
            host = self.driver.current_url.split(".")[1].lower()
            if host == "hgtv":
                frame = frames[0]  # "ngxFrame277066"
                count += 1
            else:  # if driver.title.split(".")[1].lower() == "foodnetwork":
                frame = frames[1]  # "ngxFrame277068"
                count += 1
            logger.debug("Host: " + host)
            logger.debug("URL: " + self.driver.current_url)
            logger.debug("Frame: " + frame)
            logger.debug("Count: " + str(count))
            user = emails[math.floor((count - 1) / 2)]
            logger.debug("User: " + user)

            time.sleep(1)
            self.driver.switch_to.frame(frame)
            time.sleep(1)

            self.enter_email(user)
            time.sleep(1)
            self.begin_entry()
            time.sleep(1)

            if self.already_entered_element().is_displayed() and self.already_entered():
                if host == "hgtv":
                    self.driver.get(sites[1])
                else:
                    self.driver.get(sites[0])
                logger.info("You already entered for this sweepstake today.")
                continue
            time.sleep(1)

            self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
            time.sleep(1)

            self.enter()
            time.sleep(1)
            self.driver.execute_script("window.scrollBy(document.body.scrollHeight, 0);")
            time.sleep(1)

            assert self.enter_again_button_element().is_displayed()
            logger.info("Entry - " + str(count) + " - is successful.")

            if count < allowed_entries:
                action.move_to_element(self.enter_again_button_element()).perform()
                self.enter_again()
                time.sleep(1)

                self.driver.switch_to.default_content()
                time.sleep(1)

                handles = self.driver.window_handles
                child = handles[-1]
                # self.driver.close()
                self.driver.switch_to.window(child)
            else:
                logger.info(f"All today\'s {count} entries have been performed. See ya tomorrow.")

            time.sleep(2)
