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
        self._click(Profile.nav_edit)

    def verify_profile(self):
        self._wait_element(Profile.title_profile)
        assert self._element_visible(Profile.title_profile)

    def verify_events(self):
        self._try_wait_element(Profile.title_events)
        if not self._element_visible(Profile.title_events):
            time.sleep(1)
            assert self._element_visible(Profile.exist_title_events)
        else:
            time.sleep(1)
            assert self._element_visible(Profile.title_events)


    def verify_settings(self):
        self._wait_element(Profile.title_settings)
        assert self._element_visible(Profile.title_settings)

    def verify_edit(self):
        self._wait_element(Profile.title_edit)
        assert self._element_visible(Profile.title_edit)

    def fill_firstname(self, firstname: str):
        self._fill_field(Profile.input_lastname, firstname)

    def fill_lastname(self, lastname: str):
        self._fill_field(Profile.input_lastname, lastname)

    def click_btn_save(self):
        self._click(Profile.input_email)
        self._wait_and_click(Profile.btn_save)

    def get_info_profile(self) -> dict:
        time.sleep(2)
        info = {'firstname': self._get_attribute(Profile.input_firstname, 'value', True),
                'lastname': self._get_attribute(Profile.input_lastname, 'value', True),
                'team': self._get_attribute(Profile.input_team, 'value', True),
                'gender': self._get_attribute(Profile.input_gender, 'value', True),
                'birthday': self._get_attribute(Profile.input_birthday, 'value', True),
                'city': self._get_attribute(Profile.input_city, 'value', True),
                'sport_category': self._get_attribute(Profile.input_sport_category, 'value', True),
                'email': self._get_attribute(Profile.input_email, 'value', True)}
        return info

    def fill_team(self, team):
        self._fill_field(Profile.input_team, team)

    def fill_gender(self):
        time.sleep(2)
        self._click(Profile.input_gender)
        time.sleep(1)
        self._wait_and_click(Profile.gender_male)

    def fill_birthday(self, birthday):
        self._fill_field(Profile.input_birthday, birthday)

    def fill_city(self, city):
        self._fill_field(Profile.input_city, city)

    def fill_email(self, email):
        self._fill_field(Profile.input_email, email)

    def fill_sport_category(self):
        self._click(Profile.input_sport_category)
        self._wait_and_click(Profile.sport_category_1)

