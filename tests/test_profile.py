import time

import pytest

from constants import URL, DEFAULT_USER
from pages.LoginFormPage import LoginFormPage
from pages.ProfilePage import ProfilePage


@pytest.mark.usefixtures("driver")
class TestProfileForm:
    def test_navigation_profile(self):
        login_form = LoginFormPage(self.driver)
        login_form._go_to_url(f'{URL}/login')
        login_form.fill_email(DEFAULT_USER.email)
        login_form.fill_password(DEFAULT_USER.password)
        login_form.click_btn_submit()
        login_form.verify_header_profile()
        profile_page = ProfilePage(self.driver)
        profile_page._go_to_url(f'{URL}/profile')
        profile_page.click_nav_profile()
        profile_page.verify_profile()
        profile_page.click_nav_events()
        profile_page.verify_events()
        profile_page.click_nav_password()
        profile_page.verify_settings()
        profile_page.click_nav_edit()
        profile_page.verify_edit()



