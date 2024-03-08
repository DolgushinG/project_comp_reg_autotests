import time

import pytest

from constants import User, URL, DEFAULT_USER
from pages.StudentRegistrationFormPage import StudentRegistrationFormPage
from tools import random_word, get_email


@pytest.mark.usefixtures("driver")
class TestRegistrationForm:
    def test_reg(self ):
        get_user = User()
        student_reg_form = StudentRegistrationFormPage(self.driver)
        student_reg_form._go_to_url(f'{URL}/register')
        student_reg_form.fill_first_name(get_user.firstname)
        student_reg_form.fill_last_name(get_user.lastname)
        student_reg_form.select_gender()
        student_reg_form.fill_birthday(get_user.birthday)
        student_reg_form.fill_city(get_user.city)
        student_reg_form.fill_team(get_user.team)
        student_reg_form.fill_email(get_user.email)
        student_reg_form.fill_password(get_user.password)
        student_reg_form.fill_confirm_password(get_user.password)
        student_reg_form.click_btn_submit()
        student_reg_form.verify_profile()
