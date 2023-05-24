from selenium.webdriver.common.by import By


LOGIN_BUTTON = (By.CSS_SELECTOR, '.ph-login')
ALLOW_BUTTON = (By.CSS_SELECTOR, '.cmpboxbtn.cmpboxbtnyes')
EMAIL_FIELD = (By.NAME, 'username')
ENTER_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.submit-button-wrap')
PASSWORD_FIELD = (By.CSS_SELECTOR, '.withIcon-0-2-72')
LOGIN_BUTTON_PASSWORD = (By.CSS_SELECTOR, '.inner-0-2-81')
CREATE_MESSAGE_BUTTON = (By.CSS_SELECTOR, '.compose-button__wrapper')
WHOM_FIELD = (By.CSS_SELECTOR, '.container--H9L5q')
SAVE_DRAFT = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/button')
CLOSE_MESSAGE_WINDOW = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/button[2]')
RECEPIENTS_EMAIL = (By.CSS_SELECTOR, '.contacts--1ofjA')
DRAFT_PAGE_BUTTON = (By.XPATH,'//*[@id="sideBarContent"]/div/nav/a[9]')
MESSAGE_IN_DRAFT = (By.CSS_SELECTOR, '.llc__background')