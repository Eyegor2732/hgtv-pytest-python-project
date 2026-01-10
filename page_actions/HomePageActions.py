import math
import datetime
import tldextract
from selenium.webdriver import ActionChains
from page_objects.HomePage import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


def is_sweep_small(sweep):
    small = ["newyear", "bite", "big"]
    return sweep in small


def is_sweep_large(sweep):
    large = ["oasis", "dream", "smart"]
    return sweep in large


def is_sweep_single(sweep):
    single = []
    return sweep in single


class HomePageActions(HomePage):

    def __init__(self, driver):
        self.driver = driver

    def assert_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
        except TimeoutException:
            assert False, f"Expected element {locator} was not visible"

    def switch_to_new_window(
            self,
            close_current: bool = True,
            timeout: int = 10,
    ):
        self.driver.switch_to.default_content()

        current = self.driver.current_window_handle

        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
        )

        new_window = next(
            h for h in self.driver.window_handles if h != current
        )

        if close_current:
            self.driver.switch_to.window(current)
            self.driver.close()

        self.driver.switch_to.window(new_window)

    def scroll_to_and_click(self, locator, timeout=10):
        el = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable(locator)
        ).click()

    def wait_and_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable(locator)
        ).click()

    def wait_and_send_keys(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable(locator)
        ).send_keys(text)

    def enter_email(self, email):
        self.wait_and_send_keys(HomePage.email_entry, email)

    def begin_entry(self):
        self.wait_and_click(HomePage.begin_entry_button)

    def next_small(self):
        self.wait_and_click(HomePage.next_button_small)

    def enter(self):
        self.scroll_to_and_click(HomePage.enter_button)

    def enter_button_element(self):
        return self.driver.find_element(*HomePage.enter_button)

    def enter_again_button_element(self):
        return self.driver.find_element(*HomePage.enter_again_button)

    def enter_again_discovery_button_element(self):
        return self.driver.find_element(*HomePage.enter_again_discovery_button)

    def enter_again_food_button_element(self):
        return self.driver.find_element(*HomePage.enter_again_food_button)

    def enter_again(self):
        self.wait_and_click(HomePage.enter_again_button)

    def enter_again_discovery(self):
        self.wait_and_click(HomePage.enter_again_discovery_button)

    def enter_again_food(self):
        self.wait_and_click(HomePage.enter_again_food_button)

    def already_entered_element(self):
        return self.driver.find_element(*HomePage.already_entered_message)

    def already_entered_small_element(self):
        return self.driver.find_element(*HomePage.already_entered_message_small)

    def already_entered(self):
        return "sorry" in self.already_entered_element().text.lower()

    def already_entered_small(self):
        return "sorry" in self.already_entered_small_element().text.lower()

    def agree(self):
        try:
            WebDriverWait(self.driver, 5).until(
                ec.element_to_be_clickable(HomePage.agree_button)
            ).click()
        except TimeoutException:
            pass  # button not present → nothing to do

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
                self.agree()
                domain = tldextract.extract(self.driver.current_url).domain
                if domain == original_domain:
                    frame = frames[0]
                    count += 1
                else:
                    frame = frames[1]
                    count += 1

                user = emails[math.floor((count - 1) / 2)]

                WebDriverWait(self.driver, 10).until(
                    ec.frame_to_be_available_and_switch_to_it(frame)
                )

                self.enter_email(user)
                self.begin_entry()

                try:
                    if is_sweep_small(sweep):
                        WebDriverWait(self.driver, 3).until(
                            ec.visibility_of_element_located(HomePage.already_entered_message_small)
                        )
                        already_entered = self.already_entered_small()

                    elif is_sweep_large(sweep):
                        WebDriverWait(self.driver, 3).until(
                            ec.visibility_of_element_located(HomePage.already_entered_message)
                        )
                        already_entered = self.already_entered()

                    else:
                        already_entered = False

                    if already_entered:
                        next_site = sites[1] if domain == original_domain else sites[0]
                        self.driver.get(next_site)

                        logger.info(
                            f" {sweep} - {user} - You already entered for {domain} sweepstake today."
                        )
                        continue

                except TimeoutException:
                    # "already entered" message did not appear → proceed normally
                    pass

                self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

                if domain == original_domain and is_sweep_small(sweep):  # and not ?
                    self.next_small()
                self.enter()

                WebDriverWait(self.driver, 10).until(
                    lambda d: d.current_url.endswith("thanks")
                )

                self.driver.switch_to.default_content()

                logger.info(f" {sweep} - {user} - {domain} - Entry - {count} - is successful.")

                if count < allowed_entries:
                    if domain == "discovery" and sweep == "central":
                        action.move_to_element(self.enter_again_discovery_button_element()).perform()
                        self.enter_again_discovery()
                    elif domain == 'food':
                        action.move_to_element(self.enter_again_food_button_element()).perform()
                        self.enter_again_food()
                    else:
                        action.move_to_element(self.enter_again_button_element()).perform()
                        self.enter_again()

                    self.switch_to_new_window(True)
                else:
                    logger.info(f" All today\'s {count} entries for {sweep.upper()} have been performed")

        else:
            logger.info(f" Sweepstake {sweep.upper()} is expired")

    # def entry_single(self, emails, frames, sites, sweep, date_time, home, logger):
    #     self.driver.get(home)
    #
    #     date_format = '%Y-%m-%d %H:%M:%S'
    #     date_obj = datetime.datetime.strptime(date_time, date_format)
    #
    #     if datetime.datetime.now() <= date_obj:
    #         # action = ActionChains(self.driver)
    #         count = 0
    #         allowed_entries = len(emails)
    #         #original_domain = tldextract.extract(self.driver.current_url).domain
    #
    #         while count < allowed_entries:
    #             domain = tldextract.extract(self.driver.current_url).domain
    #             count += 1
    #             frame = frames[0]
    #             user = emails[count - 1]
    #
    #             time.sleep(1)
    #             self.driver.switch_to.frame(frame)
    #             time.sleep(1)
    #
    #             self.enter_email(user)
    #             time.sleep(1)
    #             self.begin_entry()
    #             time.sleep(1)
    #
    #             try:
    #                 time.sleep(1)
    #                 if is_sweep_single(sweep) and self.already_entered_small_element().is_displayed() and self.already_entered_small():
    #                     self.driver.get(sites[0])
    #                     logger.info(f" {sweep} - {user} - You already entered for {domain} sweepstake today.")
    #                     continue
    #                 time.sleep(1)
    #             except NoSuchElementException:
    #                 pass
    #
    #             self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    #             time.sleep(1)
    #             self.enter()
    #             time.sleep(2)
    #             self.driver.execute_script("window.scrollBy(document.body.scrollHeight, 0);")
    #             time.sleep(2)
    #
    #             logger.info(f" {sweep} - {user} - {domain} - Entry - {count} - is successful.")
    #
    #             if count < allowed_entries:
    #                 self.driver.get(home)
    #                 time.sleep(1)
    #             else:
    #                 logger.info(f" All today\'s {count} entries for {sweep} have been performed")
    #
    #             time.sleep(2)
    #     else:
    #         logger.info(f" Sweepstake {sweep} is expired")
