import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from locators.AdminEventPageLocators import AdminEventPageLocators
from locators.EventPageLocators import EventPageLocators
from locators.RegistrationFormLocators import RegistrationForm
from pages.BasePage import BasePage


class AdminEventPage(BasePage):
    def __init__(self, driver: WebElement):
        super().__init__(driver)

    def fill_username(self, username: str) -> None:
        self._fill_field(AdminEventPageLocators.user_name, username)

    def fill_password(self, password: str) -> None:
        self._fill_field(AdminEventPageLocators.password, password)

    def fill_field(self, field: str, value: str) -> None:
        element = (By.ID, f'{field}')
        self._fill_field(element, value)

    def fill_field_description(self, value: str) -> None:
        self._fill_field(AdminEventPageLocators.description_text_area, value)

    def upload_image(self, value: str) -> None:
        self._fill_field(AdminEventPageLocators.image, value)

    def fill_field_category(self, number: int, value: str) -> None:
        if number == 1:
            element = AdminEventPageLocators.field_category_1
        if number == 2:
            element = AdminEventPageLocators.field_category_2
        self._fill_field(element, value)

    def click_btn_submit(self) -> None:
        self.scroll_down()
        self._wait_and_click(AdminEventPageLocators.btn_submit)

    def click_btn_enter(self) -> None:
        self._wait_and_click(AdminEventPageLocators.btn_enter)
    def click_to(self, text) -> None:
        element = (By.XPATH, f'//*[contains(text(), "{text}")]')
        self._wait_and_click(element)

    def click_to_btn_classic_radio_btn(self) -> None:
        self._wait_and_click(AdminEventPageLocators.classic_radio_btn)

    def click_to_all_route_radio_btn(self) -> None:
        self._wait_and_click(AdminEventPageLocators.all_route_radio_btn)

    def click_to_btn_add_categories(self, ) -> None:
        self._wait_and_click(AdminEventPageLocators.btn_add_category)

    def verify_header_admin(self) -> None:
        self._wait_and_click(AdminEventPageLocators.title_admin)
    def verify_title_success_create(self) -> None:
        self._wait_element(AdminEventPageLocators.title_success_create)
        assert self._element_visible(AdminEventPageLocators.title_success_create)
