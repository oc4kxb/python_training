import json
import pytest
from fixture.application import Application


fixture = None
config = None


@pytest.fixture
def app(request):
    global fixture
    global config
    browser = request.config.getoption("--browser")
    if config is None:
        with open("../config.json") as config_file:
            config = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=config["baseUrl"])
    fixture.session.ensure_login(username=config["username"], password=config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if fixture is not None:
            fixture.session.ensure_logout()
            fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")
