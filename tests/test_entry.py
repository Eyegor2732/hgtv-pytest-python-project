import pytest
from page_actions.HomePageActions import HomePageActions
from tests.conftest import data_load_single
from utilities.BaseClass import BaseClass, get_logger


class TestEntry(BaseClass):

    logger = get_logger()

    @pytest.mark.usefixtures("data_load_double")
    def test_entry_double(self, data_load_double):
        users = data_load_double[0]
        iframes = data_load_double[1]
        urls = data_load_double[2]
        sweep = data_load_double[3]
        end_date = data_load_double[4]
        home = data_load_double[5]

        self.logger.info(f" Test {sweep} Started")

        home_page_actions = HomePageActions(self.driver)
        home_page_actions.entry_double(users, iframes, urls, sweep, end_date, home, self.logger)

        self.logger.info(f" Test {sweep} Ended")

    @pytest.mark.usefixtures("data_load_single")
    def test_entry_single(self, data_load_single):
        users = data_load_single[0]
        iframes = data_load_single[1]
        urls = data_load_single[2]
        sweep = data_load_single[3]
        end_date = data_load_single[4]
        home = data_load_single[5]

        self.logger.info(f" Test {sweep} Started")

        home_page_actions = HomePageActions(self.driver)
        home_page_actions.entry_single(users, iframes, urls, sweep, end_date, home, self.logger)

        self.logger.info(f" Test {sweep} Ended")
