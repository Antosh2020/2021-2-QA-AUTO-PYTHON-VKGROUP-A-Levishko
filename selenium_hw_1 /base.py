import pytest
from ui.locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

CLICK_RETRY =3

class BaseCase:

	driver = None

	@pytest.fixture(scope="function", autouse=True)
	def setup(self, driver):
		self.driver = driver

	def find(self, locator):
		element = WebDriverWait(self.driver, 5).until((EC.presence_of_element_located(locator)))
		return element

	def login(self, email, password):
		login_button = self.find(locators.LOGIN_BUTTON)
		login_button.click()
		email_input = self.find(locators.EMAIL_INPUT)
		email_input.send_keys(email)
		password_input = self.find(locators.PASSWORD_INPUT)
		password_input.send_keys(password)
		login_button_form = self.find(locators.LOGIN_BUTTON_FORM).click()

	def click(self, locator):
		for i in range (CLICK_RETRY):
			try:
				elem = self.find(locator)
				if i <2:
					self.driver.refresh()
				elem.click()
				return
			except StaleElementReferenceException:
				if i == CLICK_RETRY -1:
					raise
