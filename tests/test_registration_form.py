import time

import pytest

from constants import User, URL, DEFAULT_USER
from pages.RegistrationFormPage import RegistrationFormPage
from tools import random_word, get_email


@pytest.mark.usefixtures("driver")
@pytest.mark.main
class TestRegistrationForm:
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

