import platform
import pytest
from selenium import webdriver
from utilities.EntriesClass import *


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox")


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
            if platform.system() != "Darwin":
                raise RuntimeError("Safari is only supported on macOS")
            driver = webdriver.Safari()
        case "firefox":
            driver = webdriver.Firefox()
        case "firefox_headless":
            ops = webdriver.FirefoxOptions()
            ops.add_argument('--headless')
            driver = webdriver.Firefox(options=ops)
        case "edge":
            driver = webdriver.Edge()
        case "edge_headless":
            ops = webdriver.EdgeOptions()
            ops.add_argument('headless=new')
            driver = webdriver.Edge(options=ops)
        case _:
            raise ValueError(f"Unsupported browser: {browser_name}")

    driver.set_window_size(1700, 1200)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


#  ========== All sweepstakes  ===

oasis = get_oasis()
central = get_central()
dream = get_dream()
smart = get_smart()
true = get_true()
kitchen = get_kitchen()
decades = get_decades()
newyear = get_newyear()
bite = get_bite()
big = get_big()


# ========== All Load fixture  ===
#
@pytest.fixture(scope="function", params=[dream, newyear, bite, big])
def data_load_double(request):
    return request.param


@pytest.fixture(scope="function", params=[true, kitchen, decades])
def data_load_single(request):
    return request.param
