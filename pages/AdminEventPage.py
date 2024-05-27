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
        self.fill_field(AdminEventPageLocators.user_name, username)

    def fill_password(self, password: str) -> None:
        self.fill_field(AdminEventPageLocators.password, password)

    def fill_field_dinamic(self, field: str, value: str, type=By.ID) -> None:
        element = (type, f'{field}')
        self.fill_field(element, value)

    def fill_field_description(self, value: str) -> None:
        self.fill_field(AdminEventPageLocators.description_text_area, value)

    def upload_image(self, value: str) -> None:
        self.fill_field(AdminEventPageLocators.image, value)

    def fill_field_category(self, number: int, value: str) -> None:
        if number == 1:
            element = AdminEventPageLocators.field_category_1
        if number == 2:
            element = AdminEventPageLocators.field_category_2
        self.fill_field(element, value)

    def click_btn_submit(self) -> None:
        self.scroll_down()
        self.wait_and_click(AdminEventPageLocators.btn_submit)

    def click_btn_enter(self) -> None:
        self.wait_and_click(AdminEventPageLocators.btn_enter)

    def click_to(self, text, type="*", index=0) -> None:
        if index == 0:
            element = (By.XPATH, f'//{type}[contains(., "{text}")]')
        if index > 0:
            element = (By.XPATH, f'(//{type}[contains(., "{text}")])[{index}]')
        self.wait_and_click(element)

    def is_semifinal(self):
        time.sleep(2)
        self.wait_and_click(AdminEventPageLocators.is_semifinal)

    def click_btn_tab_pay(self) -> None:
        self.wait_and_click(AdminEventPageLocators.btn_tab_pay)
        time.sleep(1)

    def click_btn_tab_control(self) -> None:
        self.wait_and_click(AdminEventPageLocators.btn_tab_control)

    def click_btn_tab_options(self) -> None:
        self.wait_and_click(AdminEventPageLocators.btn_tab_options)

    def click_to_btn_classic_radio_btn(self) -> None:
        self.wait_and_click(AdminEventPageLocators.classic_radio_btn)

    def click_to_btn_france_system_radio_btn(self) -> None:
        self.wait_and_click(AdminEventPageLocators.france_system_radio_btn)

    def click_to_all_route_radio_btn(self) -> None:
        self.wait_and_click(AdminEventPageLocators.all_route_radio_btn)

    def click_to_btn_add_categories(self, ) -> None:
        self.wait_and_click(AdminEventPageLocators.btn_add_category)

    def verify_header_admin(self) -> None:
        assert self.element_visible(AdminEventPageLocators.title_admin), f'title_admin not found'

    def verify_title_success_create(self) -> None:
        assert self.element_visible(AdminEventPageLocators.title_success_create)

    def go_to_main(self):
        self.wait_and_click(AdminEventPageLocators.nav_main)

    def verify_main(self):
        self.wait_element(AdminEventPageLocators.title_main)
        assert self.element_visible(AdminEventPageLocators.title_main)

    def verify_pay(self):
        self.wait_element(AdminEventPageLocators.title_pay)
        assert self.element_visible(AdminEventPageLocators.title_pay)

    def go_to_events(self):
        time.sleep(1)
        self.wait_and_click(AdminEventPageLocators.nav_events)

    def verify_events(self):
        self.wait_element(AdminEventPageLocators.title_events)
        assert self.element_visible(AdminEventPageLocators.title_events)

    def go_to_qualification(self):
        self.wait_and_click(AdminEventPageLocators.nav_qualification)

    def verify_qualification(self):
        self.wait_element(AdminEventPageLocators.title_qualification)
        assert self.element_visible(AdminEventPageLocators.title_qualification)

    def go_to_semifinal(self):
        self.wait_and_click(AdminEventPageLocators.nav_semifinal)

    def verify_semifinal(self):
        self.wait_element(AdminEventPageLocators.title_semifinal)
        assert self.element_visible(AdminEventPageLocators.title_semifinal)

    def go_to_setting_routes(self):
        self.wait_and_click(AdminEventPageLocators.nav_setting_routes)

    def verify_setting_routes(self):
        self.wait_element(AdminEventPageLocators.title_setting_routes)
        assert self.element_visible(AdminEventPageLocators.title_setting_routes)

    def go_to_final(self):
        self.wait_and_click(AdminEventPageLocators.nav_final)

    def verify_final(self):
        self.wait_element(AdminEventPageLocators.title_final)
        assert self.element_visible(AdminEventPageLocators.title_final)

    def go_to_pay(self):
        self.wait_and_click(AdminEventPageLocators.nav_pay)

    def scroll_up(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(1)

    def delete_event(self):
        time.sleep(1)
        if self.element_visible(AdminEventPageLocators.event_festival_2024):
            self.wait_and_click(AdminEventPageLocators.event_festival_2024)
            self.click_to('Подтвердить', 'button')
            self.click_to('OK', 'button')

    def verify_result_final(self):
        assert 0 < len(self.find_elements(AdminEventPageLocators.result_final)), f'results_final not found'

    def diactivate_old_event(self):
        time.sleep(1)
        self.wait_and_click(AdminEventPageLocators.event_competition_yes)

    def diactivate_new_event(self):
        time.sleep(1)
        self.wait_and_click(AdminEventPageLocators.event_festival_2024_yes)

    def activate_new_event(self):
        time.sleep(1)
        self.wait_and_click(AdminEventPageLocators.event_festival_2024_no)

    def activate_old_event(self):
        time.sleep(1)
        self.wait_and_click(AdminEventPageLocators.event_competition_no)

    def click_to_generate_result_final(self):
        self.wait_and_click(AdminEventPageLocators.btn_generate_result_final)
        self.click_to('OK', 'button')
        time.sleep(3)

    def click_to_btn_all_route_radio_btn(self):
        self.wait_and_click(AdminEventPageLocators.all_route_radio_btn)

    def verify_result_qualification(self):
        self.wait_element(AdminEventPageLocators.result_qualification, 100)
