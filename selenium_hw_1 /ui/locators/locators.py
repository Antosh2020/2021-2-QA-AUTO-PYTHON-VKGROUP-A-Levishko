from selenium.webdriver.common.by import By

LOGIN_BUTTON = (By.CLASS_NAME, "responseHead-module-button-2yl51i")
EMAIL_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.NAME, "password")
LOGIN_BUTTON_FORM = (By.CLASS_NAME, "authForm-module-button-1u2DYF")
NAME_ON_SCREEN = (By.XPATH, "//div[text()='Антон Антон']")

LOGOFF_BUTTON = (By.XPATH, "//a[text()='Log off']")

NAME_INPUT = (By.XPATH, '//div[@data-name="fio"]/div[@class="input__wrap"]/input[@maxlength="100"]')
PHONE_INPUT = (By.XPATH, '//div[@data-name="phone"]/div[@class="input__wrap"]/input[@maxlength="20"]')
SAVE_BUTTON = (By.CLASS_NAME, "button__text")

AUDIENCES_BUTTON = (By.XPATH, '//a[@href="/segments"]')
BILLING_BUTTON = (By.XPATH, '//a[@href="/billing"]')
PROFILE_BUTTON = (By.XPATH, '//a[@href="/profile"]')
