import time

import pytest

from constants import URL, DEFAULT_USER
from pages.AdminEventPage import AdminEventPage
from pages.EventPage import EventPage
from pages.LoginFormPage import LoginFormPage
from pages.ProfilePage import ProfilePage


@pytest.mark.usefixtures("driver")
class TestEvent:
    @pytest.mark.event
    def test_open_event(self, login_to_admin):
        event_form = EventPage(self.driver)
        admin_event_form = AdminEventPage(self.driver)
        admin_event_form.go_to_url(f'{URL}/admin/events')
        time.sleep(3)
        admin_event_form.click_to('Редактировать', 'a', 1)
        admin_event_form.click_btn_tab_control()
        admin_event_form.scroll_down()
        admin_event_form.click_is_public('on')
        admin_event_form.click_btn_submit()
        event_form.go_to_url(f'{URL}/event/1990-06-11/admin/competition')
        event_form.click_nav_main_info()
        event_form.click_nav_rules()
        event_form.click_nav_price()

    @pytest.mark.event
    def test_open_list_participant(self):
        event_form = EventPage(self.driver)
        event_form.go_to_url(f'{URL}/')
        event_form.click_event_with_js()
        event_form.click_list_participant()
        event_form.verify_list_participant()

    @pytest.mark.event
    def test_open_qualification_results(self):
        event_form = EventPage(self.driver)
        event_form.go_to_url(f'{URL}/')
        event_form.click_event_with_js()
        event_form.click_qualification_results()
        event_form.verify_qualification_results()

    @pytest.mark.event
    def test_take_part(self, reg):
        event_form = EventPage(self.driver)
        event_form.go_to_url(f'{URL}/')
        event_form.click_event_with_js()
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
        event_form.go_to_url(f'{URL}/')
        event_form.click_event_with_js()
        time.sleep(3)
        event_form.select_category()
        time.sleep(3)
        event_form.select_birthday()
        time.sleep(3)
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
        event_form.go_to_url(f'{URL}/')
        event_form.click_event_with_js()
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
        event_form.go_to_url(f'{URL}/')
        event_form.click_event_with_js()
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




