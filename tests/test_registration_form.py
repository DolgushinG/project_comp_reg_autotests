import time

import pytest

from constants import DATA_ROOT
from pages.StudentRegistrationFormPage import StudentRegistrationFormPage
from tools import random_word, get_email


@pytest.mark.usefixtures("driver")
class TestRegistrationForm:
    def test_open_page(self):
        student_reg_form = StudentRegistrationFormPage(self.driver)
        student_reg_form._go_to_url('http://127.0.0.1:8000/register')
        student_reg_form.fill_first_name(random_word(4, 8))
        student_reg_form.fill_last_name(random_word(4, 8))
        student_reg_form.select_gender()
        student_reg_form.fill_birthday('2020-05-21')
        student_reg_form.fill_city(random_word(4, 8))
        student_reg_form.fill_team(random_word(4, 8))
        student_reg_form.fill_email(get_email())
        student_reg_form.fill_password("password")
        student_reg_form.fill_confirm_password("password")
        student_reg_form.click_btn_submit()
        student_reg_form.verify_profile()
