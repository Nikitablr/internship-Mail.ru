import pytest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install()) # explain this line for me
    driver.implicitly_wait(10)
    yield driver
    time.sleep(40) # should avoid hard waits, especially sleep(). this line should be deleted. you're basically wait for 40 second after each test
