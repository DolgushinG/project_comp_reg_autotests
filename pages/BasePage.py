import time

from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

from locators.AdminEventPageLocators import AdminEventPageLocators
from locators.RegistrationFormLocators import RegistrationForm


class BasePage:
    TIME = 15

    def __init__(self, driver):
        self.driver = driver

    def _get_attribute(self, element: tuple, attribute: str):
        return self.driver.find_element(*element).get_attribute(attribute)

    def _wait_and_click(self, element: tuple):
        WebDriverWait(self.driver, ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
                      timeout=self.TIME) \
            .until(EC.element_to_be_clickable(element)) \
            .click()

    def _click(self, element: tuple):
        wait = WebDriverWait(self.driver, timeout=10)
        try:
            el = wait.until(EC.element_to_be_clickable(element))
            el.click()
        except ElementClickInterceptedException:
            print("Trying to click on the button again")
            self.driver.execute_script("arguments[0].click()", el)

    def _find_element(self, element: tuple):
        return self.driver.find_element(*element)

    def _wait_element(self, element: tuple):
        try:
            return WebDriverWait(self.driver, self.TIME).until(EC.presence_of_element_located(element))
        except TimeoutException and NoSuchElementException:
            msg = f'Element not found, element: "{element}"'
            raise NoSuchElementException(msg)

    def _elements_presenter(self, element: tuple) -> bool:
        return bool(len(self.driver.find_elements(*element)))

    def _clear_field(self, element: tuple):
        self.driver.find_element(*element).clear()

    def _go_to_url(self, url: str) -> None:
        self.driver.get(url)

    def _fill_field(self, element: tuple, text: str, clear=True):
        el = self._wait_element(element)
        if clear:
            el.clear()
        el.send_keys(text)

    def _press_key(self, element: tuple, keys):
        self.driver.find_element(element).send_keys(keys)

    def _get_text(self, element: tuple):
        return self._wait_element(element).text

    def scroll_down(self):
        # time.sleep(1)
        pre_scroll_height = self.driver.execute_script('return document.body.scrollHeight;')
        run_time, max_run_time = 0, 1
        while True:
            iteration_start = time.time()
            # Scroll webpage, the 100 allows for a more 'aggressive' scroll
            self.driver.execute_script('window.scrollTo(0, 100*document.body.scrollHeight);')

            post_scroll_height = self.driver.execute_script('return document.body.scrollHeight;')

            scrolled = post_scroll_height != pre_scroll_height
            timed_out = run_time >= max_run_time

            if scrolled:
                run_time = 0
                pre_scroll_height = post_scroll_height
            elif not scrolled and not timed_out:
                run_time += time.time() - iteration_start
            elif not scrolled and timed_out:
                break

    def _element_visible(self, element: tuple):
        try:
            element = self.driver.find_element(*element)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def fill_email(self, email: str) -> None:
        self._fill_field(RegistrationForm.email, email)

    def fill_password(self, password: str) -> None:
        self._fill_field(RegistrationForm.password, password)

    def verify_header_profile(self):
        assert self._element_visible(RegistrationForm.nav_header_profile_image)

    def click_btn_submit(self) -> None:
        self._wait_and_click(RegistrationForm.btn_submit)