from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def go_to_site(self):
        url = "https://mail.ru/"
        self.browser.get(url)

    def click(self, *locator):
        button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        button.click()