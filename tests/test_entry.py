import pytest
from page_actions.HomePageActions import HomePageActions
from utilities.BaseClass import BaseClass, get_logger

logger = get_logger()


class TestEntry(BaseClass):

    @pytest.mark.usefixtures("data_load_all")
    def test_entry(self, data_load_all):
        users = data_load_all[0]
        iframes = data_load_all[1]
        urls = data_load_all[2]
        sweep = data_load_all[3]
        end_date = data_load_all[4]
        home = data_load_all[5]

        logger.info(f" Test {sweep} Started")

        home_page_actions = HomePageActions(self.driver)
        home_page_actions.entry(users, iframes, urls, sweep, end_date, home, logger)

        logger.info(f" Test {sweep} Ended")
