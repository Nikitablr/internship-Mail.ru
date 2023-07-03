from pages.main_page import MainPage
from pages.mail_page import MailPage

def test_add_letter_to_draft(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    main_page.click_login_button()
    main_page.click_allow_button()
    main_page.fill_email_address_field('costartrial')
    main_page.click_enter_password_button()
    main_page.enter_password('Costar12345!')
    main_page.click_login_button_password()
    mail_page = MailPage(browser)
    mail_page.click_create_message()
    mail_page.enter_random_email('rudakby@gmail.com')
    mail_page.click_save_draft()
    mail_page.click_close_message_window()
    mail_page.open_draft_page()
    assert 'rudakby@gmail.com' in mail_page.message_in_draft()
