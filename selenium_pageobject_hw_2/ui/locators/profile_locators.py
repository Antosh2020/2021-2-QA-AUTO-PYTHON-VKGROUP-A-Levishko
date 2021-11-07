from selenium.webdriver.common.by import By


class ProfilePageLocators:
	NAME_INPUT = (By.XPATH, '//div[@data-name="fio"]//input[@maxlength="100"]')
	PHONE_INPUT = (By.XPATH, '//div[@data-name="phone"]//input[@maxlength="20"]')
	SAVE_BUTTON = (By.CLASS_NAME, "button__text")