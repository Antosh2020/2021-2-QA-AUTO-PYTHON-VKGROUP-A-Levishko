from ui.pages.base_page import BasePage
from ui.pages.profile_page import ProfilePage
from ui.locators.basic_locators import MainPageLocators


class MainPage(BasePage):

	locators = MainPageLocators()

	def go_to_page(self, page):
		page_locator = (self.locators.NAVBAR_LINK_TEMPLATE[0],
						self.locators.NAVBAR_LINK_TEMPLATE[1].format(page))
		page = self.find(page_locator).click()

		return ProfilePage(self.driver)



