import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from locators.EventPageLocators import EventPageLocators
from locators.RegistrationFormLocators import RegistrationForm
from pages.BasePage import BasePage


class EventPage(BasePage):
    def __init__(self, driver: WebElement):
        super().__init__(driver)

    def click_nav_main_info(self):
        self._wait_and_click(EventPageLocators.btn_main_info)

    def click_event_with_js(self):
        js = "document.querySelector('a[class=\"details-link\"] img').click()"
        self.driver.execute_script(js)

    def click_nav_sets(self):
        self._wait_and_click(EventPageLocators.btn_sets)

    def click_nav_rules(self):
        self._wait_and_click(EventPageLocators.btn_rules)

    def click_nav_price(self):
        self._wait_and_click(EventPageLocators.btn_price)

    def select_category(self):
        select = Select(self.driver.find_element(*EventPageLocators.select_category))
        select.select_by_index(1)

    def select_sets(self):
        select = Select(self.driver.find_element(*EventPageLocators.select_sets))
        select.select_by_index(1)

    def click_btn_take_part(self):
        self._wait_and_click(EventPageLocators.btn_take_part)

    def select_birthday(self):
        if self._element_visible(EventPageLocators.birthday):
            self._fill_field(EventPageLocators.birthday, '01.01.2000')

    def verify_success_take_part(self):
        self._try_wait_element(EventPageLocators.success_take_part)
        if self._element_visible(EventPageLocators.success_take_part):
            assert self._element_visible(EventPageLocators.success_take_part)
        if self._element_visible(EventPageLocators.success_take_part_2):
            assert self._element_visible(EventPageLocators.success_take_part_2)


