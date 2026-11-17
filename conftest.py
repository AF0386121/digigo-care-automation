import pytest, json
from ui.pages.login_page import LoginPage
from ui.pages.dashboard_page import DashboardPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

@pytest.fixture
def test_data():
    with open("testdata/test_data.json") as f:
        return json.load(f)