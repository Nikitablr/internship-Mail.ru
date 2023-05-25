from pages.main_page import MainPage
from pages.mail_page import MailPage

def test_add_letter_to_draft(browser):
    page = MainPage(browser) #change name to main_page
    page.go_to_site(())
    page.click_login_button()
    page.click_allow_button() # this step doesn't appear always
    page.fill_email_address_field()
    page.click_enter_password_button()
    page.enter_password_button()
    page.click_login_button_password()
    page = MailPage(browser) #change name to mail_page
    page.click_create_message()
    page.enter_email()
    page.click_save_draft()
    page.click_close_message_window()
    page.open_draft_page()
    page.message_in_draft() # assert should be in test directly and you should actually check letter you created in there