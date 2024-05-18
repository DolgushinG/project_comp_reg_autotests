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

    def select_sets(self, set: int):
        select = Select(self.driver.find_element(*EventPageLocators.select_sets))
        select.select_by_index(set)

    def select_changed_sets(self, set_take_part: int):
        select = Select(self.driver.find_element(*EventPageLocators.select_changed_sets))
        select.select_by_index(set_take_part)

    def click_btn_take_part(self):
        self._wait_and_click(EventPageLocators.btn_take_part)

    def select_birthday(self):
        if self._element_visible(EventPageLocators.birthday):
            self._fill_field(EventPageLocators.birthday, '01.01.2000')

    def verify_success_take_part(self):
        self._try_wait_element(EventPageLocators.success_take_part)
        if self._element_visible(EventPageLocators.success_take_part):
            assert self._element_visible(EventPageLocators.success_take_part)


    def _go_to_send_result(self):
        self._try_wait_element(EventPageLocators.success_take_part)
        self._click(EventPageLocators.success_take_part)

    def click_all_redpoints(self):
        self._wait_and_click(EventPageLocators.btn_all_redpoints)

    def click_send_result(self):
        self.scroll_down()
        time.sleep(1)
        self._wait_and_click(EventPageLocators.btn_send_result)

    def verify_already_take_part(self):
        if self._element_visible(EventPageLocators.success_take_part_2):
            assert self._element_visible(EventPageLocators.success_take_part_2)

    def grab_info_sets(self):
        return self._get_attribute(EventPageLocators.select_changed_sets, 'value')

    def click_btn_changed_set(self):
        self._wait_and_click(EventPageLocators.btn_change_set)
        self._wait_element(EventPageLocators.save_success)

    def click_list_participant(self):
        self._wait_and_click(EventPageLocators.btn_list_participant)

    def verify_list_participant(self):
        assert self._element_visible(EventPageLocators.list_participants), f'list_participants not found'

    def click_qualification_results(self):
        self._wait_and_click(EventPageLocators.btn_qualification_results)

    def verify_qualification_results(self):
        assert self._element_visible(EventPageLocators.qualification_results), f'list_participants not found'

