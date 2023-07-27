import pytest
from selenium import webdriver



capabilities = {
    "browserName": "chrome",
    "browserVersion": "106.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
    yield driver
    driver.close()

# @pytest.fixture(scope="function")
# def browser():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.close()

