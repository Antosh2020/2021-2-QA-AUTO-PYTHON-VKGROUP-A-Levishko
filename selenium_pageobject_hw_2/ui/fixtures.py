import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.profile_page import ProfilePage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


def get_driver(browser_name, download_dir=None):
    if browser_name == 'chrome':
        options = Options()
        if download_dir is not None:
            options.add_experimental_option("prefs", {"download.default_directory": download_dir})
        browser = webdriver.Chrome(executable_path="/Users/a.levishko/Dev/chromedriver/chromedriver", options=options)

    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: {browser_name}')

    browser.maximize_window()
    return browser


@pytest.fixture(scope='function')
def driver(config, temp_dir):

    browser = config['browser']
    url = config['url']

    browser = get_driver(browser, download_dir=temp_dir)
    browser.get(url)

    browser.set_window_size(1024, 768)
    yield browser
    browser.quit()


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']

    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()
