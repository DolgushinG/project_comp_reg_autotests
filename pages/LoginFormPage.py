import time

from locators.RegistrationFormLocators import RegistrationForm
from pages.BasePage import BasePage


class LoginFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

