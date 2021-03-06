import importlib
import json
import os.path
import jsonpickle
import pytest
from fixture.application import Application
from fixture.db import DbFixture


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_path) as config_file:
            target = json.load(config_file)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if fixture is not None:
            fixture.session.ensure_logout()
            fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    db_fixture = DbFixture(host=db_config["host"], database=db_config["database"],
                           user=db_config["user"], password=db_config["password"])
    return db_fixture


@pytest.fixture()
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="config.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("json_"):
            test_data = load_from_file(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).test_data


def load_from_file(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
