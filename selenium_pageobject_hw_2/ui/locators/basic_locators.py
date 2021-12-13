from selenium.webdriver.common.by import By


class BasePageLocators:
	LOGIN_BUTTON = (By.XPATH, '//div[text()="Войти" or text()="Log in"]')
	EMAIL_INPUT = (By.NAME, "email")
	PASSWORD_INPUT = (By.NAME, "password")
	LOGIN_BUTTON_FORM = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
	NAME_ON_SCREEN = (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')

	LOGOFF_BUTTON = (By.XPATH, "//a[text()='Log off']")

	AUTH_ERR_TEXT = (By.CLASS_NAME, "formMsg_text")


class MainPageLocators:
	NAVBAR_LINK_TEMPLATE = (By.XPATH, '//li[contains(@class, "center-module-buttonWrap")]//a[@href="/{}"]')
	AUDIENCES_BUTTON = (By.XPATH, '//a[@href="/segments"]')
	BILLING_BUTTON = (By.XPATH, '//a[@href="/billing"]')
	PROFILE_BUTTON = (By.XPATH, '//a[@href="/profile"]')


class CampaignPageLocators:
	CAMPAIGN_BUTTON = (By.XPATH, '//a[@href="/campaign/new"]')


class ProfilePageLocators(BasePageLocators):
	NAME_INPUT = (By.XPATH, '//div[@data-name="fio"]//input[@maxlength="100"]')
	PHONE_INPUT = (By.XPATH, '//div[@data-name="phone"]//input[@maxlength="20"]')
	SAVE_BUTTON = (By.CLASS_NAME, "button__text")

