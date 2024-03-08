import time

from locators import ProfileLocators
from locators.ProfileLocators import Profile
from locators.RegistrationFormLocators import RegistrationForm
from pages.BasePage import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_profile(self):
        self._wait_and_click(RegistrationForm.nav_header_profile_image)

    def click_nav_profile(self):
        self._wait_and_click(Profile.nav_profile)

    def click_nav_events(self):
        self._wait_and_click(Profile.nav_events)

    def click_nav_password(self):
        self._wait_and_click(Profile.nav_settings)

    def click_nav_edit(self):
        self._wait_and_click(Profile.nav_edit)

    def verify_profile(self):
        self._wait_element(Profile.title_profile)
        assert self._element_visible(Profile.title_profile)

    def verify_events(self):
        self._wait_element(Profile.title_events)
        assert self._element_visible(Profile.title_events)

    def verify_settings(self):
        self._wait_element(Profile.title_settings)
        assert self._element_visible(Profile.title_settings)

    def verify_edit(self):
        self._wait_element(Profile.title_edit)
        assert self._element_visible(Profile.title_edit)
