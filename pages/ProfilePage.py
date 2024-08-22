import time

from locators import ProfileLocators
from locators.ProfileLocators import Profile
from locators.RegistrationFormLocators import RegistrationForm
from pages.BasePage import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_profile(self):
        self.wait_and_click(RegistrationForm.nav_header_profile_image)

    def click_nav_profile(self):
        self.wait_and_click(Profile.nav_profile)

    def click_nav_events(self):
        self.wait_and_click(Profile.nav_events)

    def click_nav_password(self):
        self.wait_and_click(Profile.nav_settings)

    def click_nav_edit(self):
        time.sleep(2)
        self.wait_and_click(Profile.nav_edit)
        self.click(Profile.nav_edit)

    def verify_profile(self):
        self.wait_element(Profile.title_profile)
        time.sleep(1)

    def verify_events(self):
        self.try_wait_element(Profile.title_events)
        if not self.element_visible(Profile.title_events):
            time.sleep(1)
            assert self.element_visible(Profile.exist_title_events)
        else:
            time.sleep(1)
            assert self.element_visible(Profile.title_events)


    def verify_settings(self):
        self.wait_element(Profile.title_settings)
        assert self.element_visible(Profile.title_settings)
        time.sleep(1)

    def verify_edit(self):
        time.sleep(1)
        self.wait_element(Profile.title_edit)
        assert self.element_visible(Profile.title_edit)
        time.sleep(1)

    def fill_firstname(self, firstname: str):
        self.fill_field(Profile.input_lastname, firstname)

    def fill_lastname(self, lastname: str):
        self.fill_field(Profile.input_lastname, lastname)

    def click_btn_save(self):
        self.click(Profile.input_email)
        self.wait_and_click(Profile.btn_save)

    def get_info_profile(self) -> dict:
        time.sleep(2)
        info = {'firstname': self.get_attribute(Profile.input_firstname, 'value', True),
                'lastname': self.get_attribute(Profile.input_lastname, 'value', True),
                'team': self.get_attribute(Profile.input_team, 'value', True),
                'gender': self.get_attribute(Profile.input_gender, 'value', True),
                'birthday': self.get_attribute(Profile.input_birthday, 'value', True),
                'city': self.get_attribute(Profile.input_city, 'value', True),
                'sport_category': self.get_attribute(Profile.input_sport_category, 'value', True),
                'email': self.get_attribute(Profile.input_email, 'value', True)}
        return info

    def fill_team(self, team):
        self.fill_field(Profile.input_team, team)

    def fill_gender(self):
        time.sleep(2)
        self.click(Profile.input_gender)
        time.sleep(1)
        self.wait_and_click(Profile.gender_male)

    def fill_birthday(self, birthday):
        self.fill_field(Profile.input_birthday, birthday)

    def fill_city(self, city):
        self.fill_field(Profile.input_city, city)

    def fill_email(self, email):
        self.fill_field(Profile.input_email, email)

    def fill_sport_category(self):
        self.click(Profile.input_sport_category)
        self.wait_and_click(Profile.sport_category_1)

    def click_nav_analytics(self):
        self.wait_and_click(Profile.nav_analytics)

    def verify_analytics(self):
        self.wait_element(Profile.title_analytics)
        assert self.element_visible(Profile.title_analytics)
        time.sleep(1)

