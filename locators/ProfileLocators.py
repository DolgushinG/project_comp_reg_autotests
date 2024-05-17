from selenium.webdriver.common.by import By


class Profile:
    nav_profile = (By.ID, 'overview')
    title_profile = (By.XPATH, '//h6[contains(., \'Команда\')]')
    nav_events = (By.ID, 'events')
    input_lastname = (By.ID, 'lastname')
    input_firstname = (By.ID, 'firstname')
    input_city = (By.ID, 'city')
    input_email = (By.ID, 'email')
    input_team = (By.ID, 'team')
    input_birthday = (By.ID, 'birthday')
    input_sport_category = (By.CSS_SELECTOR, "[name='sport_category']")
    sport_category_1 = (By.XPATH, '//*[contains(., "I разряд")]')
    input_gender = (By.ID, 'gender')
    gender_male = (By.XPATH, '//*[contains(., "Муж")]')
    btn_save = (By.ID, 'saveChanges')
    title_events = (By.XPATH, "//*[contains(., 'Вы еще не принимали участие в соревнованиях')]")
    exist_title_events = (By.CLASS_NAME, "accordion-button")
    nav_settings = (By.ID, 'setting')
    title_settings = (By.XPATH, '//label[contains(., \'Старый пароль\')]')
    nav_edit = (By.ID, 'edit')
    title_edit = (By.XPATH, '//label[contains(., \'Имя\')]')