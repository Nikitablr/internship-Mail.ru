from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import locators


class MainPage(BasePage):
    #Open login page
    def click_login_button(self):
        self.browser.find_element(*locators.LOGIN_BUTTON).click()
    #Accept cookies
    def click_allow_button(self):
        self.browser.find_element(*locators.ALLOW_BUTTON).click()

    def fill_email_address_field(self):
        self.browser.switch_to.frame(self.browser.find_elements(By.CSS_SELECTOR, ".ag-popup__frame__layout__iframe")[0])
        self.browser.find_element(*locators.EMAIL_FIELD).send_keys("costartrial")

    def click_enter_password_button(self):
        self.browser.find_element(*locators.ENTER_PASSWORD_BUTTON).click()

    def enter_password_button(self):
        self.browser.find_element(*locators.PASSWORD_FIELD).send_keys("Costar12345!")

    def click_login_button_password(self):
        self.browser.find_element(*locators.LOGIN_BUTTON_PASSWORD).click()




