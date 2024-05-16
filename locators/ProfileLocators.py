from selenium.webdriver.common.by import By


class Profile:
    nav_profile = (By.ID, 'overview')
    title_profile = (By.XPATH, '//h6[contains(., \'Команда\')]')
    nav_events = (By.ID, 'events')
    title_events = (By.XPATH, "//*[contains(., 'Вы еще не принимали участие в соревнованиях')]")
    exist_title_events = (By.CSS_SELECTOR, "h2[id='heading6']")
    nav_settings = (By.ID, 'setting')
    title_settings = (By.XPATH, '//label[contains(., \'Старый пароль\')]')
    nav_edit = (By.ID, 'edit')
    title_edit = (By.XPATH, '//label[contains(., \'Имя\')]')