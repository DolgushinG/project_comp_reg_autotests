import time

import pytest

from constants import URL
from pages.AdminEventPage import AdminEventPage
from pages.EventPage import EventPage


@pytest.mark.usefixtures("driver")
class TestEvent:
    add_url = "/event/1"
    @pytest.mark.event
    def test_open_event(self):
        event_form = EventPage(self.driver)
        event_form.go_to_url(f'{URL}{self.add_url}')
        event_form.click_nav_main_info()
        event_form.click_nav_rules()
        # event_form.click_nav_price()

    @pytest.mark.event
    def test_open_list_participant(self):
        event_form = EventPage(self.driver)
        event_form.go_to_url(f'{URL}{self.add_url}')
        event_form.click_list_participant()
        event_form.verify_list_participant()

    @pytest.mark.event
    def test_open_qualification_results(self):
        event_form = EventPage(self.driver)
        event_form.go_to_url(f'{URL}{self.add_url}')
        event_form.click_qualification_results()
        event_form.verify_qualification_results()

    @pytest.mark.event
    def test_take_part(self, reg):
        event_form = EventPage(self.driver)
        event_form.go_to_url(f'{URL}{self.add_url}')
        time.sleep(3)
        event_form.select_category()
        time.sleep(3)
        event_form.select_sport_category()
        time.sleep(3)
        event_form.select_sets()
        event_form.click_btn_take_part()
        event_form.verify_success_take_part()

    @pytest.mark.event
    def test_change_set(self, reg):
        event_form = EventPage(self.driver)
        event_form.go_to_url(f'{URL}{self.add_url}')
        time.sleep(2)
        event_form.select_category()
        time.sleep(2)
        event_form.select_sport_category()
        time.sleep(1)
        event_form.select_sets()
        event_form.click_btn_take_part()
        event_form.verify_success_take_part()
        grab_set = event_form.grab_info_sets()
        time.sleep(1)
        event_form.select_changed_sets(5)
        time.sleep(1)
        event_form.click_btn_changed_set()
        time.sleep(1)
        grab_set_2 = event_form.grab_info_sets()
        assert grab_set != grab_set_2, f'Error: {grab_set} == {grab_set_2}'

    @pytest.mark.event
    def test_send_result(self, reg):
        event_form = EventPage(self.driver)
        event_form.go_to_url(f'{URL}{self.add_url}')
        time.sleep(2)
        event_form.select_category()
        time.sleep(2)
        event_form.select_sport_category()
        time.sleep(2)
        event_form.select_sets()
        event_form.click_btn_take_part()
        event_form.verify_success_take_part()
        event_form.go_to_send_result()
        event_form.click_all_redpoints()
        event_form.scroll_down()
        event_form.click_send_result()
        event_form.verify_already_take_part()

    @pytest.mark.event
    def test_edit_result_after_send_result(self, reg):
        event_form = EventPage(self.driver)
        event_form.go_to_url(f'{URL}{self.add_url}')
        time.sleep(2)
        event_form.select_category()
        time.sleep(2)
        event_form.select_sport_category()
        time.sleep(2)
        event_form.select_sets()
        time.sleep(2)
        event_form.click_btn_take_part()
        event_form.verify_success_take_part()
        event_form.go_to_send_result()
        event_form.click_all_redpoints()
        event_form.scroll_down()
        event_form.click_send_result()
        event_form.verify_already_take_part()
        time.sleep(2)
        event_form.click_edit_result()
        event_form.click_all_flash()
        event_form.scroll_down()
        event_form.click_send_result()
        event_form.verify_already_take_part()




