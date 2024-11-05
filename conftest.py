import os
import time
from dataclasses import dataclass
from datetime import datetime

import pytest

import tools
from config.drivers import get_driver
from config.options import get_options
from constants import User, URL, DEFAULT_USER
from pages.AdminEventPage import AdminEventPage
from pages.LoginFormPage import LoginFormPage
from pages.ProfilePage import ProfilePage
from pages.RegistrationFormPage import RegistrationFormPage

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
OUTPUT_ROOT = os.path.join(PROJECT_ROOT, 'tests', 'output')
DATA_ROOT = os.path.join(PROJECT_ROOT, 'data')

BROWSER_NAME = ''


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = get_options(BROWSER_NAME)
    driver = get_driver(browser_name=BROWSER_NAME, options=options)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield request.cls.driver
    request.cls.driver.quit()


def pytest_configure(config):
    global BROWSER_NAME
    BROWSER_NAME = config.getoption("--browser")


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.originalname)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.cls.driver
            take_screenshot(driver, request.node.originalname)
            print("executing test failed", request.node.originalname)


def take_screenshot(driver, originalname):
    time.sleep(1)
    file_name = \
        f'{originalname}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    driver.save_screenshot(f"{OUTPUT_ROOT}/{file_name}")


def pytest_collection_modifyitems():
    tools.remove_test_dir(OUTPUT_ROOT)


@pytest.fixture(scope='function')
def get_user_request(request):
    user = User()
    request.cls.user = user
    return user


@pytest.fixture()
def login(request):
    login_form = LoginFormPage(request.cls.driver)
    login_form.go_to_url(f'{URL}/login')
    login_form.fill_email(DEFAULT_USER.email)
    login_form.fill_password(DEFAULT_USER.password)
    login_form.click_btn_submit()
    login_form.verify_header_profile()
    profile_page = ProfilePage(request.cls.driver)
    profile_page.go_to_url(f'{URL}/profile')


@pytest.fixture()
def reg(request):
    get_user = User()
    reg_form = RegistrationFormPage(request.cls.driver)
    reg_form.go_to_url(f'{URL}/register')
    reg_form.fill_first_name(tools.random_word(4, 8) + tools.random_word(4, 8))
    reg_form.fill_last_name(tools.random_word(4, 8) + tools.random_word(4, 8))
    reg_form.select_gender()
    reg_form.fill_email(tools.get_email())
    reg_form.fill_password(get_user.password)
    reg_form.fill_confirm_password(get_user.password)
    reg_form.click_checkbox_accept_terms()
    reg_form.click_btn_submit()
    reg_form.verify_profile()
@pytest.fixture()
def login_to_admin(request):
    admin_event_form = AdminEventPage(request.cls.driver)
    admin_event_form.go_to_url(f'{URL}/moon')
    admin_event_form.fill_username('Tester2')
    admin_event_form.fill_password('Tester3')
    admin_event_form.click_btn_enter()
    admin_event_form.verify_header_admin()

@pytest.fixture()
def delete_event(request):
    yield
    time.sleep(1)
    admin_event_form = AdminEventPage(request.cls.driver)
    admin_event_form.delete_event()
