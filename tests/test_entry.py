import gc

import pytest
from page_actions.HomePageActions import HomePageActions
from utilities.BaseClass import BaseClass


class TestEntry(BaseClass):

    @pytest.mark.usefixtures("data_load_all")
    def test_entry(self, data_load, data_load_all):
        users = data_load[0]
        iframes = data_load_all[0]
        urls = data_load_all[1]
        sweep = data_load_all[2]
        end_date = data_load_all[3]
        home = data_load_all[4]

        logger = self.get_logger()
        logger.info(f" Test {sweep} Started")

        home_page_actions = HomePageActions(self.driver)
        home_page_actions.entry(users, iframes, urls, sweep, end_date, home, logger)

        logger.info(f" Test {sweep} Ended")
