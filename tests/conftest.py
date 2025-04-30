import platform
import pytest
from selenium import webdriver
from utilities.EntriesClass import *


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="edge")


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


#  ========== All sweepstakes  ===

oasis = get_oasis()
sweets = get_sweets()
k10 = get_10k()
central = get_central()
dream = get_dream()
fresh = get_fresh()
healthy = get_healthy()
yes = get_yes()
curb = get_curb()
groc = get_groc()
smart = get_smart()
champ = get_champ()
valspar = get_valspar()
spring = get_spring()
outside = get_outside()

# ========== All Load fixture  ===

# @pytest.fixture(scope="function", params=[k5groc, curb, yes, healthy, fresh, dream, central, k10, sweets, oasis])
@pytest.fixture(scope="function", params=[outside, smart, spring, groc]) #
def data_load_double(request):
    return request.param


@pytest.fixture(scope="function", params=[valspar])
def data_load_single(request):
    return request.param
