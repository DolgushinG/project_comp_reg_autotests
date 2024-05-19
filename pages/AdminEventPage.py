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

    def fill_field(self, field: str, value: str, type=By.ID) -> None:
        element = (type, f'{field}')
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

    def click_to(self, text, type="*") -> None:
        element = (By.XPATH, f'//{type}[contains(., "{text}")]')
        self._wait_and_click(element)

    def click_btn_tab_pay(self) -> None:
        self._wait_and_click(AdminEventPageLocators.btn_tab_pay)
        time.sleep(1)

    def click_btn_tab_control(self) -> None:
        self._wait_and_click(AdminEventPageLocators.btn_tab_control)

    def click_btn_tab_options(self) -> None:
        self._wait_and_click(AdminEventPageLocators.btn_tab_options)

    def click_to_btn_classic_radio_btn(self) -> None:
        self._wait_and_click(AdminEventPageLocators.classic_radio_btn)

    def click_to_all_route_radio_btn(self) -> None:
        self._wait_and_click(AdminEventPageLocators.all_route_radio_btn)

    def click_to_btn_add_categories(self, ) -> None:
        self._wait_and_click(AdminEventPageLocators.btn_add_category)

    def verify_header_admin(self) -> None:
        assert self._element_visible(AdminEventPageLocators.title_admin), f'title_admin not found'

    def verify_title_success_create(self) -> None:
        assert self._element_visible(AdminEventPageLocators.title_success_create)

    def go_to_main(self):
        self._wait_and_click(AdminEventPageLocators.nav_main)

    def verify_main(self):
        self._wait_element(AdminEventPageLocators.title_main)
        assert self._element_visible(AdminEventPageLocators.title_main)

    def verify_pay(self):
        self._wait_element(AdminEventPageLocators.title_pay)
        assert self._element_visible(AdminEventPageLocators.title_pay)

    def go_to_events(self):
        self._wait_and_click(AdminEventPageLocators.nav_events)

    def verify_events(self):
        self._wait_element(AdminEventPageLocators.title_events)
        assert self._element_visible(AdminEventPageLocators.title_events)

    def go_to_qualification(self):
        self._wait_and_click(AdminEventPageLocators.nav_qualification)

    def verify_qualification(self):
        self._wait_element(AdminEventPageLocators.title_qualification)
        assert self._element_visible(AdminEventPageLocators.title_qualification)

    def go_to_semifinal(self):
        self._wait_and_click(AdminEventPageLocators.nav_semifinal)

    def verify_semifinal(self):
        self._wait_element(AdminEventPageLocators.title_semifinal)
        assert self._element_visible(AdminEventPageLocators.title_semifinal)

    def go_to_setting_routes(self):
        self._wait_and_click(AdminEventPageLocators.nav_setting_routes)

    def verify_setting_routes(self):
        self._wait_element(AdminEventPageLocators.title_setting_routes)
        assert self._element_visible(AdminEventPageLocators.title_setting_routes)

    def go_to_final(self):
        self._wait_and_click(AdminEventPageLocators.nav_final)

    def verify_final(self):
        self._wait_element(AdminEventPageLocators.title_final)
        assert self._element_visible(AdminEventPageLocators.title_final)

    def go_to_pay(self):
        self._wait_and_click(AdminEventPageLocators.nav_pay)

    def scroll_up(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(1)

    def delete_event(self):
        self._wait_and_click(AdminEventPageLocators.event_2)

    def delete_routes(self):
        pass
