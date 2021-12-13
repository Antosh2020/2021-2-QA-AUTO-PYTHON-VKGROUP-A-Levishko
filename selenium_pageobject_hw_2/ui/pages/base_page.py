import time
from ui.locators import basic_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC

CLICK_RETRY = 3
BASE_TIMEOUT = 10


class PageNotLoadedException(Exception):
    pass


class BasePage(object):
    url = "https://target.my.com/"
    locators = basic_locators.BasePageLocators

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def is_opened(self, timeout=BASE_TIMEOUT):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True

        raise PageNotLoadedException(f'{self.url} did not open in {timeout}sec for {self.__class__.__name__}.\n'
                                     f'Current url: {self.driver.current_url}.')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY-1:
                    raise

    def login(self, email, password):
        login_button = self.click(self.locators.LOGIN_BUTTON)
        email_input = self.find(self.locators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.find(self.locators.PASSWORD_INPUT)
        password_input.send_keys(password)
        login_button_form = self.click(self.locators.LOGIN_BUTTON_FORM)
