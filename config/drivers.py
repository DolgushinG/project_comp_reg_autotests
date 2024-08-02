import os

from selenium.webdriver.chrome.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def get_driver(browser_name: str, options):
    if browser_name == 'chrome':
        service = Service(ChromeDriverManager().install())
        path = service.path
        service.path = path.replace('THIRD_PARTY_NOTICES.', "")
        os.chmod(service.path, 0o755)
        return webdriver.Chrome(service=service, options=options)
    if browser_name == 'firefox':
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
