from selenium.webdriver.common.by import By

LOGIN_BUTTON = (By.XPATH, '//div[text()="Войти" or text()="Log in"]')
EMAIL_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.NAME, "password")
LOGIN_BUTTON_FORM = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
NAME_ON_SCREEN = (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')

LOGOFF_BUTTON = (By.XPATH, "//a[text()='Log off']")

NAME_INPUT = (By.XPATH, '//div[@data-name="fio"]//input[@maxlength="100"]')
PHONE_INPUT = (By.XPATH, '//div[@data-name="phone"]//input[@maxlength="20"]')
SAVE_BUTTON = (By.CLASS_NAME, "button__text")

AUDIENCES_BUTTON = (By.XPATH, '//a[@href="/segments"]')
BILLING_BUTTON = (By.XPATH, '//a[@href="/billing"]')
PROFILE_BUTTON = (By.XPATH, '//a[@href="/profile"]')

