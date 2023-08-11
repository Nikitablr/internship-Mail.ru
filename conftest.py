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
    driver = webdriver.Remote(command_executor="http://localhost:8080", desired_capabilities=capabilities)
    yield driver
    driver.close()


