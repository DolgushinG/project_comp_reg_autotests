import time

import pytest

from constants import URL, DEFAULT_USER
from pages.EventPage import EventPage
from pages.LoginFormPage import LoginFormPage
from pages.ProfilePage import ProfilePage


@pytest.mark.usefixtures("driver")
class TestEvent:
    def test_open_event(self):
        event_form = EventPage(self.driver)
        event_form._go_to_url(f'{URL}/')
        event_form.click_event_with_js()
        event_form.click_nav_main_info()
        event_form.click_nav_rules()
        event_form.click_nav_price()

    def test_take_part(self, reg):
        event_form = EventPage(self.driver)
        event_form._go_to_url(f'{URL}/')
        event_form.click_event_with_js()
        event_form.select_category()
        event_form.select_birthday()
        event_form.select_sets()
        event_form.click_btn_take_part()
        event_form.verify_success_take_part()




