from pages.main_page import MainPage
from locators import locators


class MailPage(MainPage): # move locators here

    def click_create_message(self):
        self.browser.find_element(*locators.CREATE_MESSAGE_BUTTON).click()

    def enter_email(self): # change this method to receive a string
        self.browser.find_element(*locators.WHOM_FIELD).send_keys('rudakby@gmail.com')

    def click_save_draft(self):
        self.browser.find_element(*locators.SAVE_DRAFT).click()

    def click_close_message_window(self):
        self.browser.find_element(*locators.CLOSE_MESSAGE_WINDOW).click()

    def open_draft_page(self):
        self.browser.find_element(*locators.DRAFT_PAGE_BUTTON).click()

    def message_in_draft(self):
        assert self.browser.find_element(*locators.MESSAGE_IN_DRAFT)