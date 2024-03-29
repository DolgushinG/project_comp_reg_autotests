import time

import pytest

from constants import User, URL, DEFAULT_USER
from pages.RegistrationFormPage import RegistrationFormPage
from tools import random_word, get_email


@pytest.mark.usefixtures("driver")
class TestRegistrationForm:
    def test_reg(self):
        get_user = User()
        reg_form = RegistrationFormPage(self.driver)
        reg_form._go_to_url(f'{URL}/register')
        reg_form.fill_first_name(get_user.firstname)
        reg_form.fill_last_name(get_user.lastname)
        reg_form.select_gender()
        reg_form.fill_birthday(get_user.birthday)
        reg_form.fill_city(get_user.city)
        reg_form.fill_team(get_user.team)
        reg_form.fill_email(DEFAULT_USER.email)
        reg_form.fill_email(get_user.email)
        reg_form.fill_password(get_user.password)
        reg_form.fill_confirm_password(get_user.password)
        reg_form.click_btn_submit()
        reg_form.verify_profile()

