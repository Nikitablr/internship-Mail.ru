import pytest
from selenium import webdriver



capabilities = {
    "browserName": "chrome",
    "browserVersion": "107.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Remote(command_executor="http://192.168.1.12:4444/wd/hub/", desired_capabilities=capabilities)
    yield driver
    driver.close()


