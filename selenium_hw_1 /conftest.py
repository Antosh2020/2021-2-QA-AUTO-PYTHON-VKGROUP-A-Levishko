import pytest
from selenium import webdriver


def pytest_addoption(parser):
	parser.addoption("--url", default="https://target.my.com/")


@pytest.fixture()
def config(request):
	url = request.config.getoption("--url")
	return {"url": url}


@pytest.fixture(scope="function")
def driver(config):
	url = config["url"]
	browser = webdriver.Chrome(executable_path="/Users/a.levishko/Dev/chromedriver/chromedriver")
	browser.maximize_window()
	browser.get(url)
	yield browser
	browser.quit()



