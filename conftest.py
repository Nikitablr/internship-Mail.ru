import pytest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    driver.close()
