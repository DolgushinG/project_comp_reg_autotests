from selenium.webdriver.common.by import By


class AdminEventPageLocators:
    user_name = (By.CSS_SELECTOR, 'input[name="username"]')
    password = (By.CSS_SELECTOR, 'input[name="password"]')
    btn_submit = (By.XPATH, '//button[contains(text(), "Отправить")]')
    btn_enter = (By.CSS_SELECTOR, 'button[type="submit"]')
    title_admin = (By.XPATH, '//*[contains(text(), "Мой сайт скалодром")]')
    title_success_create = (By.XPATH, '//*[contains(text(), "Соревнование успешно сохранено")]')
    image = (By.CSS_SELECTOR, 'input[type="file"]')
    description_text_area = (By.XPATH, '//*[contains(@class, \'note-editable\')]')
    classic_radio_btn = (By.XPATH, '//*[contains(@class, "is_qualification_counting_like_final0")]')
    all_route_radio_btn = (By.XPATH, '//div[contains(@class, \'mode2\')]')
    btn_add_category = (By.XPATH, "//div[contains(@class, 'categories-add')]")
    field_category_1 = (By.XPATH, "(//input[contains(@name, 'categories[values][]')])[1]")
    field_category_2 = (By.XPATH, "(//input[contains(@name, 'categories[values][]')])[2]")