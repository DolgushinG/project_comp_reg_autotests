import time

import pytest

from constants import URL, DEFAULT_USER
from pages.EventPage import EventPage
from pages.LoginFormPage import LoginFormPage
from pages.ProfilePage import ProfilePage


@pytest.mark.usefixtures("driver")
class TestEvent:
    def test_open_event(self):
        login_form = EventPage(self.driver)
        login_form._go_to_url(f'{URL}/')
        login_form.click_event_with_js()
        login_form.click_nav_main_info()
        login_form.click_nav_sets()
        login_form.click_nav_rules()
        login_form.click_nav_price()




