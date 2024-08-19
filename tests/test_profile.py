import time

import pytest

from constants import URL, DEFAULT_USER
from pages.LoginFormPage import LoginFormPage
from pages.ProfilePage import ProfilePage
from tools import random_word


@pytest.mark.usefixtures("driver")
class TestProfileForm:
    @pytest.mark.main
    def test_navigation_profile(self, login):
        profile_page = ProfilePage(self.driver)
        profile_page.click_nav_profile()
        profile_page.verify_profile()
        profile_page.click_nav_events()
        profile_page.verify_events()
        profile_page.click_nav_analytics()
        profile_page.verify_analytics()
        profile_page.click_nav_password()
        profile_page.verify_settings()
        profile_page.click_nav_edit()
        profile_page.verify_edit()

    @pytest.mark.main
    def test_edit_profile(self, login):
        profile_page = ProfilePage(self.driver)
        profile_page.click_nav_profile()
        profile_page.verify_profile()
        profile_page.click_nav_edit()
        profile_page.verify_edit()
        info_before = profile_page.get_info_profile()
        profile_page.fill_firstname("tester"+random_word(3, 5))
        profile_page.fill_lastname("tester"+random_word(3, 5))
        profile_page.fill_team("tester"+random_word(3, 5))
        profile_page.fill_gender()
        profile_page.fill_birthday("1990-05-29")
        profile_page.fill_city("testeros"+random_word(3, 5))
        profile_page.fill_sport_category()
        profile_page.fill_email("Tester@tester.ru")
        profile_page.click_btn_save()
        time.sleep(4)
        info_after = profile_page.get_info_profile()
        assert info_before != info_after
        profile_page.fill_firstname("tester")
        profile_page.fill_lastname("tester")
        profile_page.fill_team("tester")
        profile_page.fill_gender()
        profile_page.fill_birthday("1990-05-29")
        profile_page.fill_city("testeros")
        profile_page.fill_sport_category()
        profile_page.fill_email("Tester@tester.ru")
        profile_page.click_btn_save()
        time.sleep(4)

