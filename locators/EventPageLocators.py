from selenium.webdriver.common.by import By


class EventPageLocators:
    btn_main_info = (By.XPATH, '//button[contains(., \'Общая информация\')]')
    btn_sets = (By.XPATH, "//button[contains(., 'Сеты')]")
    btn_rules = (By.XPATH, '//button[contains(., \'Положение\')]')
    btn_price = (By.XPATH, '//button[contains(., \'Стартовый взнос\')]')