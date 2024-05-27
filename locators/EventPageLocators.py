from selenium.webdriver.common.by import By


class EventPageLocators:
    select_sport_category = (By.ID, 'floatingSelectSportCategory')
    btn_main_info = (By.XPATH, '//button[contains(., \'Общая информация\')]')
    btn_sets = (By.XPATH, "//button[contains(., 'Сеты')]")
    btn_rules = (By.XPATH, '//button[contains(., \'Положение\')]')
    btn_price = (By.XPATH, '//button[contains(., \'Стартовый взнос\')]')
    btn_list_participant = (By.XPATH, '//a[contains(., \'Список участников\')]')
    btn_qualification_results = (By.XPATH, '//a[contains(., \'Предварительные результаты\')]')
    qualification_results = (By.XPATH, '//h5[contains(., \'Мужчины\')]')
    list_participants = (By.ID, 'borderedTabJustified')
    select_category = (By.ID, 'floatingSelectCategory')
    select_sets = (By.ID, 'floatingSelect')
    select_changed_sets = (By.ID, 'floatingSelectChangeSet')
    btn_change_set = (By.ID, 'btn-participant-change-set')
    btn_take_part = (By.ID, 'btn-participant')
    birthday = (By.ID, 'birthday')
    success_take_part = (By.XPATH, '//a[contains(., "Внести результаты")]')
    save_success = (By.XPATH, '//button[contains(., "Успешно сохранено")]')
    btn_all_redpoints = (By.ID, 'all-redpoint')
    btn_send_result = (By.ID, 'btn-send-result')
    success_take_part_2 = (By.XPATH, '//button[contains(., "Вы принимаете участие")]')
