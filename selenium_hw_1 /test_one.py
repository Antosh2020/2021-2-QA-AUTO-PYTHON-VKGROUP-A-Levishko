import pytest
from base import BaseCase
from ui.locators import locators
import time


class TestOne(BaseCase):
	@pytest.mark.UI
	def test_auth_success(self):
		self.login("zdobsizdub@inbox.ru", "adminadmin")
		time.sleep(3)
		name_on_screen = self.find(locators.NAME_ON_SCREEN).is_displayed()
		assert "Campaigns" in self.driver.title
		assert name_on_screen == True

	@pytest.mark.UI
	def test_logout_success(self):
		self.login("zdobsizdub@inbox.ru", "adminadmin")
		time.sleep(2)
		name_on_screen = self.find(locators.NAME_ON_SCREEN).click()
		time.sleep(2)
		logoff_button = self.find(locators.LOGOFF_BUTTON).click()
		login_button = self.find(locators.LOGIN_BUTTON).is_displayed()
		assert login_button == True
		assert "Рекламная платформа myTarget — Сервис таргетированной рекламы" in self.driver.title

	@pytest.mark.UI
	def test_contacts_info_edit(self):
		self.login("zdobsizdub@inbox.ru", "adminadmin")
		profile_button = self.find(locators.PROFILE_BUTTON).click()
		time.sleep(2)
		name_input = self.find(locators.NAME_INPUT)
		name_input.clear()
		name_input.send_keys("Антон Антон")
		phone_input = self.find(locators.PHONE_INPUT)
		phone_input.clear()
		phone_input.send_keys("+79189410098")
		save_button = self.find(locators.SAVE_BUTTON).click()
		assert name_input.get_attribute("value") == "Антон Антон"
		assert phone_input.get_attribute("value") == "+79189410098"

	testdata = [
		(locators.AUDIENCES_BUTTON, 'https://target.my.com/segments/segments_list'),
		(locators.BILLING_BUTTON, 'https://target.my.com/billing')
	]

	@pytest.mark.parametrize('page,expected', testdata)
	@pytest.mark.UI
	def test_page_navigation(self, page, expected):
		self.login("zdobsizdub@inbox.ru", "adminadmin")
		time.sleep(3)
		self.find(page).click()
		assert self.driver.current_url == expected
