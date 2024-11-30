import pytest
from page_actions.HomePageActions import HomePageActions
from utilities.BaseClass import BaseClass


class TestEntry(BaseClass):

    @pytest.mark.usefixtures("data_load_sweets")
    def test_entry_sweets(self, data_load, data_load_sweets):
        users = data_load[0]
        iframes = data_load_sweets[0]
        urls = data_load_sweets[1]
        sweep = data_load_sweets[2]
        end_date = data_load_sweets[3]
        home = data_load_sweets[4]

        logger = self.get_logger()
        logger.info(f" Test {sweep} Started")

        home_page_actions = HomePageActions(self.driver)
        home_page_actions.entry(users, iframes, urls, sweep, end_date, home, logger)

        logger.info(" Test Sweets Ended")

    @pytest.mark.usefixtures("data_load_10k")
    def test_entry_10k(self, data_load, data_load_10k):
        users = data_load[0]
        iframes = data_load_10k[0]
        urls = data_load_10k[1]
        sweep = data_load_10k[2]
        end_date = data_load_10k[3]
        home = data_load_10k[4]

        logger = self.get_logger()
        logger.info(f" Test {sweep} Started")

        home_page_actions = HomePageActions(self.driver)
        home_page_actions.entry(users, iframes, urls, sweep, end_date, home, logger)

        logger.info(f" Test {sweep} Ended")

    @pytest.mark.usefixtures("data_load_central")
    def test_entry_central(self, data_load, data_load_central):
        users = data_load[0]
        iframes = data_load_central[0]
        urls = data_load_central[1]
        sweep = data_load_central[2]
        end_date = data_load_central[3]
        home = data_load_central[4]

        logger = self.get_logger()
        logger.info(f" Test {sweep} Started")

        home_page_actions = HomePageActions(self.driver)
        home_page_actions.entry(users, iframes, urls, sweep, end_date, home, logger)

        logger.info(f" Test {sweep} Ended")

    @pytest.mark.usefixtures("data_load_oasis")
    def test_entry_oasis(self, data_load, data_load_oasis):
        users = data_load[0]
        iframes = data_load_oasis[0]
        urls = data_load_oasis[1]
        sweep = data_load_oasis[2]
        end_date = data_load_oasis[3]
        home = data_load_oasis[4]

        logger = self.get_logger()
        logger.info(f" Test {sweep} Started")

        home_page_actions = HomePageActions(self.driver)
        home_page_actions.entry(users, iframes, urls, sweep, end_date, home, logger)

        logger.info(f" Test {sweep} Ended")
