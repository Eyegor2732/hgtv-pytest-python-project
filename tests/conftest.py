import platform
import pytest
from selenium import webdriver
from utilities.EntriesClass import get_oasis, get_sweets, get_10k, get_central, get_dream


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


#  ========== All entries  ===

oasis = get_oasis()
sweets = get_sweets()
k10 = get_10k()
central = get_central()
dream = get_dream()


# ========== All Load fixture  ===

@pytest.fixture(scope="function", params=[dream, central, k10, sweets, oasis])
def data_load_all(request):
    return request.param
