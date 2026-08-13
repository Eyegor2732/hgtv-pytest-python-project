import platform
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utilities.EntriesClass import *


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome_headless")


#  ========== Class Setup / Teardown fixture  ===

@pytest.fixture(scope="class")
def setup(request):
    browser_name: str = request.config.getoption("browser_name")

    match browser_name:
        case "chrome" | "chrome_headless":
            ops = webdriver.ChromeOptions()

            ops.add_argument("--no-sandbox")
            ops.add_argument("--disable-dev-shm-usage")
            ops.add_argument("--window-size=1920,1080")

            if browser_name == "chrome_headless":
                ops.add_argument("--headless=new")

            driver = webdriver.Chrome(options=ops)
        case "safari":
            if platform.system() != "Darwin":
                raise RuntimeError("Safari is only supported on macOS")
            driver = webdriver.Safari()
        case "firefox" | "firefox_headless":
            ops = webdriver.FirefoxOptions()

            if browser_name == "firefox_headless":
                ops.add_argument("--headless")

            driver = webdriver.Firefox(options=ops)
        case "edge" | "edge_headless":
            ops = webdriver.EdgeOptions()

            if browser_name == "edge_headless":
                ops.add_argument("headless=new")

            driver = webdriver.Edge(options=ops)
        case _:
            raise ValueError(f"Unsupported browser: {browser_name}")

    # driver.set_window_size(1700, 1200)
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)
    yield
    driver.quit()


#  ========== All sweepstakes  ===

oasis = get_oasis()
central = get_central()
dream = get_dream()
smart = get_smart()
grill = get_grill()
cash = get_cash()
trick = get_trick()


# ========== All Load fixture  ===

@pytest.fixture(scope="function", params=[grill, cash, trick])
def data_load_double(request):
    return request.param


@pytest.fixture(scope="function", params=[])
def data_load_single(request):
    return request.param
