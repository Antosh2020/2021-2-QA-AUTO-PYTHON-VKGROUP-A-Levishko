import os
import pytest

from api.client import ApiClient

URL = "https://target.my.com"


@pytest.fixture(scope='function')
def api_client():
    return ApiClient(URL)


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))
