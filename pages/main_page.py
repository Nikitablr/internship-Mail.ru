from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.ph-login')
    ALLOW_BUTTON = (By.CSS_SELECTOR, '.cmpboxbtn.cmpboxbtnyes')
    LOGIN_FRAME = (By.CSS_SELECTOR, ".ag-popup__frame__layout__iframe")
    EMAIL_FIELD = (By.NAME, "username")
    ENTER_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.submit-button-wrap')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '.withIcon-0-2-72')
    LOGIN_BUTTON_PASSWORD = (By.CSS_SELECTOR, '.inner-0-2-81')

    # Open login page
    def click_login_button(self):
        self.click(*MainPage.LOGIN_BUTTON)

    # Accept cookies
    def click_allow_button(self):
        self.click(*MainPage.ALLOW_BUTTON)

    def fill_email_address_field(self, email):
        frame = self.browser.find_element(*MainPage.LOGIN_FRAME)
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MainPage.EMAIL_FIELD).send_keys(email)

    def click_enter_password_button(self):
        self.click(*MainPage.ENTER_PASSWORD_BUTTON)

    # def enter_password(self, password):
    #     self.browser.find_element(*MainPage.PASSWORD_FIELD).send_keys(password)

    def enter_password(self, password):
        self.enter(password, *MainPage.PASSWORD_FIELD)

    def click_login_button_password(self):
        self.click(*MainPage.LOGIN_BUTTON_PASSWORD)
