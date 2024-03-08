from typing import Any

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_options(browser_name: str) -> Any:
    if browser_name == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        return chrome_options
    if browser_name == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--disable-extensions")
        return firefox_options
