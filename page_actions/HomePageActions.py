import math
import time
import datetime
import tldextract
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from page_objects.HomePage import HomePage


def is_sweep_small(sweep):
    small = ["10k", "sweets", "central", "fresh", "healthy", "yes", "curb", "groc", "spring", "outside"]
    return sweep in small

def is_sweep_large(sweep):
    large = ["oasis", "dream", "smart"]
    return sweep in large

def is_sweep_single(sweep):
    single = ["champ", "valspar"]
    return sweep in single

class HomePageActions(HomePage):

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(*HomePage.email_entry).send_keys(email)

    def begin_entry(self):
        self.driver.find_element(*HomePage.begin_entry_button).click()

    def next_small(self):
        self.driver.find_element(*HomePage.next_button_small).click()

    def enter(self):
        self.driver.find_element(*HomePage.enter_button).click()

    def enter_button_element(self):
        return self.driver.find_element(*HomePage.enter_button)

    def enter_again_button_element(self):
        return self.driver.find_element(*HomePage.enter_again_button)

    def enter_again_discovery_button_element(self):
        return self.driver.find_element(*HomePage.enter_again_discovery_button)

    def enter_again(self):
        self.driver.find_element(*HomePage.enter_again_button).click()

    def enter_again_discovery(self):
        self.driver.find_element(*HomePage.enter_again_discovery_button).click()

    def already_entered_element(self):
        return self.driver.find_element(*HomePage.already_entered_message)

    def already_entered_small_element(self):
        return self.driver.find_element(*HomePage.already_entered_message_small)

    def already_entered(self):
        return self.already_entered_element().text.startswith("Sorry!")

    def already_entered_small(self):
        return self.already_entered_small_element().text.startswith("We're Sorry")

    #   ==============================================

    def entry_double(self, emails, frames, sites, sweep, date_time, home, logger):
        self.driver.get(home)

        date_format = '%Y-%m-%d %H:%M:%S'
        date_obj = datetime.datetime.strptime(date_time, date_format)

        if datetime.datetime.now() <= date_obj:
            action = ActionChains(self.driver)
            count = 0
            allowed_entries = len(emails) * 2
            original_domain = tldextract.extract(self.driver.current_url).domain

            while count < allowed_entries:
                domain = tldextract.extract(self.driver.current_url).domain
                if domain == original_domain:
                    frame = frames[0]
                    count += 1
                else:
                    frame = frames[1]
                    count += 1

                user = emails[math.floor((count - 1) / 2)]

                time.sleep(1)
                self.driver.switch_to.frame(frame)
                time.sleep(1)

                self.enter_email(user)
                time.sleep(1)
                self.begin_entry()
                time.sleep(1)

                try:
                    time.sleep(1)
                    if (is_sweep_small(sweep) and self.already_entered_small_element().is_displayed() and self.already_entered_small()) or \
                            (is_sweep_large(sweep) and self.already_entered_element().is_displayed() and self.already_entered()):
                        if domain == original_domain:
                            self.driver.get(sites[1])
                        else:
                            self.driver.get(sites[0])
                        logger.info(f" {sweep} - {user} - You already entered for {domain} sweepstake today.")
                        continue
                    time.sleep(1)
                except NoSuchElementException:
                    pass

                #self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
                #time.sleep(1)

                if domain == original_domain and is_sweep_small(sweep): # and not ?
                    self.next_small()
                time.sleep(1)
                self.enter()
                time.sleep(1)
                self.driver.execute_script("window.scrollBy(document.body.scrollHeight, 0);")
                time.sleep(2)

                if domain == "discovery" and sweep == "central":
                    assert self.enter_again_discovery_button_element().is_displayed()
                else:
                    assert self.enter_again_button_element().is_displayed()

                logger.info(f" {sweep} - {user} - {domain} - Entry - {count} - is successful.")

                if count < allowed_entries:
                    if domain == "discovery" and sweep == "central":
                        action.move_to_element(self.enter_again_discovery_button_element()).perform()
                        self.enter_again_discovery()
                    else:
                        action.move_to_element(self.enter_again_button_element()).perform()
                        self.enter_again()
                    time.sleep(1)

                    self.driver.switch_to.default_content()
                    time.sleep(1)

                    handles = self.driver.window_handles
                    child = handles[-1]
                    self.driver.close()
                    self.driver.switch_to.window(child)
                else:
                    logger.info(f" All today\'s {count} entries for {sweep} have been performed")

                time.sleep(2)
        else:
            logger.info(f" Sweepstake {sweep} is expired")


    def entry_single(self, emails, frames, sites, sweep, date_time, home, logger):
        self.driver.get(home)

        date_format = '%Y-%m-%d %H:%M:%S'
        date_obj = datetime.datetime.strptime(date_time, date_format)

        if datetime.datetime.now() <= date_obj:
            action = ActionChains(self.driver)
            count = 0
            allowed_entries = len(emails)
            #original_domain = tldextract.extract(self.driver.current_url).domain

            while count < allowed_entries:
                domain = tldextract.extract(self.driver.current_url).domain
                count += 1
                frame = frames[0]
                user = emails[count - 1]

                time.sleep(1)
                self.driver.switch_to.frame(frame)
                time.sleep(1)

                self.enter_email(user)
                time.sleep(1)
                self.begin_entry()
                time.sleep(1)

                try:
                    time.sleep(1)
                    if is_sweep_single(sweep) and self.already_entered_small_element().is_displayed() and self.already_entered_small():
                        self.driver.get(sites[0])
                        logger.info(f" {sweep} - {user} - You already entered for {domain} sweepstake today.")
                        continue
                    time.sleep(1)
                except NoSuchElementException:
                    pass

                self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
                time.sleep(1)
                self.enter()
                time.sleep(1)
                self.driver.execute_script("window.scrollBy(document.body.scrollHeight, 0);")
                time.sleep(2)

                logger.info(f" {sweep} - {user} - {domain} - Entry - {count} - is successful.")

                if count < allowed_entries:
                    self.driver.get(home)
                    time.sleep(1)
                else:
                    logger.info(f" All today\'s {count} entries for {sweep} have been performed")

                time.sleep(2)
        else:
            logger.info(f" Sweepstake {sweep} is expired")
