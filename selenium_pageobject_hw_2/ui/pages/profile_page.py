from ui.locators.profile_locators import ProfilePageLocators
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import ProfilePageLocators


class ProfilePage(BasePage):
    url = 'https://target.my.com/profile/contacts'
    locators = ProfilePageLocators()



