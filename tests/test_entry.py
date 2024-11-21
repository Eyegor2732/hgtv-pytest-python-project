from page_actions.HomePageActions import HomePageActions
from utilities.BaseClass import BaseClass


class TestEntry(BaseClass):

    def test_entry(self, data_load):
        logger = self.get_logger()
        logger.info(" Test Started")

        users = data_load[0]
        iframes = data_load[1]
        urls = data_load[2]

        home_page_actions = HomePageActions(self.driver)
        home_page_actions.entry(users, iframes, urls)

        logger.info(" Test Passed")
