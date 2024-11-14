import platform
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

# terminal command: py.test --browser_name chrome
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    match browser_name:
        case "chrome":
            driver = webdriver.Chrome()
        case "safari":
            if platform.system() == "Darwin":
                driver = webdriver.Safari()
            else:
                driver = webdriver.Edge()
        case "firefox":
            driver = webdriver.Firefox()
        case "edge":
            driver = webdriver.Edge()
        case _:
            if platform.system() == "Darwin":
                driver = webdriver.Safari()
            else:
                driver = webdriver.Edge()


    driver.get("https://www.hgtv.com/sweepstakes/hgtv-urban-oasis/sweepstakes?ocid=xp:sistersite&xp=sistersite")
    driver.set_window_size(1700, 1200)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class")
def data_load():
    print("User profile data is being created")
    return \
        [
            ("k@yahoo.com", "v@yahoo.com", "m@outlook.com"),
            ("ngxFrame277066", "ngxFrame277068"),
            ("https://www.hgtv.com/sweepstakes/hgtv-urban-oasis/sweepstakes?ocid=xp:sistersite&xp=sistersite", "https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-urban-oasis-sweepstakes?ocid=xp:sistersite&xp=sistersite")
        ]
