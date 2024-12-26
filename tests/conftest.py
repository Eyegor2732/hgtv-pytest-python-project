import platform
import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


#  ========== Class Setup / Teardown fixture  ===

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    match browser_name:
        case "chrome":
            driver = webdriver.Chrome()
        case "chrome_headless":
            ops = webdriver.ChromeOptions()
            ops.add_argument('--headless=new')
            driver = webdriver.Chrome(options=ops)
        case "safari":
            if platform.system() == "Darwin":
                driver = webdriver.Safari()
            else:
                driver = webdriver.Edge()
        case "firefox":
            driver = webdriver.Firefox()
        case "firefox_headless":
            ops = webdriver.FirefoxOptions()
            ops.add_argument('--headless=new')
            driver = webdriver.Firefox(options=ops)
        case "edge":
            driver = webdriver.Edge()
        case "edge_headless":
            ops = webdriver.EdgeOptions()
            ops.add_argument('headless')
            driver = webdriver.Edge(options=ops)
        case _:
            if platform.system() == "Darwin":
                driver = webdriver.Safari()
            else:
                driver = webdriver.Edge()

    driver.set_window_size(1700, 1200)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


#  ========== Class Dataload fixture  ===

@pytest.fixture(scope="class")
def data_load():
    email1 = os.getenv("email1")
    email2 = os.getenv("email2")
    email3 = os.getenv("email3")
    email4 = os.getenv("email4")

    return \
        [
            (email1, email2, email3, email4)
        ]


#  ========== Urban Oasis  ===  until 11/21/2024, at 8:59 a.m. ET === hgtv  ===  foodnetwork

@pytest.fixture(scope="function")
def data_load_oasis():
    return \
        [
            ("ngxFrame277066", "ngxFrame277068"),
            ("https://www.hgtv.com/sweepstakes/hgtv-urban-oasis/sweepstakes?ocid=xp:sistersite&xp=sistersite",
             "https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-urban-oasis-sweepstakes?ocid=xp:sistersite&xp=sistersite"),
            "oasis",
            "2024-11-21 08:59:00",
            "https://www.hgtv.com/sweepstakes/hgtv-urban-oasis/sweepstakes?ocid=xp:sistersite&xp=sistersite"
        ]


#  ========== Holiday Sweets $5k  ===  until 01/07/2025, at 8:59 a.m. ET  ===  foodnetwork === tlc

@pytest.fixture(scope="function")
def data_load_sweets():
    return \
        [
            ("ngxFrame279528", "ngxFrame279530"),
            (
                "https://www.foodnetwork.com/sponsored/sweepstakes/holiday-sweets-and-treats?ocid=xp:sistersite&xp=sistersite",
                "https://www.tlc.com/sweepstakes/holiday-sweets-and-treats?ocid=xp:sistersite&xp=sistersite"),
            "sweets",
            "2025-01-07 08:59:00",
            "https://www.foodnetwork.com/sponsored/sweepstakes/holiday-sweets-and-treats?nl=PC-TLC%3ASweeps_112324_box2-FNSweeps&lid=vmefnq3y10e8"
        ]


# ========== Holiday Central $5K  ===  until 01/09/2025, at 8:59 a.m. ET  ===  tlc === discovery

@pytest.fixture(scope="function")
def data_load_central():
    return \
        [
            ("ngxFrame279580", "ngxFrame279582"),
            ("https://www.tlc.com/sweepstakes/holiday-central-5k-giveaway?xp=sistersite",
             "https://www.discovery.com/sweepstakes/holiday-central?ocid=xp:sistersite&xp=sistersite"),
            "central",
            "2025-01-09 08:59:00",
            "https://www.tlc.com/sweepstakes/holiday-central-5k-giveaway?nl=PC-TLC%3ASweeps_112324_postcard&lid=53bo7n57t64x"
        ]


# ========== $10KHoliday  ===  until 01/08/2025, at 8:59 a.m. ET  ===  hgtv === foodnetwork

@pytest.fixture(scope="function")
def data_load_10k():
    return \
        [
            ("ngxFrame278086", "ngxFrame278088"),
            ("https://www.hgtv.com/shows/10k-to-holiday?xp=sistersite",
             "https://www.foodnetwork.com/sponsored/sweepstakes/10k-to-holiday?xp=sistersite"),
            "10k",
            "2025-01-08 08:59:00",
            "https://www.hgtv.com/shows/10k-to-holiday?nl=PC-TLC%3ASweeps_112324_box1-HGSweeps&lid=jaxq67lj8w6l"
        ]


# ========== DreamHome  ===  until 02/14/2025, at 5:00 p.m. ET  ===  hgtv === foodnetwork

@pytest.fixture(scope="function")
def data_load_dream():
    return \
        [
            ("ngxFrame281392", "ngxFrame281394"),
            ("https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes",
             "https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-dream-home-sweepstakes"),
            "dream",
            "2025-02-14 17:00:00",
            "https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes"
        ]
