import pytest
from ui.locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseCase:

	driver = None

	@pytest.fixture(scope="function", autouse=True)
	def setup(self, driver):
		self.driver = driver

	def find(self, locator):
		element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(((locator))))
		return element

	def login(self, email, password):
		login_button = self.find(locators.LOGIN_BUTTON)
		login_button.click()
		email_input = self.find(locators.EMAIL_INPUT)
		email_input.send_keys(email)
		password_input = self.find(locators.PASSWORD_INPUT)
		password_input.send_keys(password)
		login_button_form = self.find(locators.LOGIN_BUTTON_FORM).click()
