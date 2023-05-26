from pages.main_page import MainPage
from selenium.webdriver.common.by import By



class MailPage(MainPage):
    CREATE_MESSAGE_BUTTON = (By.CSS_SELECTOR, '.compose-button__wrapper')
    WHOM_FIELD = (By.CSS_SELECTOR, '.container--H9L5q')
    SAVE_DRAFT = (By.XPATH, '//button[@data-test-id="save"]')
    CLOSE_MESSAGE_WINDOW = (By.XPATH, '//button[@title="Закрыть"]')
    RECEPIENTS_EMAIL = (By.CSS_SELECTOR, '.contacts--1ofjA')
    DRAFT_PAGE_BUTTON = (By.XPATH, '//*[@id="sideBarContent"]/div/nav/a[9]')
    MESSAGE_IN_DRAFT = (By.XPATH, '//span[@class="ll-crpt"]')
    USER_EMAIL = (By.XPATH, '//div/span[@class="text--1tHKB"]')

    def click_create_message(self):
        self.click(*MailPage.CREATE_MESSAGE_BUTTON)

    # def random_email(self):
    #     fake = Faker()
    #     fake.pystr(min_chars=None, max_chars=10)
    #     email = fake.email()
    #     return str(email)

    def enter_random_email(self, email):
        self.browser.find_element(*MailPage.WHOM_FIELD).send_keys(email)

    def click_save_draft(self):
        self.click(*MailPage.SAVE_DRAFT)

    def click_close_message_window(self):
        self.click(*MailPage.CLOSE_MESSAGE_WINDOW)

    def open_draft_page(self):
        self.click(*MailPage.DRAFT_PAGE_BUTTON)

    def message_in_draft(self):
        mess = self.browser.find_element(*MailPage.MESSAGE_IN_DRAFT)
        return mess.text


