import time
import pytest
from base import BaseCase
from ui.locators import basic_locators
from ui.pages.main_page import MainPage


class TestOne(BaseCase):
	@pytest.mark.skip("SKIP")
	def test_auth_success(self):
		self.base_page.login("zdobsizdub@inbox.ru", "adminadmin")
		name_on_screen = self.base_page.find(basic_locators.BasePageLocators.NAME_ON_SCREEN).is_displayed()
		time.sleep(1)
		assert "Campaigns" in self.driver.title
		assert name_on_screen == True

	def test_logout_success(self):
		self.base_page.login("zdobsizdub@inbox.ru", "adminadmin")
		name_on_screen = self.base_page.click(basic_locators.BasePageLocators.NAME_ON_SCREEN)
		logoff_button = self.base_page.click(basic_locators.BasePageLocators.LOGOFF_BUTTON)
		login_button = self.base_page.find(basic_locators.BasePageLocators.LOGIN_BUTTON).is_displayed()
		assert login_button == True
		assert "Рекламная платформа myTarget — Сервис таргетированной рекламы" in self.driver.title
	@pytest.mark.skip("SKIP")
	def test_contacts_info_edit(self):
		self.base_page.login("zdobsizdub@inbox.ru", "adminadmin")
		profile_button = self.base_page.click(basic_locators.MainPageLocators.PROFILE_BUTTON)
		name_input = self.base_page.find(basic_locators.ProfilePageLocators.NAME_INPUT)
		name_input.clear()
		name_input.send_keys("Антон Антон")
		phone_input = self.base_page.find(basic_locators.ProfilePageLocators.PHONE_INPUT)
		phone_input.clear()
		phone_input.send_keys("+79189410098")
		save_button = self.base_page.click(basic_locators.ProfilePageLocators.SAVE_BUTTON)
		assert name_input.get_attribute("value") == "Антон Антон"
		assert phone_input.get_attribute("value") == "+79189410098"

	testdata = [
		(basic_locators.MainPageLocators.AUDIENCES_BUTTON, 'https://target.my.com/segments/segments_list'),
		(basic_locators.MainPageLocators.BILLING_BUTTON, 'https://target.my.com/billing')
	]

	@pytest.mark.parametrize('page,expected', testdata)
	@pytest.mark.skip("SKIP")
	def test_page_navigation(self, page, expected):
		self.base_page.login("zdobsizdub@inbox.ru", "adminadmin")
		self.base_page.click(page)
		assert self.driver.current_url == expected

	@pytest.mark.parametrize(
		'login,password',
		[
			("zdobsizdub@inbox.ru", 'admin'),  # валидный логин и невалидный пароль
			("zdobsizdub@mail.ru", 'adminadmin')  # невалидный логин и валидный пароль
		]
	)
	@pytest.mark.skip("SKIP")
	def test_negative_auth(self, login, password):
		self.base_page.login(login, password)
		auth_err_text = self.base_page.find(basic_locators.BasePageLocators.AUTH_ERR_TEXT).is_displayed()
		assert auth_err_text == True

	@pytest.mark.skip("SKIP")
	def test_page(self):
		self.base_page.login("zdobsizdub@inbox.ru", "adminadmin")
		segments_page = self.main_page.go_to_page('profile')
		assert segments_page.is_opened()