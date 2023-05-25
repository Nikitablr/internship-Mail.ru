class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def go_to_site(self):
        url = "https://mail.ru/"
        self.browser.get(url)

    # should rewrite basic selenium methods here. click(locator) => find_element(locator).click()