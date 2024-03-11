import time

from selenium.webdriver.remote.webelement import WebElement

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

