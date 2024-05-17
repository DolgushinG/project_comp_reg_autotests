from selenium.webdriver.common.by import By


class EventPageLocators:
    btn_main_info = (By.XPATH, '//button[contains(., \'Общая информация\')]')
    btn_sets = (By.XPATH, "//button[contains(., 'Сеты')]")
    btn_rules = (By.XPATH, '//button[contains(., \'Положение\')]')
    btn_price = (By.XPATH, '//button[contains(., \'Стартовый взнос\')]')
    select_category = (By.ID, 'floatingSelectCategory')
    category = (By.XPATH, '//*[contains(., "Новичок")]')
    select_sets = (By.ID, 'floatingSelect')
    set = (By.XPATH, '//*[contains(., "Сет 1")]')
    btn_take_part = (By.ID, 'btn-participant')
    birthday = (By.ID, 'birthday')
    success_take_part = (By.XPATH, '//*[contains(., "Внести результат")]')
    success_take_part_2 = (By.XPATH, '//*[contains(., "Вы принимаете участие")]')