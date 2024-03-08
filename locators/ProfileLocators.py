from selenium.webdriver.common.by import By


class Profile:
    nav_profile = (By.ID, 'overview')
    title_profile = (By.XPATH, '//h6[contains(., \'Команда\')]')
    nav_events = (By.ID, 'events')
    title_events = (By.XPATH, "//h5[contains(., 'Вы не принимали участие ни в каких соревнованиях')]")
    nav_settings = (By.ID, 'setting')
    title_settings = (By.XPATH, '//label[contains(., \'Старый пароль\')]')
    nav_edit = (By.ID, 'edit')
    title_edit = (By.XPATH, '//label[contains(., \'Имя\')]')