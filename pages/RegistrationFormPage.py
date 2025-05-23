import time
from time import sleep

from locators.RegistrationFormLocators import RegistrationForm
from pages.BasePage import BasePage


class RegistrationFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def remove_footer(self):
        self.driver.execute_script('document.querySelector(\'footer\').remove()')
        self.driver.execute_script('document.querySelector(\'#close-fixedban\').remove()')

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def fill_first_name(self, first_name: str) -> None:
        self.fill_field(RegistrationForm.first_name, first_name)

    def fill_first_name_group(self, first_name: str) -> None:
        self.fill_field(RegistrationForm.first_name_group, first_name)

    def fill_last_name_group(self, last_name: str) -> None:
        self.fill_field(RegistrationForm.last_name_group, last_name)

    def fill_last_name(self, last_name: str) -> None:
        self.fill_field(RegistrationForm.last_name, last_name)

    def fill_birthday(self, birthday: str) -> None:
        sleep(1)
        self.fill_field(RegistrationForm.birthday, birthday)

    def fill_city(self, last_name: str) -> None:
        self.fill_field(RegistrationForm.city, last_name)

    def fill_team(self, last_name: str) -> None:
        self.fill_field(RegistrationForm.team, last_name)

    def fill_confirm_password(self, last_name: str) -> None:
        self.fill_field(RegistrationForm.confirm_password, last_name)

    def click_checkbox_accept_terms(self):
        self.click(RegistrationForm.terms_checkbox)
    def click_checkbox_gender_male(self) -> None:
        self.click(RegistrationForm.gender_checkbox_1)

    def fill_mobile_phone(self, phone: str) -> None:
        self.fill_field(RegistrationForm.user_mobile_number, phone)

    def click_checkbox_hobbies_sports(self) -> None:
        self.wait_element(RegistrationForm.hobbies_checkbox_1)
        self.click(RegistrationForm.hobbies_checkbox_1)

    def attach_picture(self, path) -> None:
        self.fill_field(RegistrationForm.picture, path)

    def fill_current_address(self, address: str) -> None:
        self.fill_field(RegistrationForm.current_address, address)

    def select_state(self) -> None:
        self.wait_element(RegistrationForm.state)
        self.wait_and_click(RegistrationForm.state)
        self.wait_element(RegistrationForm.NCR)
        self.wait_and_click(RegistrationForm.NCR)

    def select_city(self) -> None:
        self.wait_and_click(RegistrationForm.city)
        self.wait_element(RegistrationForm.DELHI)
        self.wait_and_click(RegistrationForm.DELHI)

    def select_gender(self) -> None:
        self.wait_and_click(RegistrationForm.gender)
        self.wait_element(RegistrationForm.male)
        self.wait_and_click(RegistrationForm.male)

    def click_btn_submit(self) -> None:
        self.scroll_down()
        time.sleep(1)
        self.wait_and_click(RegistrationForm.btn_submit)

    def click_btn_submit_group_registration(self) -> None:
        self.scroll_down()
        time.sleep(1)
        self.wait_and_click(RegistrationForm.btn_submit_group_registration)

    def verify_confirm_form(self) -> None:
        time.sleep(2)
        assert self.element_visible(RegistrationForm.modal_submitting_form)

    def verify_profile(self) -> None:
        self.try_wait_element(RegistrationForm.nav_profile)
        if self.element_visible(RegistrationForm.nav_profile):
            text = self.get_text(RegistrationForm.nav_profile)
            assert 'ПРОФИЛЬ' == text, f"EXP - ПРОФИЛЬ, REAL - {text}"
        else:
            assert self.element_visible(RegistrationForm.nav_profile_2), "Profile not found"


    def verify_full_name(self, firstname: str, lastname: str) -> None:
        full_name = f"{firstname} {lastname}"
        text = self.get_text(RegistrationForm.modal_name)
        assert full_name == text, f"EXP - {full_name}, REAL - {text}"

    def verify_email(self, email: str) -> None:
        text = self.get_text(RegistrationForm.modal_email)
        assert email == text, f"EXP - {email}, REAL - {text}"

    def verify_gender_male(self) -> None:
        text = self.get_text(RegistrationForm.modal_gender_male)
        assert 'Male' == text, f"EXP - 'Male', REAL - {text}"

    def verify_mobile_phone(self, phone: str) -> None:
        text = self.get_text(RegistrationForm.modal_mobile_number)
        assert phone == text, f"EXP - {phone}, REAL - {text}"

    def verify_checkbox_hobbies_sports(self) -> None:
        text = self.get_text(RegistrationForm.modal_hobbies)
        assert 'Sports' == text, f"EXP - 'Sports', REAL - {text}"

    def verify_picture(self) -> None:
        text = self.get_text(RegistrationForm.modal_picture)
        assert 'picture.png' == text, f"EXP - 'Picture.png', REAL - {text}"

    def verify_current_address(self, address: str) -> None:
        text = self.get_text(RegistrationForm.modal_current_address)
        assert address == text, f"EXP - {address}, REAL - {text}"

    def verify_state_and_city(self, state: str, city: str) -> None:
        state_and_city = f"{state} {city}"
        text = self.get_text(RegistrationForm.modal_state_and_city)
        assert state_and_city == text, f"EXP - {state_and_city}, REAL - {text}"

    def verify_btn_title_success_creaeted(self):
        self.try_wait_element(RegistrationForm.text_btn_success_created)
        assert self.element_visible(RegistrationForm.text_btn_success_created), "text_btn_success_created not found"
