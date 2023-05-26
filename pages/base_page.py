class BasePage:

    def __init__(self, browser):
        self.browser = browser
        

    def go_to_site(self):
        url = "https://mail.ru/"
        self.browser.get(url)

