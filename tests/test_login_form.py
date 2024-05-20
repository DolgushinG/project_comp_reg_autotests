import time

import pytest

from constants import URL, DEFAULT_USER
from pages.LoginFormPage import LoginFormPage


@pytest.mark.usefixtures("driver")
class TestLoginForm:

    def test_login(self):
        login_form = LoginFormPage(self.driver)
        login_form.go_to_url(f'{URL}/login')
        login_form.fill_email(DEFAULT_USER.email)
        login_form.fill_password(DEFAULT_USER.password)
        login_form.click_btn_submit()
        login_form.verify_header_profile()




