import time

import pytest

from constants import User, URL, DEFAULT_USER
from pages.AdminEventPage import AdminEventPage
from pages.EventPage import EventPage
from pages.RegistrationFormPage import RegistrationFormPage
from tools import random_word, get_email


@pytest.mark.usefixtures("driver")
class TestRegistrationForm:
    @pytest.mark.main
    def test_reg(self):
        get_user = User()
        reg_form = RegistrationFormPage(self.driver)
        reg_form.go_to_url(f'{URL}/register')
        reg_form.fill_first_name(get_user.firstname)
        reg_form.fill_last_name(get_user.lastname)
        reg_form.select_gender()
        reg_form.fill_email(get_email())
        reg_form.fill_password(get_user.password)
        reg_form.fill_confirm_password(get_user.password)
        reg_form.click_checkbox_accept_terms()
        reg_form.click_btn_submit()
        reg_form.verify_profile()


    @pytest.mark.main
    def test_event_classic_checking_group_registration(self, login):
        event_form = EventPage(self.driver)
        reg_form = RegistrationFormPage(self.driver)
        get_user = User()
        event_form.go_to_url(f'{URL}/')
        event_form.click_event_with_js()
        event_form.click_to_btn_group_registration()
        event_form.verify_title_group_registration()
        event_form.click_add_participant()
        reg_form.fill_first_name_group(get_user.firstname)
        reg_form.fill_last_name_group(get_user.lastname)
        reg_form.select_gender()
        event_form.select_category_group()
        event_form.select_group_sport_category()
        event_form.select_sets_group()
        reg_form.click_btn_submit_group_registration()
        reg_form.verify_btn_title_success_creaeted()